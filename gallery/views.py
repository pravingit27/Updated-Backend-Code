from django.shortcuts import render
from .serializers import CategorySerializer,SizeSerializer,DetailSerializer,ImageSerializer
from rest_framework import generics, serializers, views
from .models import size,category,meet,image
from rest_framework import viewsets
from work.helpers import modify_input_for_multiple_files
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser

# Create your views here.
'''class ListCategory(generics.ListCreateAPIView):
	queryset = category.objects.all()
	serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
	queryset = category.objects.all()
	serializer_class = CategorySerializer
	lookup_field = 'slug'''

class CategoryView(viewsets.ModelViewSet):
	queryset = category.objects.all()
	serializer_class = CategorySerializer
	lookup_field = 'slug'
	
class ListSize(generics.ListCreateAPIView):
	queryset = size.objects.all()
	serializer_class = SizeSerializer

class DetailSize(generics.RetrieveUpdateDestroyAPIView):
	queryset = size.objects.all()
	serializer_class = SizeSerializer

'''class ListMeet(generics.ListCreateAPIView):
	queryset = meet.objects.all()
	serializer_class = DetailSerializer

class DetailMeet(generics.RetrieveUpdateDestroyAPIView):
	queryset = meet.objects.all()
	serializer_class = DetailSerializer'''

class ResultView(viewsets.ModelViewSet):
	queryset = meet.objects.all()
	serializer_class = DetailSerializer
	#lookup_field = 'slug'

class ListImage(generics.ListCreateAPIView):
	queryset = image.objects.all()
	serializer_class = ImageSerializer

class DetailImage(generics.RetrieveUpdateDestroyAPIView):
	queryset = image.objects.all()
	serializer_class = ImageSerializer

	def get_serializer(self, instance=None, data=None, many=False, partial=False):
			if data is not None:
				data.is_valid(raise_exception=True)
				return super(DetailImage, self).get_serializer(instance=instance, data=data, partial=partial)
			else:
				return super(DetailImage, self).get_serializer(instance=instance, partial=partial)

'''class ImageView(viewsets.ModelViewSet):
	queryset = image.objects.all()
	parser_classes = (MultiPartParser, FormParser,)
	serializer_class = ImageSerializer'''
	#lookup_field = 'slug'


