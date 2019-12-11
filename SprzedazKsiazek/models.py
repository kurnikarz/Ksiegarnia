from django.db import models

# Create your models here.

class kategoria(models.Model):
    idKategoria = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=45)

class autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

class ksiazka(models.Model):
    idKsiazka = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=45)
    rokWydania = models.DateField()
    cena = models.FloatField()
    idAutor = models.ForeignKey(autor, on_delete=models.CASCADE)
    idKategoria = models.ForeignKey(kategoria, on_delete=models.CASCADE)

class klient(models.Model):
    idKlient = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    nrKontaktowy = models.CharField(max_length=12)
    tworca = models.ForeignKey('auth.User', related_name='klient', on_delete=models.CASCADE)

class pracownik(models.Model):
    idPracownik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=11)
    nrKontaktowy = models.CharField(max_length=12)
    zarobki = models.FloatField()

class zamowienia(models.Model):
    idZamowienia = models.AutoField(primary_key=True)
    idKsiazka = models.ForeignKey(ksiazka, on_delete=models.CASCADE)
    idKlient = models.ForeignKey(klient, on_delete=models.CASCADE)
    idPracownik = models.ForeignKey(pracownik, on_delete=models.CASCADE)
    cena = models.FloatField()