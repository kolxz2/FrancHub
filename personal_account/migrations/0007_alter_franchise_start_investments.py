# Generated by Django 5.0.1 on 2024-02-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0006_franchise_start_investments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchise',
            name='start_investments',
            field=models.IntegerField(),
        ),
    ]