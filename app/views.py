from django.shortcuts import render
from django.http import HttpResponse
from .pick import pick_up_data
import datetime

def index(request):
    dt_now = str(datetime.datetime.now())
    month = dt_now[5:7]
    day = dt_now[8:10]
    data = pick_up_data()["total"]
    params = {
        'month': month,
        'day': day,
        'weather': data["weather"],
        'high': data["high"],
        'low': data["low"]
    }
    return render(request, 'app/index.html', params)

# Create your views here.