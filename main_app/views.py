from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
import geocoder
from django.contrib import messages


# Create your views here.

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def home(request):
    context = {}

    if request.method == 'POST':
        city = request.POST.get('city')
        place = city
        exact_place_founder = geocoder.location(place)
        lat = exact_place_founder.lat
        lng = exact_place_founder.lng

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=02176245d35573f9dc55f7db28075562"
        response = requests.get(url).json()

        print(response)
        context['result'] = f"{kelvin_to_celsius(response['main']['temp']):.2f}°"
        context['city'] = city
        context['feels_like'] = f"Feels Like: {kelvin_to_celsius(response['main']['feels_like']):.2f}°"
        context['humidity'] = f"Humidity: {response['main']['humidity']:.2f}%"

    return render(request, 'main.html', context)
