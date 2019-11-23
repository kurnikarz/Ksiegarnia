from rest_framework import serializers
from .models import *

class kategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = kategoria
        fields = ['idKategoria','nazwa']
