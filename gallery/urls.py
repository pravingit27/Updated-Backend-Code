from django.urls import path,include
from .views import ListCategory,DetailCategory,ListSize,DetailSize,ListImage,DetailImage,ListMeet,DetailMeet

urlpatterns = [
    path('show',ListCategory.as_view(),name='category'),
    path('show/<int:pk>',DetailCategory.as_view(),name='singlecategory'),
    path('size',ListSize.as_view(),name='size'),
    path('size/<int:pk>',DetailSize.as_view(),name='detailsize'),
    path('image',ListImage.as_view(),name='image'),
    path('image/<int:pk>',DetailImage.as_view(),name='singleimage'),
    path('meet',ListMeet.as_view(),name='meet'),
    path('meet/<int:pk>',DetailMeet.as_view(),name='singlemeet')
]
