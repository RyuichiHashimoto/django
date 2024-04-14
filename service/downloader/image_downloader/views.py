from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from .download.downloader import SiteEnum
import urllib


@require_GET
def download(request):

    if request.method != "GET":
        error_data = {"error": "Invalid request method"}
        return JsonResponse(error_data, status=405)

    try:
        last_url = urllib.parse.unquote(request.GET.get("last_url", ""))
        book_name = urllib.parse.unquote(request.GET.get("book_name", ""))

        # urllib(last)

        if last_url == "" or book_name == "":
            raise ValueError("site and/or book_name are required")

        SiteEnum.download(last_url, book_name)

        return HttpResponse("Hello, world. You're at the polls index")
    except Exception as e:
        error_data = {"error": str(e)}
        import traceback

        traceback.print_exc()
        return JsonResponse(error_data, status=500)
    finally:
        return
