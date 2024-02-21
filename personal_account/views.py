from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CurrentUserForm, AddFranchiseForm, FranchiseEditForm, FranchisePhotoForm
from .models import Franchise, FranchisePhoto


def my_view(request):
    current_user_form = CurrentUserForm(request=request)
    return render(request, 'my_template.html', {'current_user_form': current_user_form})


@login_required
def create_franchise(request):
    if request.user.user_type != 'owner':
        return redirect('login')

    if request.method == 'POST':
        form = AddFranchiseForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('user_franchises')

    else:
        form = AddFranchiseForm()

    return render(request, 'create_franchise.html',{'form': form} )


@login_required
def user_franchises(request):
    franchises = Franchise.objects.filter(user_id=request.user.id)
    return render(request, 'user_franchises.html', {'franchises': franchises})


@login_required
def edit_franchise(request, franchise_id):
    franchise = get_object_or_404(Franchise, pk=franchise_id)
    if franchise.user_id != request.user.id:
        return redirect('unauthorized_access')
    if request.method == 'POST':
        form = FranchiseEditForm(request.POST, instance=franchise)
        if form.is_valid():
            form.save()
            return redirect('franchise_list')
    else:
        form = FranchiseEditForm(instance=franchise)
    return render(request, 'edit_franchise.html', {'form': form})


# def upload_photos2(request):
#     if request.method == 'POST':
#         form = FranchisePhotoForm(request.POST, request.FILES)
#         if form.is_valid():
#             franchise_id = 2  # Assuming you have some way to determine franchise_id
#             for photo in request.FILES.getlist('file'):  # Change 'photo' to 'file' to match Dropzone paramName
#                 try:
#                     FranchisePhoto.objects.create(franchise_id=franchise_id, franchise_photos=photo)
#                 except Exception as e:
#                     print(f"Error occurred while saving photo: {e}")
#             return redirect('franchise_detail', franchise_id=franchise_id)
#         else:
#             print(f"Form is not valid: {form.errors}")
#     else:
#         form = FranchisePhotoForm()
#     return render(request, 'upload_franchise_photos.html', {'form': form})

#
# def upload_photos(request):
#     if request.method == 'POST':
#
#         images = request.FILES.getlist('images')
#
#         franchise_id = 2  # Получите franchise_id из вашего контекста или запроса
#         for photo in request.FILES.getlist('images'):
#             FranchisePhoto.objects.create(franchise_id=franchise_id, franchise_photos=photo)
#         return redirect('franchise_detail', franchise_id=franchise_id)
#
#     return render(request, 'upload_franchise_photos.html')
#
#
# def upload_images(request):
#     if request.method == 'POST' and request.FILES.getlist('images'):
#         images = request.FILES.getlist('images')
#         # Обработка каждого изображения
#         for photo in request.FILES.getlist('images'):
#             FranchisePhoto.objects.create(franchise_id=2, franchise_photos=photo)
#
#         return HttpResponse('Images uploaded successfully!')
#     return render(request, 'photo_up.html')
