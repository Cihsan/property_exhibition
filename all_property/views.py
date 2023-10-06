from django.shortcuts import render, HttpResponse

# for api
from rest_framework import viewsets
from .models import Property, PropertyImage
from .serializers import PropertySerializer
from django.db.models import Prefetch


# Create your views here.
def propertylist(request):
    return render(request, "property.html")


# property api
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request  # Include the request object in the context
        return context


def detailproperty(request):
    return render(request, "detail.html")
