from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='img', null=False, blank=True)
    price = models.IntegerField(verbose_name='Цена')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


