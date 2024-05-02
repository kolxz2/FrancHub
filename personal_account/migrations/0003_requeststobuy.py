# Generated by Django 5.0.1 on 2024-02-24 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0002_remove_franchise_city_head_office_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestsToBuy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_account.franchise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'requests_to_buy',
            },
        ),
    ]