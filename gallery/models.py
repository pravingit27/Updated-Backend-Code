from django.db import models
from django.db.models.base import Model

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.CharField(max_length=100,unique=True,default=None)
    item_url = models.URLField(default=None,unique=True)

    class Meta:
        unique_together = ('name', 'slug',)

    def __str__(self):
        return self.name
        
class size(models.Model):
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size

class meet(models.Model):
    category_name = models.ForeignKey(category,related_name='categories',on_delete=models.CASCADE)
    size_name = models.ForeignKey(size,related_name='size_name',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category_name} and {self.size_name}'

class image(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to='post_images')
    relation = models.ForeignKey(meet,related_name='output',on_delete=models.CASCADE)
    image_name = models.CharField(max_length=300)
    amount = models.FloatField(default=True,blank=True,null=True)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.image_name



