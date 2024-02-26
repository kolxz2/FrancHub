from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from accounts.models import CustomUser
from personal_account.models import Franchise, FranchisePhoto, RequestsToBuy, Category


# @csrf_exempt
def main_list(request):
    budget = request.GET.get('budget')
    category = request.GET.get('category')
    if budget and budget != '':
        if budget == "5000000":
            # В случае, если выбрано "Более 5,000,000 ₽", фильтруем объекты, где start_investments больше или равно 5000000
            franchise_list = Franchise.objects.filter(start_investments__gte=5000000)
        else:
            min_investment, max_investment = map(int, budget.split('/'))
            franchise_list = Franchise.objects.filter(start_investments__gte=min_investment,
                                                      start_investments__lte=max_investment)
    else:
        franchise_list = Franchise.objects.all()
    if category and category != '':
        franchise_list = franchise_list.filter(category__title=category)
    categories = Category.objects.all()
    user = request.user
    return render(request, 'main_list.html',
                  {'franchise_list': franchise_list,
                   'user': user,
                   'categories': categories,
                   'budget': budget,
                   'category': category
                   }
                  )


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
        return render(request, 'franchise_info.htm',
                      {'franchise': franchise, 'franchise_photos': franchise_photos, 'user': user})
