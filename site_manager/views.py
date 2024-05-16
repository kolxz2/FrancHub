from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from personal_account.forms import AddFranchiseForm, FranchiseEditForm
from personal_account.models import FranchisePhoto, Franchise


@login_required
def franchise_validation(request, franchise_id):
    franchise = get_object_or_404(Franchise, pk=franchise_id)
    # if franchise.user_id != request.user.id:
    #     return redirect('unauthorized_access')
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
def all_site_franchises(request):
    if not request.user.is_staff:
        return redirect('login')

    publish_filter = request.GET.get('publish_filter')
    franchises = Franchise.objects.all()

    if publish_filter == 'published':
        franchises = franchises.filter(allow_to_publish=True)
    elif publish_filter == 'unpublished':
        franchises = franchises.filter(allow_to_publish=False)

    return render(request, 'all_site_franchises.html', {'franchises': franchises, 'publish_filter': publish_filter})
