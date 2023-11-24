from django.urls import path
from padaria.views import ReceitaListView, ReceitaCrateView, ReceitaDeleteView

urlpatterns = [
    path("novaReceita", ReceitaListView.as_view(), name="padaria_list"),
    path("", ReceitaCrateView.as_view(), name="padaria_create"),
    path("delete/<int:pk>", ReceitaDeleteView.as_view(), name="receita_delete")

]
