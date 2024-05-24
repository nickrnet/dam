import uuid

from django.db import models


class BaseMedia(models.Model):
    file = models.FileField(upload_to=uuid.uuid4(), max_length=256)
    name = models.CharField(max_length=255)
