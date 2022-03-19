from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from django.shortcuts import render
from django.http import JsonResponse

from .models import FileModel, ImageModel

from .serializers import FileSerializer, ImageSerializer, MultipleImageSerializer, MultipleFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        """Upload multiple files and create objects."""
        serializer = MultipleFileSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        files = serializer.validated_data.get("files")

        files_list = []
        for file in files:
            files_list.append(
                FileModel(file=file)
            )
        if files_list:
            FileModel.objects.bulk_create(files_list)

        return Response("Success")


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        """Upload multiple images and create objects."""
        serializer = MultipleImageSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        images = serializer.validated_data.get("images")

        images_list = []
        for image in images:
            images_list.append(
                ImageModel(file=image)
            )
        if images_list:
            ImageModel.objects.bulk_create(images_list)

        return Response("Success")


# WITHOUT DRF UPLOADS

def single_upload(request):
    file = request.FILES.get("file")
    FileModel.objects.create(file=file)
    return JsonResponse({"message": "Success"})


def multiple_upload(request):
    files = request.FILES.getlist("files")

    files_list = []
    for file in files:
        files_list.append(FileModel(file=file))

    if files_list:
        FileModel.objects.bulk_create(files_list)

    return JsonResponse({"message": "Success"})


def index(request):
    return render(template_name="index.html", request=request)