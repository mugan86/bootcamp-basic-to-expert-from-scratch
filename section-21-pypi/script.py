from open_weather_api.api import Api
from open_weather_api.constants import CURRENT


config = dict(
    key='194f66064a427d3f0bcca212ab703736',
    units='metric',
    lang='es',
    type=CURRENT
)

configuration = Api(config)

print(configuration.get_api_key())
print(configuration.get_lang())
print(configuration.get_units())
print(configuration.get_type())
print(configuration.get_url('lat=43.1926929&lon=-2.4153159'))