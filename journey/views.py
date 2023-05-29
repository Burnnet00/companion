from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments
from rest_framework import routers
from .api import PostViewset
from .form import PostForm


class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'journey/index.html', {'posts': posts})

router = routers.DefaultRouter()
router.register('api/journey', PostViewset, 'journey')

urlpatterns = router.urls

class PostViewDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'journey/detail.html', {'post': post})












# class AddComments(View):
#     '''add comments'''
#     def post(self, request, pk):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.post_id = pk
#             form.save()
#         return redirect(f'/{pk}')
