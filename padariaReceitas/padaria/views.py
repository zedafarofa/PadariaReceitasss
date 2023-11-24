from django.views.generic import ListView, CreateView, DeleteView
from .models import Receita
from django.urls import reverse_lazy


class ReceitaListView(ListView):
    model = Receita


class ReceitaCrateView(CreateView):
    model = Receita
    fields = ["titulo", "descricao"]
    success_url = reverse_lazy("padaria_list")

class ReceitaDeleteView(DeleteView):
    model = Receita
    success_url = reverse_lazy("padaria_list")