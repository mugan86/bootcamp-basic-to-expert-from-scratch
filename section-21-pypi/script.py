from open_weather_api.api import Api
from open_weather_api.constants import CURRENT, FORECAST
from open_weather_api.options.city import City
from open_weather_api.options.coordinates import Coordinates

config = dict(
    key='194f66064a427d3f0bcca212ab703736',
    units='metric',
    lang='es',
    type=FORECAST
)

karakate_weather = Coordinates(config, '43.1926324', '-2.4151716')

print('-------------------------')
print(karakate_weather.get_data())