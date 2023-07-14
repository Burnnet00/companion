from django.contrib import admin
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'age', 'sex', 'image', 'title',
                    'place', 'description', 'phone', 'mail', 'date',)
    list_display_links = ('id','autor', 'title')
    search_fields = ('sex', 'place',)
    list_filter = ('sex', 'place',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','email','name','text_comments')


