from django.contrib import admin
from .models import category,size,image,meet

# Register your models here.
admin.site.register(category)
admin.site.register(image)
admin.site.register(size)
admin.site.register(meet)