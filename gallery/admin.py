from django.contrib import admin
from .models import category,size,image,meet

# Register your models here.
admin.site.register(category)
#admin.site.register(image)
admin.site.register(size)
#admin.site.register(meet)

class PostImageAdmin(admin.StackedInline):
    model = image

@admin.register(meet)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = meet
 
@admin.register(image)
class PostImageAdmin(admin.ModelAdmin):
    pass