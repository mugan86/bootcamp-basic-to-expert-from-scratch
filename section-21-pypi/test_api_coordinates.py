from unittest import main, TestCase, mock
from open_weather_api.constants import CURRENT
from open_weather_api.options.coordinates import Coordinates

"""
Estamos testeando lo correspondiente a la request de JSONPlaceHolder Typicode
el apartado de commentarios "comments" que hemos añadido al módulo "blog" con "comments"
como función
"""


class TestCoordinates(TestCase):
    def test_check_is_add_correct_init(self):
        config = dict(
            key='194f66064a427d3f0bcca212ab703736',
            units='metric',
            lang='es',
            type=CURRENT
        )
        coordinates = Coordinates(config, 43.1994987, -2.2879428)
        print(coordinates.get_coordinates())
        self.assertEqual(type(coordinates.get_coordinates()), str)
        self.assertEqual(
            'lat=43.1994987&lon=-2.2879428', coordinates.get_coordinates())
        self.assertEqual(type(coordinates.get_api_key()), str)
        self.assertEqual(
            '&appid=194f66064a427d3f0bcca212ab703736', coordinates.get_api_key())
        self.assertEqual(type(coordinates.get_lang()), str)
        self.assertEqual(
            '&lang=es', coordinates.get_lang())
        self.assertEqual(type(coordinates.get_units()), str)
        self.assertEqual(type(coordinates.get_type()), str)
        self.assertEqual(coordinates.get_type(), CURRENT)

    @mock.patch("open_weather_api.options.coordinates.Coordinates")
    def test_coordinates_ok(self, mock_response):
        coordinates = mock_response()
        coordinates.get_data.return_value = {'coord': {'lon': -2.2879, 'lat': 43.1995}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'nubes', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 15.23, 'feels_like': 14.71, 'temp_min': 13.92, 'temp_max': 18.97, 'pressure': 1017, 'humidity': 73, 'sea_level': 1017, 'grnd_level': 917}, 'visibility': 10000, 'wind': {
            'speed': 1.67, 'deg': 145, 'gust': 2.09}, 'clouds': {'all': 94}, 'dt': 1634486404, 'sys': {'type': 2, 'id': 2001916, 'country': 'ES', 'sunrise': 1634451908, 'sunset': 1634491410}, 'timezone': 7200, 'id': 6325251, 'name': 'Santa Kurutz', 'cod': 200}
        response = coordinates.get_data()
        print(response)
        self.assertIsNotNone(response)
        self.assertEqual(type(response["cod"]), int)
        self.assertEqual(response["cod"], 200)


if __name__ == "__main__":
    main()
