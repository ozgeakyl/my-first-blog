from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def my_view(request):
    now = timezone.now()
    return render(request, "my_template.html", {"now": now})