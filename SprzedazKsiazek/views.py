from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404

# Create your views here.

class klient_list(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        klienci = klient.objects.all()
        serializer = klientSerializer(klienci, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = klientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class klient_detail(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return klient.objects.get(pk=pk)
        except klient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = klientSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = klientSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class pracownik_list(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        pracownicy = pracownik.objects.all()
        serializer = pracownikSerializer(pracownicy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = pracownikSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class pracownik_detail(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return pracownik.objects.get(pk=pk)
        except pracownik.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = pracownikSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = pracownikSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def autor_list(request):
    if request.method == 'GET':
        autorzy = autor.objects.all()
        serializer = autorSerializer(autorzy, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = autorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def autor_detail(request, pk):
    try :
        autorzy = autor.objects.get(pk=pk)
    except autor.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = autorSerializer(autorzy)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = autorSerializer(autorzy, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        autor.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def ksiazka_list(request):
    if request.method == 'GET':
        ksiazki = ksiazka.objects.all()
        serializer = ksiazkaSerializer(ksiazki, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ksiazkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ksiazka_detail(request, pk):
    try:
        ksiazki = ksiazka.objects.get(pk=pk)
    except ksiazka.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ksiazkaSerializer(ksiazki)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ksiazkaSerializer(ksiazki, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        ksiazki.delete()
        return Response(status.HTTP_204_NO_CONTENT)