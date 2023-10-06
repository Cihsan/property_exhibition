from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView,ListView
from django.db.models import Q
from .models import Property
# Create your views here.
def propertylist(request):
    properties = Property.objects.all()
    count = properties.count()
    context={'properties':properties,'count':count}
    return render(request,'property.html',context)

def Test(request):
    return render(request,'test.html')

class propertyDetail(DetailView):
    model = Property
    context_object_name = 'porperty'
    template_name = 'detail.html'

class search(ListView):
    model = Property
    template_name = 'property.html'
    context_object_name = 'properties'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Property.objects.filter(Q(title__icontains=query) |Q(description__icontains=query) |Q(price__icontains=query) |Q(area__icontains=query) |Q(purpose__icontains=query) |Q(completion__icontains=query) |Q(status__icontains=query)| Q(division__icontains=query) | Q(district__icontains=query) | Q(upozila__icontains=query) | Q(union_ward__icontains=query) | Q(village__icontains=query)).order_by('-created_at')
    
    