# Generated by Django 2.2.7 on 2020-01-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SprzedazKsiazek', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pracownik',
            name='tworca',
        ),
    ]
