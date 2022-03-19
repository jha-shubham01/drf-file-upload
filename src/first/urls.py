from rest_framework import routers

from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('file', views.FileViewSet)
router.register('image', views.ImageViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('index/', views.index),
    path('single_upload/', views.single_upload),
    path('multiple_upload/', views.multiple_upload),
]