from open_weather_api.constants import CURRENT
from open_weather_api.options.coordinates import Coordinates

config = dict(
    key='194f66064a427d3f0bcca212ab703736',
    units='metric',
    lang='es',
    type=CURRENT
)

karakate_weather = Coordinates(config, 43.1994987,-2.2879428)

print('-------------------------')
print(karakate_weather.get_data())