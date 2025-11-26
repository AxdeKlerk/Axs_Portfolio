import traceback
from django.http import HttpResponse
from portfolio.views import home as real_home

def probe(request):
    try:
        raise Exception("Render 500 Probe Triggered")
    except Exception:
        return HttpResponse(
            "<pre>" + traceback.format_exc() + "</pre>",
            content_type="text/html"
        )

def homepage_probe(request):
    from django.http import JsonResponse
    try:
        data = {
            "about": str(request.context.get("about", None)) if hasattr(request, "context") else "no context",
            "page": "home",
            "status": "view works"
        }
        return JsonResponse(data)
    except Exception as e:
        import traceback
        return HttpResponse("<pre>" + traceback.format_exc() + "</pre>")

def home_debug(request):
    try:
        return real_home(request)
    except Exception:
        return HttpResponse(
            "<pre>" + traceback.format_exc() + "</pre>",
            content_type="text/html"
        )