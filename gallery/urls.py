from gallery.models import category
from django.urls import path,include
from .views import ListSize,DetailSize,ImageViewSet
from rest_framework import routers
from . import views
from rest_framework import permissions

router = routers.DefaultRouter()

router.register(r'items', views.CategoryView)
#router.register(r'image',views.ImageView)
router.register(r'result',views.ResultView)
router.register(r'images',views.ImageViewSet)

urlpatterns = [
    #path('show',ListCategory.as_view(),name='category'),
    #path('show/<int:pk>',DetailCategory.as_view(),name='singlecategory'),
    path('size',ListSize.as_view(),name='size'),
    path('size/<int:pk>',DetailSize.as_view(),name='detailsize'),
    #path('image',ListImage.as_view(),name='image'),
    #path('image/<int:pk>',DetailImage.as_view(),name='singleimage'),
    #path('meet',ListMeet.as_view(),name='meet'),
    #path('meet/<int:pk>',DetailMeet.as_view(),name='singlemeet'),
    path('',include(router.urls))
]
