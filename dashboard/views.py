from django.shortcuts import render


# Create your views here.
def dashbaord_view(request):
    return render(request, "dashboard.html")
