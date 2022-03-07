from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='file/')


class ImageModel(models.Model):
    file = models.ImageField(upload_to='img/')