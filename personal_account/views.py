from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CurrentUserForm, AddFranchiseForm, FranchiseEditForm
from .models import Franchise, FranchisePhoto, RequestsToBuy, LocationMap

all_regions = [
    {'value': '-', 'text': 'Выберите регион размещения', 'geo': [34, 54]},
    {'value': 'adygea', 'text': 'Адыгея', 'geo': [40.105852, 44.606683]},
    {'value': 'altai', 'text': 'Алтайский край', 'geo': [83.776860, 53.346785]},
    {'value': 'altai_republic', 'text': 'Республика Алтай', 'geo': [40.105852, 44.606683]},
    {'value': 'amur', 'text': 'Амурская область', 'geo': [85.960631, 51.957805]},
    {'value': 'arkhangelsk', 'text': 'Архангельская область', 'geo': [40.515762, 64.539912]},
    {'value': 'astrakhan', 'text': 'Астраханская область', 'geo': [48.030175, 46.347616]},
    {'value': 'bashkortostan', 'text': 'Республика Башкортостан', 'geo': [55.958727, 54.735147]},
    {'value': 'belgorod', 'text': 'Белгородская область', 'geo': [36.587272, 50.595415]},
    {'value': 'bryansk', 'text': 'Брянская область', 'geo': [34.363991, 53.243400]},
    {'value': 'buryatia', 'text': 'Республика Бурятия', 'geo': [107.584545, 51.834811]},
    {'value': 'chechnya', 'text': 'Чеченская Республика', 'geo': [43.318368, 45.692419]},
    {'value': 'chelyabinsk', 'text': 'Челябинская область', 'geo': [61.402554, 55.159897]},
    {'value': 'chukotka', 'text': 'Чукотский автономный округ', 'geo': [177.518911, 64.735815]},
    {'value': 'chuvashia', 'text': 'Чувашская Республика', 'geo': [47.247731, 56.139920]},
    {'value': 'crimea', 'text': 'Республика Крым', 'geo': [34.100318, 44.948237]},
    {'value': 'dagestan', 'text': 'Республика Дагестан', 'geo': [47.504748, 42.983103]},
    {'value': 'donetsk', 'text': 'Донецкая область', 'geo': [37.802850, 48.015884]},
    {'value': 'ingushetia', 'text': 'Республика Ингушетия', 'geo': [44.803574, 43.166786]},
    {'value': 'irkutsk', 'text': 'Иркутская область', 'geo': [104.280608, 52.289590]},
    {'value': 'ivanovo', 'text': 'Ивановская область', 'geo': [40.973921, 57.000348]},
    {'value': 'jewish_autonomous_oblast', 'text': 'Еврейская автономная область', 'geo': [132.924750, 48.789917]},
    {'value': 'kabardino_balkaria', 'text': 'Кабардино-Балкарская Республика', 'geo': [43.607072, 43.485259]},
    {'value': 'kaliningrad', 'text': 'Калининградская область', 'geo': [20.510138, 54.710161]},
    {'value': 'kalmykia', 'text': 'Республика Калмыкия', 'geo': [44.269759, 46.307743]},
    {'value': 'kaluga', 'text': 'Калужская область', 'geo': [36.261341, 54.513678]},
    {'value': 'kamchatka', 'text': 'Камчатский край', 'geo': [158.643504, 53.024263]},
    {'value': 'karachay_cherkessia', 'text': 'Карачаево-Черкесская Республика', 'geo': [42.048277, 44.228376]},
    {'value': 'karelia', 'text': 'Республика Карелия', 'geo': [34.346881, 61.785020]},
    {'value': 'kemerovo', 'text': 'Кемеровская область', 'geo': [86.086848, 55.355200]},
    {'value': 'khabarovsk', 'text': 'Хабаровский край', 'geo': [135.071917, 48.480223]},
    {'value': 'khakassia', 'text': 'Республика Хакасия', 'geo': [91.442387, 53.721152]},
    {'value': 'khanty_mansi', 'text': 'Ханты-Мансийский автономный округ', 'geo': [69.018902, 61.003180]},
    {'value': 'kherson', 'text': 'Херсонская область', 'geo': [32.614962, 46.640319]},
    {'value': 'kirov', 'text': 'Кировская область', 'geo': [49.668019, 58.603595]},
    {'value': 'komi', 'text': 'Республика Коми', 'geo': [50.836500, 61.668796]},
    {'value': 'kostroma', 'text': 'Костромская область', 'geo': [40.926894, 57.767918]},
    {'value': 'krasnodar', 'text': 'Краснодарский край', 'geo': [38.975313, 45.035470]},
    {'value': 'krasnoyarsk', 'text': 'Красноярский край', 'geo': [92.852572, 56.010563]},
    {'value': 'kurgan', 'text': 'Курганская область', 'geo': [65.341122, 55.441005]},
    {'value': 'kursk', 'text': 'Курская область', 'geo': [36.193015, 51.730848]},
    {'value': 'leningrad', 'text': 'Ленинградская область', 'geo': [30.314997, 59.938784]},
    {'value': 'lipetsk', 'text': 'Липецкая область', 'geo': [39.599220, 52.608820]},
    {'value': 'lugansk', 'text': 'Луганская область', 'geo': [39.307708, 48.573896]},
    {'value': 'magadan', 'text': 'Магаданская область', 'geo': [150.808590, 59.565153]},
    {'value': 'mari_el', 'text': 'Республика Марий Эл', 'geo': [47.886180, 56.631600]},
    {'value': 'mordovia', 'text': 'Республика Мордовия', 'geo': [45.183939, 54.187433]},
    {'value': 'moscow', 'text': 'Москва', 'geo': [37.617698, 55.755864]},
    {'value': 'moscow_oblast', 'text': 'Московская область', 'geo': [35.938676, 54.326808]},
    {'value': 'murmansk', 'text': 'Мурманская область', 'geo': [33.074914, 68.970663]},
    {'value': 'nenets', 'text': 'Ненецкий автономный округ', 'geo': [53.006926, 67.638050]},
    {'value': 'nizhny_novgorod', 'text': 'Нижегородская область', 'geo': [56.326799, 44.006520]},
    {'value': 'north_ossetia_alania', 'text': 'Республика Северная Осетия — Алания', 'geo': [44.681768, 43.024617]},
    {'value': 'novgorod', 'text': 'Новгородская область', 'geo': [31.269813, 58.522856]},
    {'value': 'novosibirsk', 'text': 'Новосибирская область', 'geo': [55.030199, 82.920430]},
    {'value': 'omsk', 'text': 'Омская область', 'geo': [73.368212, 54.989342]},
    {'value': 'orel', 'text': 'Орловская область', 'geo': [52.970758, 36.064355]},
    {'value': 'orenburg', 'text': 'Оренбургская область', 'geo': [55.097000, 51.768205]},
    {'value': 'penza', 'text': 'Пензенская область', 'geo': [45.018318, 53.195042]},
    {'value': 'perm', 'text': 'Пермский край', 'geo': [56.229441, 58.010454]},
    {'value': 'primorsky', 'text': 'Приморский край', 'geo': [131.885485, 43.115536]},
    {'value': 'pskov', 'text': 'Псковская область', 'geo': [28.332458, 57.819276]},
    {'value': 'rostov', 'text': 'Ростовская область', 'geo': [39.720349, 47.222078]},
    {'value': 'ryazan', 'text': 'Рязанская область', 'geo': [39.741914, 54.629565]},
    {'value': 'sakha_yakutia', 'text': 'Республика Саха (Якутия)', 'geo': [129.732178, 62.027221]},
    {'value': 'sakhalin', 'text': 'Сахалинская область', 'geo': [142.729587, 46.957770]},
    {'value': 'samara', 'text': 'Самарская область', 'geo': [50.100199, 53.195876]},
    {'value': 'saratov', 'text': 'Саратовская область', 'geo': [46.034265, 51.533561]},
    {'value': 'sevastopol_city', 'text': 'Севастополь', 'geo': [33.524471, 44.616020]},
    {'value': 'smolensk', 'text': 'Смоленская область', 'geo': [32.045288, 54.782634]},
    {'value': 'st_petersburg', 'text': 'Санкт-Петербург', 'geo': [30.314997, 59.938784]},
    {'value': 'stavropol', 'text': 'Ставропольский край', 'geo': [41.969111, 45.043315]},
    {'value': 'sverdlovsk', 'text': 'Свердловская область', 'geo': [60.597465, 56.838011]},
    {'value': 'tambov', 'text': 'Тамбовская область', 'geo': [41.452749, 52.721293]},
    {'value': 'tatarstan', 'text': 'Республика Татарстан', 'geo': [49.106414, 55.796129]},
    {'value': 'tomsk', 'text': 'Томская область', 'geo': [84.947649, 56.484640]},
    {'value': 'tula', 'text': 'Тульская область', 'geo': [37.617348, 54.193122]},
    {'value': 'tuva', 'text': 'Республика Тыва', 'geo': [94.437986, 51.719891]},
    {'value': 'tver', 'text': 'Тверская область', 'geo': [35.911851, 56.859561]},
    {'value': 'tyumen', 'text': 'Тюменская область', 'geo': [65.541231, 57.152986]},
    {'value': 'udmurtia', 'text': 'Удмуртская Республика', 'geo': [53.206896, 56.852677]},
    {'value': 'ulyanovsk', 'text': 'Ульяновская область', 'geo': [48.403131, 54.314194]},
    {'value': 'vladimir', 'text': 'Владимирская область', 'geo': [40.406635, 56.129057]},
    {'value': 'volgograd', 'text': 'Волгоградская область', 'geo': [44.516979, 48.707068]},
    {'value': 'vologda', 'text': 'Вологодская область', 'geo': [39.891523, 59.220496]},
    {'value': 'voronezh', 'text': 'Воронежская область', 'geo': [39.200292, 51.660779]},
    {'value': 'yamalo_nenets', 'text': 'Ямало-Ненецкий автономный округ', 'geo': [66.614507, 66.529865]},
    {'value': 'yaroslavl', 'text': 'Ярославская область', 'geo': [39.893813, 57.626560]},
    {'value': 'zabaykalsky', 'text': 'Забайкальский край', 'geo': [113.501052, 52.033638]},
    {'value': 'zaporozhye', 'text': 'Запорожская область', 'geo': [35.138851, 47.838312]},
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
