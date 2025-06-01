from django.http import HttpResponse
from .models import PageVisit

# Create your views here.
def pagevisit_view(request, *args, **kwargs):
    PageVisit.objects.create(path=request.path)
    count = PageVisit.objects.filter(path=request.path).count()
    html = "<h1>Page Visits Count:</h1> {count}<br>".format(count=count)
    return HttpResponse(html)
