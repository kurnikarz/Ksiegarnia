from django.http import HttpResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
@api_view(['GET','POST'])
def klient_list(request):
    if request.method == 'GET':
        klienci = klient.objects.all()
        serializer = klientSerializer(klienci, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = klientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def klient_detail(request, pk):
    try:
        klient = klient.objects.get(pk=pk)
    except klient.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = klientSerializer(klient)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = klientSerializer(klient, request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        klient.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def pracownik_list(request):
    if request.method == 'GET':
        pracownicy = pracownik.objects.all()
        serializer = pracownikSerializer(pracownicy, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = pracownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pracownik_detail(request, pk):
    try:
        pracownik = pracownik.objects.get(pk=pk)
    except pracownik.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = pracownikSerializer(pracownik)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        serializer = pracownikSerializer(pracownik, request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        pracownik.delete()
        return Response(status.HTTP_204_NO_CONTENT)