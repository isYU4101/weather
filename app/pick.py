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
            "wether": None, "high": None, "low": None
        },
        "tenki_jp": {
            "wether": None, "high": None, "low": None
        },
        "goo": {
            "wether": None, "high": None, "low": None
        }
    }
    # yahooの情報
    html = pick_up(target_url[0])
    div_site_detail = html.find('div', class_="forecastCity")
    data["yahoo"]["wether"] = div_site_detail.find('p', class_="pict").get_text().replace("\n", "").replace(" ", "")
    data["yahoo"]["high"] = div_site_detail.find('li', class_="high").get_text()[0:2]
    data["yahoo"]["low"] = div_site_detail.find('li', class_="low").get_text()[0:2]

    # tenki.jpの情報
    html = pick_up(target_url[1])
    div_site_detail = html.find('div', class_="forecast-days-wrap")
    data["tenki_jp"]["wether"] = div_site_detail.find('p', class_="weather-telop").get_text().replace("\n", "").replace(" ", "")
    data["tenki_jp"]["high"] = div_site_detail.find('dd', class_="high-temp temp").get_text()[0:2]
    data["tenki_jp"]["low"] = div_site_detail.find('dd', class_="low-temp temp").get_text()[0:2]

    # ウェザーニュースの情報
    html = pick_up(target_url[2])
    div_site_detail = html.find_all('div', class_="weather_area weather")[0]
    data["goo"]["wether"] = div_site_detail.find('p', class_="weather").get_text()
    data["goo"]["high"] = div_site_detail.find('p', class_="red").get_text()[7:9]
    data["goo"]["low"] = div_site_detail.find('p', class_="blue").get_text()[7:9]
    return data

print(pick_up_data())