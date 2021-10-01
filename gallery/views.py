from django.core import exceptions
from django.shortcuts import render
from .serializers import CategorySerializer,SizeSerializer,DetailSerializer,ImageSerializer
from rest_framework import generics, serializers, views
from .models import size,category,meet,image
from rest_framework import viewsets
from work.helpers import modify_input_for_multiple_files
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from django.http import JsonResponse
from work.utils import handle_uploaded_file

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

'''class ListImage(generics.ListCreateAPIView):
	queryset = image.objects.all()
	serializer_class = ImageSerializer

	parser_classes = (MultiPartParser, FormParser,)
	# http_method_names = ['get', 'post', 'head']

class DetailImage(generics.RetrieveUpdateDestroyAPIView):
	queryset = image.objects.all()
	serializer_class = ImageSerializer'''

class ImageViewSet(viewsets.ModelViewSet):
	queryset = image.objects.all()
	serializer_class = ImageSerializer

'''class ImageView(views.APIView):
	#queryset = image.objects.all()
	parser_classes = (MultiPartParser, FormParser, JSONParser)
	#serializer_class = ImageSerializer
	#lookup_field = 'slug'

	def get(self, request, format=None, *args, **kwargs):
		photo = image.objects.all()
		serializer = ImageSerializer(photo, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ImageSerializer(data=request.data) 
		image_list = request.FILES.getlist('images')
		relation = request.data['relation']
		
		if serializer.is_valid():
			for item in image_list:
				f = image.objects.create(relation =relation,image_name=request.data['image_name'], images=item)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

	

	

