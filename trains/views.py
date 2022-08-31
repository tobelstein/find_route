from django.shortcuts import render, get_object_or_404
from trains.models import Train
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# from trains.forms import HtmlForm, TrainForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

__all__ = (
    "home",  "TrainListView", "TrainDetailView",
    #  "TrainDeleteView",
    #  "TrainCreateView", "TrainUpdateView",
)

# Create your views here.
def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'trains/home.html', context)

class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = "trains/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super.get_context_data(**kwargs)
    #     form = TrainForm()
    #     context['form'] = form
    #     return context


class TrainDetailView(DetailView):
     queryset = Train.objects.all()
     template_name = 'trains/detail.html'

# class TrainCreateView(SuccessMessageMixin, CreateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/create.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = "Город успешно создан"

# class TrainUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('trains:home')
#     success_message = "Город успешно отредактирован"

# class TrainDeleteView(SuccessMessageMixin, DeleteView):
#     model = Train
# #    template_name = 'trains/delete.html'
#     success_url = reverse_lazy('trains:home')
    
#     def get(self, request, *args, **kwargs):
#         messages.success(request, 'Город успешно удален')
#         return self.post(request, *args, **kwargs)

