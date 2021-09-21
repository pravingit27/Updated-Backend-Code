from django.db import models
from django.db.models.base import Model
from django.db.models.signals import pre_save
from work.utils import unique_slug_generator

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=100,unique=True,default=None,null=True,blank=True)
    item_url = models.URLField(default=None,unique=True,null=True,blank=True)

    '''class Meta:
        unique_together = (('name', 'slug',))'''

    def __str__(self):
        return self.name
        
class size(models.Model):
    size = models.CharField(max_length=200)
    #slug = models.SlugField(max_length=100,unique=True,default=None,null=True,blank=True)

    def __str__(self):
        return self.size

class meet(models.Model):
    category_name = models.ForeignKey(category,related_name='categories',on_delete=models.CASCADE)
    size_name = models.ForeignKey(size,related_name='size_name',on_delete=models.CASCADE)
    #slug = models.SlugField(max_length=100,unique=True,default=None,null=True,blank=True)
    #item_url = models.URLField(default=None,unique=True,null=True,blank=True)
    image = models.ForeignKey('image',related_name='output',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.category_name} and {self.size_name}'

class image(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to='post_images')
    #slug = models.SlugField(max_length=100,unique=True,default=None,null=True,blank=True)
    relation = models.ForeignKey(meet,related_name='output',on_delete=models.CASCADE)
    image_name = models.CharField(max_length=300)
    #amount = models.FloatField(default=True,blank=True,null=True)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.image_name

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

'''def meet_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = second_slug_generator(instance)'''

pre_save.connect(slug_generator,sender=category)
#pre_save.connect(meet_generator,sender=meet)





