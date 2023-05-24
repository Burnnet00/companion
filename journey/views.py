from django.shortcuts import render
from django.views.generic.base import View
from .models import Post, Comments
from rest_framework import routers
from .api import PostViewset


class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'journey/index.html', {'posts': posts})

router = routers.DefaultRouter()
router.register('api/journey', PostViewset, 'journey')

urlpatterns = router.urls
