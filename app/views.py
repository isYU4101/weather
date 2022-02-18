from django.shortcuts import render
from django.http import HttpResponse
from .pick import pick_up_data
import datetime
import pytz

def index(request):
    dt_now = str(datetime.datetime.now(pytz.timezone('Asia/Tokyo')))
    month = dt_now[5:7]
    day = dt_now[8:10]
    data = pick_up_data()["total"]
    params = {
        'title': "まとめ",
        'month': month,
        'day': day,
        'weather': data["weather"],
        'high': data["high"],
        'low': data["low"],
        'url': "http://localhost:8000/app/"
    }
    return render(request, 'app/index.html', params)

def yahoo(request):
    dt_now = str(datetime.datetime.now())
    month = dt_now[5:7]
    day = dt_now[8:10]
    data = pick_up_data()["yahoo"]
    params = {
        'title': "Yahoo!",
        'month': month,
        'day': day,
        'weather': data["weather"],
        'high': data["high"],
        'low': data["low"],
        'url': "https://weather.yahoo.co.jp/weather/jp/47/9110.html"
    }
    return render(request, 'app/index.html', params)

def tenki_jp(request):
    dt_now = str(datetime.datetime.now())
    month = dt_now[5:7]
    day = dt_now[8:10]
    data = pick_up_data()["tenki_jp"]
    params = {
        'title': "tenki.jp",
        'month': month,
        'day': day,
        'weather': data["weather"],
        'high': data["high"],
        'low': data["low"],
        'url': "https://tenki.jp/forecast/10/50/9110/47201/"
    }
    return render(request, 'app/index.html', params)

def goo(request):
    dt_now = str(datetime.datetime.now())
    month = dt_now[5:7]
    day = dt_now[8:10]
    data = pick_up_data()["goo"]
    params = {
        'title': "weather.goo",
        'month': month,
        'day': day,
        'weather': data["weather"],
        'high': data["high"],
        'low': data["low"],
        'url': "https://weather.goo.ne.jp/weather/division-1/471010/"
    }
    return render(request, 'app/index.html', params)
# Create your views here.