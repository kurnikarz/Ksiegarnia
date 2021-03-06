from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class kategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kategoria
        fields = ['id','nazwa']

class autorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autor
        fields = ['id','imie','nazwisko']

class ksiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ksiazka
        fields = ['id','nazwa','rokWydania','cena','Autor','Kategoria']

class klientSerializer(serializers.ModelSerializer):

    class Meta:
        model = klient
        fields = ['id','imie','nazwisko','pesel','nrKontaktowy']

class pracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = pracownik
        fields = ['id','imie','nazwisko','pesel','nrKontaktowy','zarobki']

class zamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = zamowienia
        fields = ['id','Ksiazka','Klient','Pracownik','cena']