import datetime
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from formly.models import Survey

def index(request):
    surveys = [f for f in Survey.objects.filter(published__lte=datetime.date.today())]
    return render(request, "homepage.html", {'surveys': surveys})
