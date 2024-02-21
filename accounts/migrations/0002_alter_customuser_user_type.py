# Generated by Django 5.0.1 on 2024-02-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('owner', 'Франчайзер'), ('franchise', 'Франчизи')], max_length=10, null=True, verbose_name='Тип пользователя'),
        ),
    ]
