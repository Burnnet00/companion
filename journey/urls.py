from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PostView.as_view(), name='main'),
    path('<int:pk>', views.PostViewDetail.as_view()),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comments'),
    path('addpost/', views.add_post, name='addpost'),
    path('about/', views.about, name='about'),
]
