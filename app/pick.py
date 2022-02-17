import requests
from bs4 import BeautifulSoup

def pick_up(url):
    res = requests.get(url)
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = soup
    return text

def pick_up_data():     # ３サイトのデータを返す
    target_url = [
        "https://weather.yahoo.co.jp/weather/jp/47/9110.html", 
        "https://tenki.jp/forecast/10/50/9110/47201/", 
        "https://weather.goo.ne.jp/weather/division-1/471010/"
    ]

    data = {
        "yahoo": {
            "weather": None, "high": None, "low": None
        },
        "tenki_jp": {
            "weather": None, "high": None, "low": None
        },
        "goo": {
            "weather": None, "high": None, "low": None
        },
        "total": {
            "weather": None, "high": None, "low": None
        },
    }

    # yahooの情報
    html = pick_up(target_url[0])
    div_site_detail = html.find('div', class_="forecastCity")
    data["yahoo"]["weather"] = div_site_detail.find('p', class_="pict").get_text().replace("\n", "").replace(" ", "")
    data["yahoo"]["high"] = int(div_site_detail.find('li', class_="high").get_text()[0:2])
    data["yahoo"]["low"] = int(div_site_detail.find('li', class_="low").get_text()[0:2])

    # tenki.jpの情報
    html = pick_up(target_url[1])
    div_site_detail = html.find('div', class_="forecast-days-wrap")
    data["tenki_jp"]["weather"] = div_site_detail.find('p', class_="weather-telop").get_text().replace("\n", "").replace(" ", "")
    data["tenki_jp"]["high"] = int(div_site_detail.find('dd', class_="high-temp temp").get_text()[0:2])
    data["tenki_jp"]["low"] = int(div_site_detail.find('dd', class_="low-temp temp").get_text()[0:2])

    # ウェザーニュースの情報
    html = pick_up(target_url[2])
    div_site_detail = html.find_all('div', class_="weather_area weather")[0]
    data["goo"]["weather"] = div_site_detail.find('p', class_="weather").get_text()
    data["goo"]["high"] = int(div_site_detail.find('p', class_="red").get_text()[7:9])
    data["goo"]["low"] = int(div_site_detail.find('p', class_="blue").get_text()[7:9])

    # まとめの情報
    data["total"]["high"] = int((data["yahoo"]["high"] + data["tenki_jp"]["high"] + data["goo"]["high"]) / 3)
    data["total"]["low"] = int((data["yahoo"]["low"] + data["tenki_jp"]["low"] + data["goo"]["low"]) / 3)

    text = data["yahoo"]["weather"] + data["tenki_jp"]["weather"] + data["goo"]["weather"]
    hare = text.count("晴")
    ame = text.count("雨")
    kumo = text.count("曇")
    if (hare > ame) and (hare > kumo):
        data["total"]["weather"] = "晴れ"
    elif (ame > hare) and (ame > kumo):
        data["total"]["weather"] = "雨"
    else:
        data["total"]["weather"] = "曇り"
    
    return data