print('OpenWeatherMap')
import pyowm
owm = pyowm.OWM('b9db482190ac899aac5a8959d781f106')
observation = owm.weather_at_place('Bataysk,ru')
weather = observation.get_weather()
location = observation.get_location()

translate = {'Bataysk':'Батайск'}

def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'
    if 10 <= weather.get_clouds() <= 20:
        return 'немного облачная'
    if 20 <= weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 <= weather.get_clouds() <= 100:
        return 'мрачная'

print('Погода в городе ' + translate[location.get_name()] +
 ' ' + WhatIsCloudness() + ', температура ' +
 str(weather.get_temperature('celsius')['temp']) +
' градусов цельсия' + ' скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с.')