from django.shortcuts import render, get_object_or_404
from cities.models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import HtmlForm, CityForm


__all__ = (
    "home", "CityDetailView", "CityCreateView", "CityUpdateView", "CityDeleteView", "CityListView",
)

# Create your views here.
def home(request, pk=None):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
#    if pk:
#        #city = City.objects.filter(pk=pk).first()
#        city = get_object_or_404(City, pk=pk)
#        context = {'object':city}
#        return render(request, 'cities/detail.html', context)

    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj, "form":form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

class CityDeleteView(DeleteView):
    model = City
#    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = "cities;/home.html"

    