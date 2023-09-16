
from django.shortcuts import render

import requests
from weather import settings


# Create your views here.


def index(request):

    city=request.GET.get('city')
    api_key = settings.WEATHERSTACK_API_KEY

    if city:
        url= f"http://api.weatherstack.com/current"
        params={"access_key": api_key, "query":city}
        response=requests.get(url,params=params)

        if response.status_code ==200:
            data=response.json()
            if 'current' in data:
                temperature =data['current']['temperature']
                description=data['current']['weather_descriptions'][0]
                humidity=data['current']['humidity']
                weather_icons = data['current']['weather_icons']
                region = data['location']['region']

                return render(request,'weather.html',{'city':city, 'temperature':temperature,'description':description,'humidity':humidity,'weather_icons': weather_icons,'region':region})

            else:
                error_message = "Weather data format is not as expected."
                return render(request, 'weather.html', {'error_message': error_message})
        else:
            error_message = "Unable to fetch weather data."
            return render(request,'weather.html',{'error_message':error_message})

    return render(request, 'weather.html')






