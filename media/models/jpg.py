from exif import Image

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .base_media import BaseMedia as BaseMediaModel


class Jpg(BaseMediaModel):
    def get_exif_data(self) -> dict:
        image_file = ContentFile(default_storage.open(self.file).read())
        with open(image_file, 'rb') as image_file_content:
            image = Image(image_file_content)
            if image.has_exif:
                return image.exif_data
            else:
                return {}
