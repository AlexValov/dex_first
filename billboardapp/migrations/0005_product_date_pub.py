# Generated by Django 2.2.5 on 2019-09-22 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billboardapp', '0004_auto_20190922_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]