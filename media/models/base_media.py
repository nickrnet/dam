import logging
import uuid

import magic

from django.db import models


logger = logging.getLogger(__name__)


class BaseMedia(models.Model):

    class Meta:
        abstract = True

    class AllowedTypes(models.TextChoices):
        JPG = "image/jpeg", "IMAGE/JPEG"
        PNG = "image/png", "IMAGE/PNG"
        GIF = "image/gif", "IMAGE/GIF"
        MP4 = "image/mp4", "IMAGE/MP4"

    file = models.FileField(upload_to=uuid.uuid4(), max_length=256)
    name = models.CharField(max_length=255)

    @classmethod
    def is_valid_media_type(self, file: bytes) -> bool:
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file)
        logger.debug(f"Uploaded file mime_type: {mime_type}")
        return mime_type in self.AllowedTypes.values
