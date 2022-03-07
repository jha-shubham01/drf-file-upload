from dataclasses import field
from rest_framework import serializers

from .models import FileModel, ImageModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"