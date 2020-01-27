from django.db import models

# Create your models here.

class kategoria(models.Model):
    nazwa = models.CharField(max_length=45)

class autor(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

class ksiazka(models.Model):
    nazwa = models.CharField(max_length=45)
    rokWydania = models.DateField()
    cena = models.FloatField()
    Autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    Kategoria = models.ForeignKey(kategoria, on_delete=models.CASCADE)

class klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    nrKontaktowy = models.CharField(max_length=12)

class pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    nrKontaktowy = models.CharField(max_length=12)
    zarobki = models.FloatField()
    tworca = models.ForeignKey('auth.User', related_name='pracownik', on_delete=models.CASCADE)

class zamowienia(models.Model):
    Ksiazka = models.ForeignKey(ksiazka, on_delete=models.CASCADE)
    Klient = models.ForeignKey(klient, on_delete=models.CASCADE)
    Pracownik = models.ForeignKey(pracownik, on_delete=models.CASCADE)
    cena = models.FloatField()