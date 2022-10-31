from django.shortcuts import render, get_object_or_404
from .models import Category, Services
# Create your views here.



def services(request):
    services = Services.objects.all().last()
    context = {'services':services}

    return render(request, 'services/services.html', context)


def service(request, s_id):
    service = get_object_or_404(Services, pk=s_id)
    context = {'service':service}

    return render(request, 'services/service.html', context)

def categories(request):
    categories = Category.objects.all()
    context ={'categories':categories}

    return render(request, 'services/categories.html', context)



def category(request, c_id):
    category = get_object_or_404(Category, pk=c_id)
    services = Services.objects.filter(category=category)
    context = {
        'category':category,
        'services':services
    }

    return render(request, 'services/category.html', context)

    