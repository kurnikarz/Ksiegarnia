from rest_framework import serializers
from .models import *

class kategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kategoria
        fields = ['idKategoria','nazwa']

class autorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autor
        fields = ['idAutor','imie','nazwisko']

class ksiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ksiazka
        fields = ['idKsiazka','nazwa','rokWydania','cena','idAutor','idKategoria']

class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ['idKlient','imie','nazwisko','pesel','nrKontaktowy']

class pracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = pracownik
        fields = ['idPracownik','imie','nazwisko','pesel','nrKontaktowy','zarobki']

class zamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = zamowienia
        fields = ['idZamowienia','idKsiazka','idKlient','idPracownik','cena']