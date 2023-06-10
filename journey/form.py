from django.forms import TextInput, ImageField, Textarea, EmailField
from .models import Post, Comments
from django import forms
from .models import GENDER_CHOICES, COUNTRY_CHOICES
from django.core.exceptions import ValidationError



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comments', 'name', 'email',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'age', 'sex', 'image', 'title',
                  'place', 'description', 'phone', 'mail',)

#     def clean_image(self):
#         image = self.cleaned_data.get('image', False)
#         if image:
#             if image.size > 4*1024*1024:
#                 raise ValidationError("Фаіл занадто великий. Максимальний розмір 4 МБ.")
#             return image
#         else:
#             raise ValidationError("Не вдалося завантажити зображення")



# class AddPostForm(forms.Form):
#     autor = forms.CharField(label='Імя', max_length=200,)# required=False, widget=forms.TextInput(attrs={'class': 'css_input'}))#добавимо необовязкове поле, виджет створеного цсс
#     age = forms.CharField(label='Вік', max_length=200)
#     sex = forms.CharField(label='Стать', max_length=200)
#     image = forms.CharField(label='Світлина', max_length=200, required=False)
#     title = forms.CharField(label='Заголовок', max_length=200,)
#     place = forms.CharField(label='Місце подорожі', max_length=200)
#     description = forms.CharField(label='Опис', max_length=20000)
#     phone = forms.CharField(label='Телефон', max_length=15)
#     mail = forms.CharField(label='Емайл', max_length=50)