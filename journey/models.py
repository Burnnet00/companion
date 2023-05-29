from django.db import models
from django.core.validators import validate_integer, validate_email

GENDER_CHOICES = (
    ('M', 'Чоловік'),
    ('F', 'Жінка'),
)

COUNTRY_CHOICES = (
    ('UA', 'Україна'),
    ('AU', 'Австралія'),
    ('AT', 'Австрія'),
    ('BE', 'Бельгія'),
    ('BG', 'Болгарія'),
    ('BR', 'Бразилія'),
    ('HU', 'Угорщина'),
    ('DE', 'Німеччина'),
    ('GR', 'Греція'),
    ('DK', 'Данія'),
    ('EG', 'Єгипет'),
    ('IL', 'Ізраїль'),
    ('IN', 'Індія'),
    ('IE', 'Ірландія'),
    ('IS', 'Ісландія'),
    ('ES', 'Іспанія'),
    ('IT', 'Італія'),
    ('CY', 'Кіпр'),
    ('CN', 'Китай'),
    # ('KR', 'Південна Корея'),
    ('CO', 'Колумбія'),
    ('LV', 'Латвія'),
    ('LT', 'Литва'),
    ('LU', 'Люксембург'),
    ('MK', 'Північна Македонія'),
    ('MY', 'Малайзія'),
    ('MT', 'Мальта'),
    ('MX', 'Мексика'),
    ('MA', 'Марокко'),
    ('NZ', 'Нова Зеландія'),
    ('NO', 'Норвегія'),
    ('PL', 'Польща'),
    ('PT', 'Португалія'),
    ('RO', 'Румунія'),
    # ('RU', 'Росія'),
    ('SG', 'Сінгапур'),
    ('SK', 'Словаччина'),
    ('SI', 'Словенія'),
    ('US', 'Сполучені Штати Америки'),
    ('TH', 'Таїланд'),
    ('TN', 'Туніс'),
    ('TR', 'Туреччина'),
    ('UY', 'Уругвай'),
    ('PH', 'Філіппіни'),
    ('FI', 'Фінляндія'),
    ('FR', 'Франція'),
    ('HR', 'Хорватія'),
    ('CZ', 'Чехія'),
    ('CL', 'Чилі'),
    ('CH', 'Швейцарія'),
    ('SE', 'Швеція'),
    ('EC', 'Еквадор'),
    ('ZA', 'ПАР'),
    ('JP', 'Японія'),
    ('PY', 'Парагвай'),
    ('PE', 'Перу'),
    # ('--', 'Свій варіант'),

)


class Post(models.Model):
    """Post"""
    autor = models.CharField('Автор: ', max_length=50)
    age = models.CharField('Вік: ', max_length=2)
    sex = models.CharField('Стать:', max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField('Світлина: ', upload_to='image/%Y', blank=True, null=True)
    title = models.CharField('Заголовок: ', max_length=150)
    place = models.CharField('Місце подорожі: ', max_length=150, choices=COUNTRY_CHOICES, blank=True, null=True)
    description = models.TextField('Опис: ', max_length=2000)
    phone = models.CharField('Тел: ', max_length=20, validators=[validate_integer])
    mail = models.EmailField('Емайл:', max_length=20, validators=[validate_email])
    date = models.DateTimeField('Дата публікації:', auto_now_add=True)

    def __str__(self):
        return f'{self.autor}, {self.title}'

    class Meta:
        verbose_name = 'Запиc'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    """Commentars"""
    email = models.EmailField()
    name = models.CharField('Автор:',max_length=50)
    text_comments = models.TextField('Текст коменту:', max_length=500)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'









