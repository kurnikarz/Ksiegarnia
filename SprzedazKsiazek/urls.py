from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('klienci', views.klient_list.as_view()),
    path('klient/<int:pk>', views.klient_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('pracownicy', views.pracownik_list),
    path('pracownik/<int:pk>', views.pracownik_detail),
    path('autorzy', views.autor_list),
    path('autor/<int:pk>', views.autor_detail),
    path('ksiazki', views.ksiazka_list),
    path('ksiazka/<int:pk>', views.ksiazka_detail)
=======
    path('klienci', views.klient_list),
    path('klienci/<int:pk>', views.klient_detail),
    path('pracownicy', views.pracownik_list),
    path('pracownicy/<int:pk>', views.pracownik_detail)
>>>>>>> 02ed1f6d3e590b07865e924a50d456b657637f2d
]