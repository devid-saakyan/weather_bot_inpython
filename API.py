from bs4 import BeautifulSoup
import urllib.request
import bot

def get_it(lat,long):

    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&mode' \
          '=xml&units=metric&appid=a417a9afcbcad213b77ced6b64f2e589'.format(lat, long)
    req = urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'lxml')
    temperature = xml.find('temperature')
    max_temp = temperature.get_attribute_list('max')[0] + "°C"
    min_temp = temperature.get_attribute_list('min')[0] + "°C"
    live_temp = temperature.get_attribute_list('value')[0] + "°C"
    feels_like_ = xml.find('feels_like')
    feels_like = feels_like_.get_attribute_list('value')[0] + "°C"
    humidity_ = xml.find('humidity')
    humidity = humidity_.get_attribute_list('value')[0] + "%"
    wind_speed_ = xml.find('speed')
    wind_speed = wind_speed_.get_attribute_list('value')[0] + "м/с"
    output = 'Погода на улице ❄ : {}\nОщущается как: {}\nМаксимальная температура на сегодня \uD83C\uDF21 : ' \
             '{}\nМинимальная температур на сегодня \uD83C\uDF21 : {}\n' \
             'Влажность воздуха \uD83D\uDCA7 : {}\nСкорость ветра 💨 : ' \
             '{}'.format(live_temp, feels_like, max_temp, min_temp, humidity, wind_speed)
    return output

def function_for_all(url):
    url = url
    req = urllib.request.urlopen(url)
    xml = BeautifulSoup(req, 'lxml')
    temperature = xml.find('temperature')
    max_temp = temperature.get_attribute_list('max')[0] + "°C"
    min_temp = temperature.get_attribute_list('min')[0] + "°C"
    live_temp = temperature.get_attribute_list('value')[0] + "°C"
    feels_like_ = xml.find('feels_like')
    feels_like = feels_like_.get_attribute_list('value')[0] + "°C"
    humidity_ = xml.find('humidity')
    humidity = humidity_.get_attribute_list('value')[0] + "%"
    wind_speed_ = xml.find('speed')
    wind_speed = wind_speed_.get_attribute_list('value')[0] + "м/с"
    output = 'Погода на улице ❄ : {}\nОщущается как: {}\nМаксимальная температура на сегодня \uD83C\uDF21 : ' \
             '{}\nМинимальная температур на сегодня \uD83C\uDF21 : {}\n' \
             'Влажность воздуха \uD83D\uDCA7 : {}\nСкорость ветра 💨 : ' \
             '{}'.format(live_temp, feels_like, max_temp, min_temp, humidity, wind_speed)
    return output
