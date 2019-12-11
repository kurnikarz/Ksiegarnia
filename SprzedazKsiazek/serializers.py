from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    klient = serializers.PrimaryKeyRelatedField(many=True, queryset=klient.objects.all())
    class Meta:
        model = User
        fields = ['idUser', 'username', 'klient']

class kategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kategoria
        fields = ['idKategoria','nazwa']

<<<<<<< HEAD
class QuestionSerializer(serializers.ModelSerializer):
    tworca = serializers.ReadOnlyField(source='tworca.username')

    class Meta:
        model = klient
        fields = ['id', 'question_text', 'pub_date', 'tworca']


=======
>>>>>>> 02ed1f6d3e590b07865e924a50d456b657637f2d
class autorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autor
        fields = ['idAutor','imie','nazwisko']

class ksiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ksiazka
        fields = ['idKsiazka','nazwa','rokWydania','cena','idAutor','idKategoria']

class klientSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    tworca = serializers.ReadOnlyField(source='tworca.username')

    class Meta:
        model = klient
        fields = ['idKlient','imie','nazwisko','pesel','nrKontaktowy', 'tworca']
=======
    class Meta:
        model = klient
        fields = ['idKlient','imie','nazwisko','pesel','nrKontaktowy']
>>>>>>> 02ed1f6d3e590b07865e924a50d456b657637f2d

class pracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = pracownik
        fields = ['idPracownik','imie','nazwisko','pesel','nrKontaktowy','zarobki']

class zamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = zamowienia
        fields = ['idZamowienia','idKsiazka','idKlient','idPracownik','cena']