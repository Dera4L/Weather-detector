from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST': 
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=38906824d750bcc35e6784b0a5692731').read()
        
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp" : str(json_data['main']['temp']) + ' k',
            "pressure" : str(json_data["main"]["pressure"]) + ' N/m2',
            "humidity"  : str(json_data["main"]["humidity"]) + ' g.m-3',
            # "time" : str(json_data["main"]["time"])
        }
    else:
        city = ''
        data = {}
        
    return render(request, "index.html", {"city":city, "data":data})