from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from personal_account.forms import AddFranchiseForm
from personal_account.models import FranchisePhoto, Franchise


@login_required
def franchise_validation(request):
    if not request.user.is_staff:
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
def all_site_franchises(request):
    franchises = Franchise.objects.all()
    return render(request, 'user_franchises.html', {'franchises': franchises})
