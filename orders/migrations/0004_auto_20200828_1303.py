# Generated by Django 3.1 on 2020-08-28 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200809_0159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
