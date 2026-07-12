from django.http import HttpResponse                          # Send text back to the browser

# -------------------------------------------------------------------------
# View: hello
#
# A view is a Python function that receives an HTTP request
# and returns an HTTP response.
#
# request  -> Information sent by the browser.
# response -> Information sent back to the browser.
# -------------------------------------------------------------------------

def hello(request):
    """
    This is our first Django view.

    Whenever the browser visits the URL mapped to this function,
    Django calls this function automatically.
    """

    return HttpResponse("Hello from Django!")