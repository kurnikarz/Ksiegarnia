from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.klient_list),
    path('klienci/<int:pk>', views.klient_detail),
    path('pracownicy', views.pracownik_list),
    path('pracownicy/<int:pk>', views.pracownik_detail)
]