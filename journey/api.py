from .models import Post
from .serializers import PostSerializers
from rest_framework import viewsets, permissions

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializers