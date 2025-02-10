import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url).json()

        if response['cod'] == 200:
            weather_data = {
                'city': response['name'],
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }

    return render(request, 'weather/weather.html', {'weather': weather_data})
