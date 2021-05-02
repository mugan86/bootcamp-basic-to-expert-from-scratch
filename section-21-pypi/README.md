# Open Weather Map API Python Package
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Package that take current and forecast weather in select location.

Location options:
* By City
* By Geographic Location Coordinates.

## Install intructions

### Windows
```pip install mugan86-openwm-api```

### Linux / MacOSx
```pip3 install mugan86-openwm-api```

## Available Languages to take info

```
'af': 'Afrikaans',
'al': 'Albanian',
'ar': 'Arabic',
'az': 'Azerbaijani',
'bg': 'Bulgarian',
'ca': 'Catalan',
'cz': 'Czech',
'da': 'Danish',
'de': 'German',
'el': 'Greek',
'en': 'English',
'eu': 'Basque',
'fa': 'Persian (Farsi)',
'fi': 'Finnish',
'fr': 'French',
'gl': 'Galician',
'he': 'Hebrew',
'hi': 'Hindi',
'hr': 'Croatian',
'hu': 'Hungarian',
'id': 'Indonesian',
'it': 'Italian',
'ja': 'Japanese',
'kr': 'Korean',
'la': 'Latvian',
'lt': 'Lithuanian',
'mk': 'Macedonian',
'no': 'Norwegian',
'nl': 'Dutch',
'pl': 'Polish',
'pt': 'Portuguese',
'pt_br': 'Português Brasil',
'ro': 'Romanian',
'ru': 'Russian',
'sv': 'Swedish',
'sk': 'Slovak',
'sl': 'Slovenian',
'es': 'Spanish',
'sr': 'Serbian',
'th': 'Thai',
'tr': 'Turkish',
'uk': 'Ukrainian',
'vi': 'Vietnamese',
'zh_cn': 'Chinese Simplified',
'zhtw':  'Chinese Traditional',
'zu': 'Zulu'
```
## Use example

Create script file (For example: **script.py**)
### Take by city name
```
from open_weather_api.constants import CURRENT, FORECAST
from open_weather_api.options.city import City

# Configuration
config = dict(
    key='<api-key>',
    units='metric',      # metric
    lang='es',      # Select language from available language codes
    type=CURRENT    # (OR FORECAST)
)

city = City(config, "Bilbao")

result = city.get_data()

print(result)

```
Result
```
{'coord': {'lon': -2.9253, 'lat': 43.2627}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'muy nuboso', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 12.68, 'feels_like': 11.99, 'temp_min': 12.22, 'temp_max': 13.33, 'pressure': 1009, 'humidity': 76}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 310}, 'clouds': {'all': 75}, 'dt': 1619620260, 'sys': {'type': 1, 'id': 6395, 'country': 'ES', 'sunrise': 1619586540, 'sunset': 1619636945}, 'timezone': 7200, 'id': 3128026, 'name': 'Bilbao', 'cod': 200}
```
### Take by Location Geographic (Latitude / Longitude)
```
from open_weather_api.constants import CURRENT, FORECAST
from open_weather_api.options.coordinates import Coordinates

# Configuration
config = dict(
    key='<api-key>',
    units='m',      # metric
    lang='es',      # Select language from available language codes
    type=CURRENT    # (OR FORECAST)
)

city = Coordinates(config, '43.1736976', '-2.41297')

result = city.get_data()

print(result)

```
Result
```
{'coord': {'lon': -2.413, 'lat': 43.1737}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'nubes', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 12.18, 'feels_like': 11.93, 'temp_min': 8.89, 'temp_max': 13.89, 'pressure': 941, 'humidity': 95}, 'visibility': 10000, 'wind': {'speed': 2.34, 'deg': 346, 'gust': 3.21}, 'clouds': {'all': 100}, 'dt': 1619620423, 'sys': {'type': 3, 'id': 2007106, 'country': 'ES', 'sunrise': 1619586428, 'sunset': 1619636811}, 'timezone': 7200, 'id': 6358153, 'name': 'Soraluze / Placencia de las Armas', 'cod': 200}
```