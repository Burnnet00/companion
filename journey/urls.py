from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PostView.as_view()),#, name='main'),
    path('<int:pk>', views.PostViewDetail.as_view()),#, name='detail'),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comments'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
