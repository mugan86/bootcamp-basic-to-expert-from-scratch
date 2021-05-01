from open_weather_api.constants import CURRENT
from open_weather_api.config import Config

config = dict(
    key='194f66064a427d3f0bcca212ab703736',
    units='metric',
    lang='es',
    type=CURRENT
)

configuration = Config(config)

print(configuration.get_api_key())
print(configuration.get_lang())
print(configuration.get_units())
print(configuration.get_type())