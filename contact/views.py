from django.shortcuts import render
from .models import Contact
# Create your views here.



def contact(request):
    contact = Contact.objects.all()
    context = {'contact':contact}


    return render(request, 'contact/contact.html', context)

    

    