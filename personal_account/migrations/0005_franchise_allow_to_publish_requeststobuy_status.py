# Generated by Django 5.0.1 on 2024-02-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0004_requeststobuy_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchise',
            name='allow_to_publish',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requeststobuy',
            name='status',
            field=models.CharField(blank=True, choices=[('owner', 'На рассмотрении'), ('franchise', 'Отменена'), ('franchise', 'Франчайзер не смог связаться'), ('franchise', 'Сделка заключена')], max_length=100, null=True, verbose_name='Статус заявки'),
        ),
    ]
