from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CurrentUserForm, AddFranchiseForm, FranchiseEditForm
from .models import Franchise, FranchisePhoto, RequestsToBuy, LocationMap

all_regions = [
    {'value': '-', 'text': 'Выберите регион размещения'},
    {'value': 'adygea', 'text': 'Адыгея'},
    {'value': 'altai', 'text': 'Алтайский край'},
    {'value': 'altai_republic', 'text': 'Республика Алтай'},
    {'value': 'amur', 'text': 'Амурская область'},
    {'value': 'arkhangelsk', 'text': 'Архангельская область'},
    {'value': 'astrakhan', 'text': 'Астраханская область'},
    {'value': 'bashkortostan', 'text': 'Республика Башкортостан'},
    {'value': 'belgorod', 'text': 'Белгородская область'},
    {'value': 'bryansk', 'text': 'Брянская область'},
    {'value': 'buryatia', 'text': 'Республика Бурятия'},
    {'value': 'chechnya', 'text': 'Чеченская Республика'},
    {'value': 'chelyabinsk', 'text': 'Челябинская область'},
    {'value': 'chukotka', 'text': 'Чукотский автономный округ'},
    {'value': 'chuvashia', 'text': 'Чувашская Республика'},
    {'value': 'crimea', 'text': 'Республика Крым'},
    {'value': 'dagestan', 'text': 'Республика Дагестан'},
    {'value': 'donetsk', 'text': 'Донецкая область'},
    {'value': 'ingushetia', 'text': 'Республика Ингушетия'},
    {'value': 'irkutsk', 'text': 'Иркутская область'},
    {'value': 'ivanovo', 'text': 'Ивановская область'},
    {'value': 'jewish_autonomous_oblast', 'text': 'Еврейская автономная область'},
    {'value': 'kabardino_balkaria', 'text': 'Кабардино-Балкарская Республика'},
    {'value': 'kaliningrad', 'text': 'Калининградская область'},
    {'value': 'kalmykia', 'text': 'Республика Калмыкия'},
    {'value': 'kaluga', 'text': 'Калужская область'},
    {'value': 'kamchatka', 'text': 'Камчатский край'},
    {'value': 'karachay_cherkessia', 'text': 'Карачаево-Черкесская Республика'},
    {'value': 'karelia', 'text': 'Республика Карелия'},
    {'value': 'kemerovo', 'text': 'Кемеровская область'},
    {'value': 'khabarovsk', 'text': 'Хабаровский край'},
    {'value': 'khakassia', 'text': 'Республика Хакасия'},
    {'value': 'khanty_mansi', 'text': 'Ханты-Мансийский автономный округ'},
    {'value': 'kherson', 'text': 'Херсонская область'},
    {'value': 'kirov', 'text': 'Кировская область'},
    {'value': 'komi', 'text': 'Республика Коми'},
    {'value': 'kostroma', 'text': 'Костромская область'},
    {'value': 'krasnodar', 'text': 'Краснодарский край'},
    {'value': 'krasnoyarsk', 'text': 'Красноярский край'},
    {'value': 'kurgan', 'text': 'Курганская область'},
    {'value': 'kursk', 'text': 'Курская область'},
    {'value': 'leningrad', 'text': 'Ленинградская область'},
    {'value': 'lipetsk', 'text': 'Липецкая область'},
    {'value': 'lugansk', 'text': 'Луганская область'},
    {'value': 'magadan', 'text': 'Магаданская область'},
    {'value': 'mari_el', 'text': 'Республика Марий Эл'},
    {'value': 'mordovia', 'text': 'Республика Мордовия'},
    {'value': 'moscow', 'text': 'Москва'},
    {'value': 'moscow_oblast', 'text': 'Московская область'},
    {'value': 'murmansk', 'text': 'Мурманская область'},
    {'value': 'nenets', 'text': 'Ненецкий автономный округ'},
    {'value': 'nizhny_novgorod', 'text': 'Нижегородская область'},
    {'value': 'north_ossetia_alania', 'text': 'Республика Северная Осетия — Алания'},
    {'value': 'novgorod', 'text': 'Новгородская область'},
    {'value': 'novosibirsk', 'text': 'Новосибирская область'},
    {'value': 'omsk', 'text': 'Омская область'},
    {'value': 'orel', 'text': 'Орловская область'},
    {'value': 'orenburg', 'text': 'Оренбургская область'},
    {'value': 'penza', 'text': 'Пензенская область'},
    {'value': 'perm', 'text': 'Пермский край'},
    {'value': 'primorsky', 'text': 'Приморский край'},
    {'value': 'pskov', 'text': 'Псковская область'},
    {'value': 'rostov', 'text': 'Ростовская область'},
    {'value': 'ryazan', 'text': 'Рязанская область'},
    {'value': 'sakha_yakutia', 'text': 'Республика Саха (Якутия)'},
    {'value': 'sakhalin', 'text': 'Сахалинская область'},
    {'value': 'samara', 'text': 'Самарская область'},
    {'value': 'saratov', 'text': 'Саратовская область'},
    {'value': 'sevastopol_city', 'text': 'Севастополь'},
    {'value': 'smolensk', 'text': 'Смоленская область'},
    {'value': 'st_petersburg', 'text': 'Санкт-Петербург'},
    {'value': 'stavropol', 'text': 'Ставропольский край'},
    {'value': 'sverdlovsk', 'text': 'Свердловская область'},
    {'value': 'tambov', 'text': 'Тамбовская область'},
    {'value': 'tatarstan', 'text': 'Республика Татарстан'},
    {'value': 'tomsk', 'text': 'Томская область'},
    {'value': 'tula', 'text': 'Тульская область'},
    {'value': 'tuva', 'text': 'Республика Тыва'},
    {'value': 'tver', 'text': 'Тверская область'},
    {'value': 'tyumen', 'text': 'Тюменская область'},
    {'value': 'udmurtia', 'text': 'Удмуртская Республика'},
    {'value': 'ulyanovsk', 'text': 'Ульяновская область'},
    {'value': 'vladimir', 'text': 'Владимирская область'},
    {'value': 'volgograd', 'text': 'Волгоградская область'},
    {'value': 'vologda', 'text': 'Вологодская область'},
    {'value': 'voronezh', 'text': 'Воронежская область'},
    {'value': 'yamalo_nenets', 'text': 'Ямало-Ненецкий автономный округ'},
    {'value': 'yaroslavl', 'text': 'Ярославская область'},
    {'value': 'zabaykalsky', 'text': 'Забайкальский край'},
    {'value': 'zaporozhye', 'text': 'Запорожская область'},
]


def my_view(request):
    current_user_form = CurrentUserForm(request=request)
    return render(request, 'greeting_form.html', {'current_user_form': current_user_form})


@login_required
def create_franchise(request):
    if request.user.user_type != 'owner':
        return redirect('login')
    if request.method == 'POST':
        form = AddFranchiseForm(request.POST, request.FILES, request=request)
        franchise_photos = request.FILES.getlist('images')
        if form.is_valid() and len(franchise_photos) > 0:
            franchise = form.save()
            # Сохранение локаций размещения
            regions = []
            values = []
            # Извлекаем данные из POST запроса
            for key in request.POST:
                if key.startswith('region_'):
                    index = key.split('_')[1]
                    regions.append(request.POST[key])
                    values.append(request.POST[f'value_{index}'])
            for region, value in zip(regions, values):
                location_map, created = LocationMap.objects.get_or_create(
                    franchise=franchise,
                    defaults={region: int(value)}
                )
                if not created:
                    setattr(location_map, region, int(value))
                    location_map.save()
            # сохранение фотографий
            for photo in franchise_photos:
                FranchisePhoto.objects.create(franchise=franchise, franchise_photos=photo)
            return redirect('user_franchises')
    else:
        form = AddFranchiseForm()
        initial_data = []
    return render(request, 'create_franchise.html',
                  {'form': form, "all_regions": all_regions, 'initial_data': initial_data})


@login_required
def edit_franchise(request, franchise_id):
    franchise = get_object_or_404(Franchise, pk=franchise_id)
    if franchise.user_id != request.user.id:
        return redirect('unauthorized_access')
    if request.method == 'POST':
        if 'delete_franchise' in request.POST:
            franchise.delete()
            return redirect('user_franchises')
        form = AddFranchiseForm(request.POST, request.FILES, instance=franchise)
        franchise_photos = request.FILES.getlist('images')
        if form.is_valid():
            FranchisePhoto.objects.filter(franchise=franchise).delete()
            form.save()
            for photo in franchise_photos:
                FranchisePhoto.objects.create(franchise=franchise, franchise_photos=photo)
            return redirect('user_franchises')
    else:
        form = FranchiseEditForm(instance=franchise)
        location_maps = LocationMap.objects.filter(franchise=franchise.franchise_id)
        initial_data = []
        for location in location_maps:
            for field in location._meta.fields:
                if field.name not in ['id', 'franchise'] and getattr(location,
                                                                     field.name) > 0 and field.name != 'map_id':
                    initial_data.append({'region': field.name, 'value': getattr(location, field.name)})
    return render(request, 'create_franchise.html',
                  {'franchise': franchise, 'form': form, "all_regions": all_regions, 'initial_data': initial_data})


def location_map_view(request):
    if request.method == 'POST':
        regions = []
        values = []

        # Извлекаем данные из POST запроса
        for key in request.POST:
            if key.startswith('region_'):
                index = key.split('_')[1]
                regions.append(request.POST[key])
                values.append(request.POST[f'value_{index}'])
        franchise = Franchise.objects.get(pk=9)

        for region, value in zip(regions, values):
            location_map, created = LocationMap.objects.get_or_create(
                franchise=franchise,
                defaults={region: int(value)}
            )
            if not created:
                setattr(location_map, region, int(value))
                location_map.save()
    else:
        location_maps = LocationMap.objects.filter(franchise=5)
        initial_data = []
        for location in location_maps:
            for field in location._meta.fields:
                if field.name not in ['id', 'franchise'] and getattr(location, field.name) > 0:
                    initial_data.append({'region': field.name, 'value': getattr(location, field.name)})

    return render(request, 'location_map_form.html', {
        'all_regions': all_regions,
        'initial_data': initial_data,
    })


@login_required
def user_franchises(request):
    franchises = Franchise.objects.filter(user_id=request.user.id)
    return render(request, 'user_franchises.html', {'franchises': franchises})


@login_required
def user_buy_franchise_requests(request):
    list_visibility = False
    if request.method == 'POST':
        list_visibility = True
        status_value = request.POST.get('status')
        status, request_id = status_value.split('/')
        # Получаем объект RequestsToBuy по его id
        request_to_buy = get_object_or_404(RequestsToBuy, id=request_id)
        # Изменяем статус заявки на новое значение
        request_to_buy.status = status
        request_to_buy.save()
        # Перенаправляем пользователя на ту же страницу или на другую страницу, где вы хотите отобразить обновленные данные
        return redirect('user_buy_franchise_requests')

    user_franchises = Franchise.objects.filter(user_id=request.user.id)
    requests_to_buy = []
    for franchise in user_franchises:
        franchise_requests = RequestsToBuy.objects.filter(franchise=franchise)
        for franchise_request in franchise_requests:
            request_info = {
                'request': franchise_request,
                'franchise': franchise_request.franchise,
                'user': franchise_request.user,
                'created_at': franchise_request.created_at,
                'status': franchise_request.status
            }
            requests_to_buy.append(request_info)
    if requests_to_buy:
        list_visibility = True

    return render(request, 'user_buy_franchise_requests.html',
                  {'requests_to_buy': requests_to_buy, 'list_visibility': list_visibility})


@login_required
def user_requests_to_by(request):
    list_visibility = False
    if request.method == 'POST':
        list_visibility = True
        request_id = request.POST.get('request_id')
        request_to_buy = get_object_or_404(RequestsToBuy, id=request_id)
        # Изменяем статус заявки на новое значение
        # request_to_buy.status = "cansel"
        request_to_buy.delete()
        # Перенаправляем пользователя на ту же страницу или на другую страницу, где вы хотите отобразить обновленные данные
        # return redirect('user_buy_franchise_requests')

    user_franchises = RequestsToBuy.objects.filter(user=request.user.id)
    if user_franchises:
        list_visibility = True
    return render(request, 'user_requests_to_by.html',
                  {'requests_to_buy': user_franchises, 'list_visibility': list_visibility})





@login_required
def delete_franchise(request, franchise_id):
    franchise = get_object_or_404(Franchise, pk=franchise_id)
    if franchise.user_id != request.user.id:
        return redirect('unauthorized_access')
    if request.method == 'POST':
        franchise.delete()
        return redirect('user_franchises')
    else:
        return HttpResponseRedirect(reverse('user_franchises'))
