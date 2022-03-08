from dataclasses import field
from rest_framework import serializers

from .models import FileModel, ImageModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"


class MultipleFileSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField()
    )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class MultipleImageSerializer(serializers.Serializer):
    images = serializers.ListField(
        child=serializers.ImageField()
    )
