from django.forms import TextInput, ImageField, Textarea, EmailField, NumberInput, ClearableFileInput
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

        widgets = {'autor': TextInput(attrs={"class": "form-control", "placeholder": "Введіть ім`я"}),
                   'age': TextInput(attrs={"class": "form-control", "placeholder": "Введіть ваш вік"}),
                   # 'sex': TextInput(attrs={"class": "form-control", "placeholder": "Введіть стать"}),
                   'image': ClearableFileInput(attrs={"class": "form-control", "placeholder": "Світлина"}),
                   'title': TextInput(attrs={"class": "form-control", "placeholder": "Введіть заголовок"}),
                   # 'place': TextInput(attrs={"class": "form-control", "placeholder": "Введіть місце зустрічі"}),
                   'description': Textarea(attrs={"class": "form-control", "placeholder": "Введіть деталі подорожі"}),
                   'phone': NumberInput(attrs={"class": "form-control", "placeholder": "Введіть свій телефон"}),
                   'mail': TextInput(attrs={"class": "form-control", "placeholder": " Введіть свій емаіл"}),
                   }

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 4*1024*1024:
                raise ValidationError("Файл занадто великий. Максимальний розмір 4 МБ.")
            return image
        else:
            raise ValidationError("Не вдалося завантажити зображення")
