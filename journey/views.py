from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments
from .form import PostForm, CommentsForm
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializers

class PostView(View):
    def get(self, request):
        sort = request.GET.get('sort')
        if sort:
            if sort == 'date':
                posts = Post.objects.order_by('-date')
            elif sort == 'sex-M':
                posts = Post.objects.filter(sex='M').order_by('-date')

            else:
                posts = Post.objects.filter(sex='F').order_by('-date')

        else:
            posts = Post.objects.order_by('-date')

        return render(request, 'journey/index.html', {'posts': posts})

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

def add_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('main')
        else:
            error = 'Невірна форма'

    form = PostForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'journey/addpost.html', data)

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

def about(request):
    return render(request, 'journey/about.html')