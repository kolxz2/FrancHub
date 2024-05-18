# Generated by Django 5.0.1 on 2024-05-18 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('internet_and_communication_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('utility_payment', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'regions_statistic',
            },
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('franchise_id', models.AutoField(primary_key=True, serialize=False)),
                ('advantages_over_competitors', models.TextField()),
                ('business_launch_deadline', models.SmallIntegerField()),
                ('company_description', models.TextField()),
                ('costs_at_the_franchise_launch_stage', models.TextField()),
                ('date_of_trademark_registration', models.TextField()),
                ('example_of_profit_calculation', models.TextField()),
                ('franchise_start_year', models.SmallIntegerField()),
                ('inn_link', models.TextField()),
                ('investments_from_and_to', models.TextField()),
                ('juicy_description_of_the_franchise', models.TextField()),
                ('juridical_information', models.TextField()),
                ('link_to_the_franchise_website', models.TextField()),
                ('most_important_choosing_factors', models.TextField()),
                ('number_of_franchise_points', models.SmallIntegerField()),
                ('number_of_own_points', models.SmallIntegerField()),
                ('payback_period', models.SmallIntegerField()),
                ('registered_trademark_number', models.IntegerField()),
                ('required_number_of_employees', models.SmallIntegerField()),
                ('royalties_monthly_deductions', models.TextField()),
                ('short_description', models.TextField()),
                ('title', models.TextField()),
                ('training_and_support', models.TextField()),
                ('what_is_included_in_the_lump_sum', models.TextField()),
                ('year_of_company_opening', models.SmallIntegerField()),
                ('preview_photo', models.ImageField(blank=True, null=True, upload_to='preview_photo/')),
                ('allow_to_publish', models.CharField(blank=True, choices=[('need_a_check', 'Нужна проверка'), ('published', 'Опубликована'), ('filled_in_incorrectly', 'Заполнена неверно')], max_length=100, null=True, verbose_name='Статус заявки')),
                ('sait_manager_comment', models.TextField(blank=True, null=True)),
                ('average_check', models.IntegerField()),
                ('royalties_monthly_coast', models.IntegerField()),
                ('start_investments', models.IntegerField()),
                ('lump_sum_payment', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_account.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'franchises',
            },
        ),
        migrations.CreateModel(
            name='FranchisePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_photos', models.ImageField(upload_to='franchise_photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='franchise_photos', to='personal_account.franchise')),
            ],
        ),
        migrations.CreateModel(
            name='LocationMap',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('adygea', models.IntegerField(default=0)),
                ('altai', models.IntegerField(default=0)),
                ('altai_republic', models.IntegerField(default=0)),
                ('amur', models.IntegerField(default=0)),
                ('arkhangelsk', models.IntegerField(default=0)),
                ('astrakhan', models.IntegerField(default=0)),
                ('bashkortostan', models.IntegerField(default=0)),
                ('belgorod', models.IntegerField(default=0)),
                ('bryansk', models.IntegerField(default=0)),
                ('buryatia', models.IntegerField(default=0)),
                ('chechnya', models.IntegerField(default=0)),
                ('chelyabinsk', models.IntegerField(default=0)),
                ('chukotka', models.IntegerField(default=0)),
                ('chuvashia', models.IntegerField(default=0)),
                ('crimea', models.IntegerField(default=0)),
                ('dagestan', models.IntegerField(default=0)),
                ('donetsk', models.IntegerField(default=0)),
                ('ingushetia', models.IntegerField(default=0)),
                ('irkutsk', models.IntegerField(default=0)),
                ('ivanovo', models.IntegerField(default=0)),
                ('jewish_autonomous_oblast', models.IntegerField(default=0)),
                ('kabardino_balkaria', models.IntegerField(default=0)),
                ('kaliningrad', models.IntegerField(default=0)),
                ('kalmykia', models.IntegerField(default=0)),
                ('kaluga', models.IntegerField(default=0)),
                ('kamchatka', models.IntegerField(default=0)),
                ('karachay_cherkessia', models.IntegerField(default=0)),
                ('karelia', models.IntegerField(default=0)),
                ('kemerovo', models.IntegerField(default=0)),
                ('khabarovsk', models.IntegerField(default=0)),
                ('khakassia', models.IntegerField(default=0)),
                ('khanty_mansi', models.IntegerField(default=0)),
                ('kherson', models.IntegerField(default=0)),
                ('kirov', models.IntegerField(default=0)),
                ('komi', models.IntegerField(default=0)),
                ('kostroma', models.IntegerField(default=0)),
                ('krasnodar', models.IntegerField(default=0)),
                ('krasnoyarsk', models.IntegerField(default=0)),
                ('kurgan', models.IntegerField(default=0)),
                ('kursk', models.IntegerField(default=0)),
                ('leningrad', models.IntegerField(default=0)),
                ('lipetsk', models.IntegerField(default=0)),
                ('lugansk', models.IntegerField(default=0)),
                ('magadan', models.IntegerField(default=0)),
                ('mari_el', models.IntegerField(default=0)),
                ('mordovia', models.IntegerField(default=0)),
                ('moscow', models.IntegerField(default=0)),
                ('moscow_oblast', models.IntegerField(default=0)),
                ('murmansk', models.IntegerField(default=0)),
                ('nenets', models.IntegerField(default=0)),
                ('nizhny_novgorod', models.IntegerField(default=0)),
                ('north_ossetia_alania', models.IntegerField(default=0)),
                ('novgorod', models.IntegerField(default=0)),
                ('novosibirsk', models.IntegerField(default=0)),
                ('omsk', models.IntegerField(default=0)),
                ('orel', models.IntegerField(default=0)),
                ('orenburg', models.IntegerField(default=0)),
                ('penza', models.IntegerField(default=0)),
                ('perm', models.IntegerField(default=0)),
                ('primorsky', models.IntegerField(default=0)),
                ('pskov', models.IntegerField(default=0)),
                ('rostov', models.IntegerField(default=0)),
                ('ryazan', models.IntegerField(default=0)),
                ('sakha_yakutia', models.IntegerField(default=0)),
                ('sakhalin', models.IntegerField(default=0)),
                ('samara', models.IntegerField(default=0)),
                ('saratov', models.IntegerField(default=0)),
                ('sevastopol_city', models.IntegerField(default=0)),
                ('smolensk', models.IntegerField(default=0)),
                ('st_petersburg', models.IntegerField(default=0)),
                ('stavropol', models.IntegerField(default=0)),
                ('sverdlovsk', models.IntegerField(default=0)),
                ('tambov', models.IntegerField(default=0)),
                ('tatarstan', models.IntegerField(default=0)),
                ('tomsk', models.IntegerField(default=0)),
                ('tula', models.IntegerField(default=0)),
                ('tuva', models.IntegerField(default=0)),
                ('tver', models.IntegerField(default=0)),
                ('tyumen', models.IntegerField(default=0)),
                ('udmurtia', models.IntegerField(default=0)),
                ('ulyanovsk', models.IntegerField(default=0)),
                ('vladimir', models.IntegerField(default=0)),
                ('volgograd', models.IntegerField(default=0)),
                ('vologda', models.IntegerField(default=0)),
                ('voronezh', models.IntegerField(default=0)),
                ('yamalo_nenets', models.IntegerField(default=0)),
                ('yaroslavl', models.IntegerField(default=0)),
                ('zabaykalsky', models.IntegerField(default=0)),
                ('zaporozhye', models.IntegerField(default=0)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_account.franchise')),
            ],
            options={
                'db_table': 'location_map',
            },
        ),
        migrations.CreateModel(
            name='RequestsToBuy',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('under_consideration', 'На рассмотрении'), ('cansel', 'Отменена'), ('could_not_be_contacted', 'Франчайзер не смог связаться'), ('the_deal_is_done', 'Сделка заключена')], max_length=100, null=True, verbose_name='Статус заявки')),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_account.franchise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'requests_to_buy',
            },
        ),
    ]
