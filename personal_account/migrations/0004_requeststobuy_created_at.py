# Generated by Django 5.0.1 on 2024-02-24 18:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0003_requeststobuy'),
    ]

    operations = [
        migrations.AddField(
            model_name='requeststobuy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]