import traceback
from django.http import HttpResponse

def probe(request):
    try:
        raise Exception("Render 500 Probe Triggered")
    except Exception:
        return HttpResponse(
            "<pre>" + traceback.format_exc() + "</pre>",
            content_type="text/html"
        )
