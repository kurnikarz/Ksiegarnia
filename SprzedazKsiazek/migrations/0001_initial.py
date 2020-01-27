# Generated by Django 2.2.7 on 2020-01-23 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('pesel', models.CharField(max_length=11)),
                ('nrKontaktowy', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ksiazka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=45)),
                ('rokWydania', models.DateField()),
                ('cena', models.FloatField()),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SprzedazKsiazek.autor')),
                ('Kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SprzedazKsiazek.kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('pesel', models.CharField(max_length=11)),
                ('nrKontaktowy', models.CharField(max_length=12)),
                ('zarobki', models.FloatField()),
                ('tworca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pracownik', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='zamowienia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.FloatField()),
                ('Klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SprzedazKsiazek.klient')),
                ('Ksiazka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SprzedazKsiazek.ksiazka')),
                ('Pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SprzedazKsiazek.pracownik')),
            ],
        ),
    ]
