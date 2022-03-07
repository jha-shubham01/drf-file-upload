
from rest_framework import viewsets

from .models import FileModel, ImageModel

from .serializers import FileSerializer, ImageSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer