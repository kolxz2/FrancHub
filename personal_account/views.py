from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CurrentUserForm, AddFranchiseForm, FranchiseEditForm
from .models import Franchise, FranchisePhoto, RequestsToBuy


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
            for photo in franchise_photos:
                FranchisePhoto.objects.create(franchise=franchise, franchise_photos=photo)
            return redirect('user_franchises')
    else:
        form = AddFranchiseForm()
    return render(request, 'create_franchise.html', {'form': form})


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

    return render(request, 'user_buy_franchise_requests.html', {'requests_to_buy': requests_to_buy, 'list_visibility': list_visibility})


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
    return render(request, 'user_requests_to_by.html', {'requests_to_buy': user_franchises, 'list_visibility': list_visibility})



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
    return render(request, 'create_franchise.html', {'franchise': franchise, 'form': form})


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