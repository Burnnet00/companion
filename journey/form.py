from .models import Post, Comments
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'age', 'sex', 'image', 'title',
                  'place', 'description', 'phone', 'mail',)
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comments', 'name', 'email',)