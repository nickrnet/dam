from django_htmx.middleware import HtmxDetails
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models.base_media import BaseMedia
from .models.jpg import Jpg


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    # TODO: get all media types allowed
    jpgs = Jpg.objects.all()
    return render(request, "index.html", {"jpgs": jpgs})


@require_POST
def upload(request: HtmxHttpRequest) -> HttpResponse:
    succesful_upload = False

    if BaseMedia.is_valid_media_type(request.FILES["file"].read()):
        # TODO: save the thing when we know what type it is
        # Jpg.objects.create(file=request.FILES["file"], name=request.FILES["file"].name)
        succesful_upload = True
    return render(request, "upload.html", {"success": succesful_upload})
