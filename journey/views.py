from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments
from rest_framework import routers
from .api import PostViewset
from .form import PostForm, CommentsForm


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

class AddComment(View):
    '''add comments'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

class AddPost(View):
    def posts(self, request):
        posts = Post.objects.all()
        return render(request, 'journey/thx.html', {'posts': posts})


        # pform = PostForm(request.POST)
        # pform.save(commit=False)




# class AddPost(View):
#     def get(self,request):
#         if request.POST:
#             autor = request.POST['autor']
#             age = request.POST['age']
#             sex = request.POST['sex']
#             image = request.POST['image']
#             title = request.POST['title']
#             place = request.POST['place']
#             description = request.POST['description']
#             phone = request.POST['phone']# отримуемо параметри з полями name, phone
#             mail = request.POST['mail']
#
#             element = Post(
#                 autor=autor,
#                 age=age,
#                 sex=sex,
#                 image=image,
#                 title=title,
#                 place=place,
#                 description=description,
#                 phone=phone,
#                 mail=mail,
#             )# створюємо новий екземпляр класу Post, присвоюємо поля
#             element.save()  # зберігаємо методом сейв
#             return render(request, 'thx.html)
#         else:
#             print('Спробуйте ще')
#             return render(request, 'register.html')