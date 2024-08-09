from django.shortcuts import HttpResponse, render
from django.http import response

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from . import models
from . import serializers


@api_view(['GET','POST'])
def gejala_list(request):
    if request.method == 'GET':
        gejala = models.Gejala.objects.all()
        serializer = serializers.GejalaSerializer(gejala, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.GejalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([IsMethodAllowed])
def detail_gejala(req, id):
    try:
        gejala = models.Gejala.objects.get(pk=id)
    except models.Gejala.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.GejalaSerializer(gejala)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.GejalaSerializer(gejala, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        gejala.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
# @permission_classes([IsMethodAllowed])
def penyakit_list(req):
    if req.method == 'GET':
        penyakit = models.Penyakit.objects.all()
        serializer = serializers.PenyakitSerializer(penyakit, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = serializers.PenyakitSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([IsMethodAllowed])
def detail_penyakit(req, id):
    try:
        penyakit = models.Penyakit.objects.get(pk=id)
    except models.Penyakit.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.PenyakitSerializer(penyakit)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.PenyakitSerializer(penyakit, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        penyakit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def basispengetahuan_list(req):
    if req.method == 'GET':
        basis_pengetahuan = models.BasisPengetahuan.objects.all()
        serializer = serializers.BasisPengetahuanSerializer(basis_pengetahuan, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = serializers.BasisPengetahuanSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([IsMethodAllowed])
def detail_bp(req, id):
    try:
        penyakit = models.BasisPengetahuan.objects.get(pk=id)
    except models.BasisPengetahuan.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.BasisPengetahuanSerializer(penyakit)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.BasisPengetahuanSerializer(penyakit, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        penyakit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def riwayat_list(request):
    if request.method == 'GET':
        riwayat = models.Riwayat.objects.all()
        serializer = serializers.RiwayatSerializer(riwayat, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.RiwayatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([IsMethodAllowed])
def detail_riwayat(req, id):
    try:
        riwayat = models.Riwayat.objects.get(pk=id)
    except models.Gejala.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = serializers.GejalaSerializer(riwayat)
        return Response(serializer.data)

    elif req.method == 'PATCH':
        serializer = serializers.GejalaSerializer(riwayat, data=req.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif  req.method == 'DELETE':
        riwayat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    