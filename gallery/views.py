from django.shortcuts import render
from .serializers import CategorySerializer,SizeSerializer,DetailSerializer,ImageSerializer
from rest_framework import generics, serializers
from .models import size,category,meet,image

# Create your views here.
class ListCategory(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class ListSize(generics.ListCreateAPIView):
    queryset = size.objects.all()
    serializer_class = SizeSerializer

class DetailSize(generics.RetrieveUpdateDestroyAPIView):
    queryset = size.objects.all()
    serializer_class = SizeSerializer

class ListMeet(generics.ListCreateAPIView):
    queryset = meet.objects.all()
    serializer_class = DetailSerializer

class DetailMeet(generics.RetrieveUpdateDestroyAPIView):
    queryset = meet.objects.all()
    serializer_class = DetailSerializer

class ListImage(generics.ListCreateAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer

class DetailImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer

