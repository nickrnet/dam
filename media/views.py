from django_htmx.middleware import HtmxDetails
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models.jpg import Jpg


class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    jpgs = Jpg.objects.all()
    return render(request, "index.html", {"jpgs": jpgs})
