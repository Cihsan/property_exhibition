from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about_contact/about.html')


def contact(request):
    return render(request, 'about_contact/contact.html')
