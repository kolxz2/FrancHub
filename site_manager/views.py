from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from personal_account.forms import AddFranchiseForm, FranchiseEditForm
from personal_account.models import FranchisePhoto, Franchise, LocationMap
from personal_account.views import all_regions


@login_required
def franchise_validation(request, franchise_id):
    franchise = get_object_or_404(Franchise, pk=franchise_id)
    # if request.user.is_staff:
    #     return redirect('unauthorized_access')
    if request.method == 'POST':
        if 'action' in request.POST:
            action = request.POST.get('action')
            comment = request.POST.get('sait_manager_comment', '')
            if action == 'comment':
                franchise.sait_manager_comment = comment
                franchise.allow_to_publish = False
            elif action == 'publish':
                franchise.allow_to_publish = True
            franchise.save()
            return redirect('all_site_franchises')
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
        initial_data = []
        location_maps = LocationMap.objects.filter(franchise=franchise.franchise_id)
        for location in location_maps:
            for field in location._meta.fields:
                if field.name not in ['id', 'franchise'] and getattr(location,
                                                                     field.name) > 0 and field.name != 'map_id':
                    initial_data.append({'region': field.name, 'value': getattr(location, field.name)})
    return render(request, 'franchise_validation.html',
                  {'franchise': franchise, 'form': form, "all_regions": all_regions, 'initial_data': initial_data})


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
