
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('be727924bed4a3fd6611f93cefce59a1')
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print('Description:',w.detailed_status)
print('Temperature: ',w.temperature('celsius'),'°C')
print('Humidity: ',w.humidity)
print(w.rain)
print('clouds: ',w.clouds)
print('Wind: ',w.wind())





