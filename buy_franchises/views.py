from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from accounts.models import CustomUser
from personal_account.models import Franchise, FranchisePhoto, RequestsToBuy, Category, LocationMap, Region
from personal_account.views import all_regions


# @csrf_exempt
from django.db.models import Q

def main_list(request):
    budget = request.GET.get('budget')
    category = request.GET.get('category')
    search_query = request.GET.get('search')

    franchise_list = Franchise.objects.filter(allow_to_publish="published")

    if budget and budget != '':
        if budget == "5000000":
            franchise_list = franchise_list.filter(start_investments__gte=5000000)
        else:
            min_investment, max_investment = map(int, budget.split('/'))
            franchise_list = franchise_list.filter(start_investments__gte=min_investment,
                                                   start_investments__lte=max_investment)
    if category and category != '':
        franchise_list = franchise_list.filter(category__title=category)

    if search_query and search_query != '':
        franchise_list = franchise_list.filter(
            Q(advantages_over_competitors__icontains=search_query) |
            Q(company_description__icontains=search_query) |
            Q(costs_at_the_franchise_launch_stage__icontains=search_query) |
            Q(example_of_profit_calculation__icontains=search_query) |
            Q(juicy_description_of_the_franchise__icontains=search_query) |
            Q(most_important_choosing_factors__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(title__icontains=search_query) |
            Q(training_and_support__icontains=search_query) |
            Q(what_is_included_in_the_lump_sum__icontains=search_query)
        )

    categories = Category.objects.all()
    user = request.user

    return render(request,
                  'main_list.html',
                  {
                      'franchise_list': franchise_list,
                      'user': user,
                      'categories': categories,
                      'budget': budget,
                      'category': category,
                      'search_query': search_query
                  })


@csrf_exempt
def franchise_info(request, franchise_id):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, email=request.user.email)
        franchise = get_object_or_404(Franchise, pk=franchise_id)
        # Создаем новую запись в модели RequestsToBuy
        new_request = RequestsToBuy(user=user, franchise=franchise)
        new_request.save()

        return HttpResponse("Franchise ID franchise_info received successfully!")
    else:
        franchise = get_object_or_404(Franchise, pk=franchise_id)
        franchise_photos = FranchisePhoto.objects.filter(franchise=franchise)
        user = request.user
        regions = Region.objects.all()
        total_initial_investment = franchise.start_investments + franchise.lump_sum_payment
        initial_data = []
        location_maps = LocationMap.objects.filter(franchise=franchise)
        for location in location_maps:
            for field in location._meta.fields:
                if field.name not in ['id', 'franchise'] and getattr(location, field.name) > 0:
                    region_data = next((item for item in all_regions if item['value'] == field.name), None)
                    if region_data:
                        initial_data.append({
                            'region': region_data['text'],
                            'value': getattr(location, field.name),
                            'geo': region_data['geo']
                        })
        return render(request, 'franchise_info.htm',
                      {
                          'franchise': franchise,
                          'franchise_photos': franchise_photos,
                          'user': user,
                          'regions': regions,
                          'total_initial_investment': total_initial_investment,
                          'initial_data': initial_data
                      }
                      )
