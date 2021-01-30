from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    isNewYear = now.month == 1 and now.day == 1
   #  return HttpResponse(f"{isNewYear}")
    return render(request, "newyear/index.html", {
        "newyear": isNewYear
        }
    )

