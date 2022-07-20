from django.shortcuts import render, get_object_or_404
from cities.models import City

__all__ = (
    "home",
)

# Create your views here.
def home(request, pk=None):
    if pk:
        #city = City.objects.filter(pk=pk).first()
        city = get_object_or_404(City, pk=pk)
        context = {'object':city}
        return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'objects_list':qs}
    return render(request, 'cities/home.html', context)
