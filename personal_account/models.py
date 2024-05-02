import os

from django.db import models

from accounts.models import CustomUser


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'


class Franchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    advantages_over_competitors = models.TextField()
    business_launch_deadline = models.SmallIntegerField()
    # city_head_office = models.TextField()
    company_description = models.TextField()
    costs_at_the_franchise_launch_stage = models.TextField()
    date_of_trademark_registration = models.TextField()
    # desired_placement_sections = models.TextField()
    example_of_profit_calculation = models.TextField()
    franchise_start_year = models.SmallIntegerField()
    # geography_of_development = models.TextField()
    # in_which_cities_shouldiopenafranchise = models.TextField()
    inn_link = models.TextField()
    investments_from_and_to = models.TextField()
    juicy_description_of_the_franchise = models.TextField()
    juridical_information = models.TextField()
    link_to_the_franchise_website = models.TextField()
    lump_sum_payment = models.IntegerField()
    monthly_profit = models.TextField()
    most_important_choosing_factors = models.TextField()
    number_of_franchise_points = models.SmallIntegerField()
    number_of_own_points = models.SmallIntegerField()
    payback_period = models.SmallIntegerField()
    registered_trademark_number = models.IntegerField()
    required_number_of_employees = models.SmallIntegerField()
    # room_requirements = models.TextField()
    royalties_monthly_deductions = models.TextField()
    short_description = models.TextField()
    title = models.TextField()
    training_and_support = models.TextField()
    what_is_included_in_the_lump_sum = models.TextField()
    # what_is_your_main_product = models.TextField()
    year_of_company_opening = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    preview_photo = models.ImageField(upload_to="preview_photo/", null=True, blank=True)
    allow_to_publish = models.BooleanField()
    # todo добавить в регистрацию франшизы поле
    start_investments = models.IntegerField()

    def delete(self, *args, **kwargs):
        # Удаление файла изображения перед удалением экземпляра модели
        if self.preview_photo:
            if os.path.isfile(self.preview_photo.path):
                os.remove(self.preview_photo.path)
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'franchises'


class FranchisePhoto(models.Model):
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, related_name='franchise_photos')
    franchise_photos = models.ImageField(upload_to='franchise_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Удаление файла изображения перед удалением экземпляра модели
        if self.franchise_photos:
            if os.path.isfile(self.franchise_photos.path):
                os.remove(self.franchise_photos.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Photo for {self.franchise.title}'


class LocationMap(models.Model):
    map_id = models.AutoField(primary_key=True)
    adygea = models.IntegerField()
    altai = models.IntegerField()
    altai_republic = models.IntegerField()
    amur = models.IntegerField()
    arkhangelsk = models.IntegerField()
    astrakhan = models.IntegerField()
    bashkortostan = models.IntegerField()
    belgorod = models.IntegerField()
    bryansk = models.IntegerField()
    buryatia = models.IntegerField()
    chechnya = models.IntegerField()
    chelyabinsk = models.IntegerField()
    chukotka = models.IntegerField()
    chuvashia = models.IntegerField()
    crimea = models.IntegerField()
    dagestan = models.IntegerField()
    donetsk = models.IntegerField()
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    ingushetia = models.IntegerField()
    irkutsk = models.IntegerField()
    ivanovo = models.IntegerField()
    jewish_autonomous_oblast = models.IntegerField()
    kabardino_balkaria = models.IntegerField()
    kaliningrad = models.IntegerField()
    kalmykia = models.IntegerField()
    kaluga = models.IntegerField()
    kamchatka = models.IntegerField()
    karachay_cherkessia = models.IntegerField()
    karelia = models.IntegerField()
    kemerovo = models.IntegerField()
    khabarovsk = models.IntegerField()
    khakassia = models.IntegerField()
    khanty_mansi = models.IntegerField()
    kherson = models.IntegerField()
    kirov = models.IntegerField()
    komi = models.IntegerField()
    kostroma = models.IntegerField()
    krasnodar = models.IntegerField()
    krasnoyarsk = models.IntegerField()
    kurgan = models.IntegerField()
    kursk = models.IntegerField()
    leningrad = models.IntegerField()
    lipetsk = models.IntegerField()
    lugansk = models.IntegerField()
    magadan = models.IntegerField()
    mari_el = models.IntegerField()
    mordovia = models.IntegerField()
    moscow = models.IntegerField()
    moscow_oblast = models.IntegerField()
    murmansk = models.IntegerField()
    nenets = models.IntegerField()
    nizhny_novgorod = models.IntegerField()
    north_ossetia_alania = models.IntegerField()
    novgorod = models.IntegerField()
    novosibirsk = models.IntegerField()
    omsk = models.IntegerField()
    orel = models.IntegerField()
    orenburg = models.IntegerField()
    penza = models.IntegerField()
    perm = models.IntegerField()
    primorsky = models.IntegerField()
    pskov = models.IntegerField()
    rostov = models.IntegerField()
    ryazan = models.IntegerField()
    sakha_yakutia = models.IntegerField()
    sakhalin = models.IntegerField()
    samara = models.IntegerField()
    saratov = models.IntegerField()
    sevastopol_city = models.IntegerField()
    smolensk = models.IntegerField()
    st_petersburg = models.IntegerField()
    stavropol = models.IntegerField()
    sverdlovsk = models.IntegerField()
    tambov = models.IntegerField()
    tatarstan = models.IntegerField()
    tomsk = models.IntegerField()
    tula = models.IntegerField()
    tuva = models.IntegerField()
    tver = models.IntegerField()
    tyumen = models.IntegerField()
    udmurtia = models.IntegerField()
    ulyanovsk = models.IntegerField()
    vladimir = models.IntegerField()
    volgograd = models.IntegerField()
    vologda = models.IntegerField()
    voronezh = models.IntegerField()
    yamalo_nenets = models.IntegerField()
    yaroslavl = models.IntegerField()
    zabaykalsky = models.IntegerField()
    zaporozhye = models.IntegerField()

    class Meta:
        db_table = 'location_map'


class RequestsToBuy(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_TYPE_CHOICES = [
        ('under_consideration', 'На рассмотрении'),
        ('cansel', 'Отменена'),
        ('could_not_be_contacted', 'Франчайзер не смог связаться'),
        ('the_deal_is_done', 'Сделка заключена'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_TYPE_CHOICES, verbose_name="Статус заявки", null=True,
                              blank=True)

    class Meta:
        db_table = 'requests_to_buy'