from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.klient_list.as_view()),
    path('klienci/<int:pk>', views.klient_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('pracownicy', views.pracownik_list.as_view()),
    path('pracownicy/<int:pk>', views.pracownik_detail.as_view()),
    path('autorzy', views.autor_list),
    path('autorzy/<int:pk>', views.autor_detail),
    path('ksiazki', views.ksiazka_list),
    path('ksiazki/<int:pk>', views.ksiazka_detail)
]