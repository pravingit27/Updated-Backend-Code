from django.db import models
from django.db.models import fields
from rest_framework import relations, serializers
from .models import category,meet,image,size
from rest_framework.serializers import Serializer
from drf_writable_nested.serializers import WritableNestedModelSerializer,NestedUpdateMixin

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = category
		fields = ('pk','name','url','slug')
		read_only_fields = ('url',)
		extra_kwargs = {'url': {'lookup_field': 'slug'}}

	'''def to_representation(self,instance):
		product = super(CategorySerializer,self).to_representation(instance)
		product['parent'] = instance.parent.size
		return product'''

class SizeSerializer(serializers.ModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name='api:user-list', source='username',
												  # lookup_url_kwarg='slug', lookup_field='slug')
	class Meta:
		model = size
		fields = ('pk','size')
		#exclude = ['slug',]

class ImageMeetSerializer(serializers.ModelSerializer):
	class Meta:
		model = image
		fields = ('image_name','images')

class DetailSerializer(serializers.ModelSerializer):
	output= ImageMeetSerializer(many=True,read_only=True)
	class Meta:
		model = meet
		fields = ('id','category_name','size_name','output')
		#read_only_fields = ('url',)
		#extra_kwargs = {'url': {'lookup_field': 'slug'}}

	def to_representation(self,instance):
		result = super(DetailSerializer,self).to_representation(instance)
		result['size_name'] = instance.size_name.size
		result['category_name'] = instance.category_name.name
		return result

'''class ListSerializer(serializers.Serializer):
	image_name = serializers.CharField(max_length = 50)
	images = serializers.ListField(
	  child = serializers.FileField(max_length = 100000,
		allow_empty_file = False,
		use_url = False))
	#relation = serializers.PrimaryKeyRelatedField()

	def create(self, validated_data):
		relation = meet.objects.create( 'id' ,**validated_data)
		result = validated_data.pop('images')
		image_name = validated_data.pop('image_name')
		#relation = validated_data.pop('relation')
		for img in result:
			photo = image.objects.create(relation = relation,images = img,image_name = image_name ,** validated_data)
		photo.save()
		return photo '''  
	
class ImageSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
	images = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
	#relation = DetailSerializer()
	
	class Meta:
		model = image
		fields = ('pk','relation','images','image_name')
		#read_only_fields = ('url',)
		#extra_kwargs = {'url': {'lookup_field': 'slug'}}

	def to_representation(self,instance):
		result = super(ImageSerializer,self).to_representation(instance)
		result['relation'] = f'{instance.relation.category_name} + {instance.relation.size_name}'
		#result['category_name'] = instance.category_name.name
		return result	

	
	

	

	



