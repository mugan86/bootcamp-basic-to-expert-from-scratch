from unittest import main, TestCase, mock
from open_weather_api.constants import CURRENT
from open_weather_api.options.city import City

"""
Estamos testeando lo correspondiente a la request de JSONPlaceHolder Typicode
el apartado de commentarios "comments" que hemos añadido al módulo "blog" con "comments"
como función
"""


class TestCity(TestCase):
    def test_check_is_add_correct_init(self):
        config = dict(
            key='AQUI_NUESTRA_API_KEY',
            units='metric',
            lang='es',
            type=CURRENT
        )
        citys = City(config, "Barcelona")
        """print(citys.get_citys())
        self.assertEqual(type(citys.get_citys()), str)
        self.assertEqual(type(citys.get_api_key()), str)
        self.assertEqual(type(citys.get_lang()), str)
        self.assertEqual(type(citys.get_units()), str)
        self.assertEqual(type(citys.get_type()), str)
        self.assertEqual(citys.get_type(), CURRENT)"""
        print(citys.get_data())

    @mock.patch("open_weather_api.options.city.City")
    def test_citys_ok(self, mock_response):
        citys = mock_response()
        citys.get_data.return_value = {'coord': {'lon': 2.159, 'lat': 41.3888}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'muy nuboso', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 20.47, 'feels_like': 20.61, 'temp_min': 19.15, 'temp_max': 22.89, 'pressure': 1018, 'humidity': 78}, 'visibility': 10000, 'wind': {
            'speed': 0.89, 'deg': 60, 'gust': 2.24}, 'clouds': {'all': 82}, 'dt': 1634486406, 'sys': {'type': 2, 'id': 18549, 'country': 'ES', 'sunrise': 1634450716, 'sunset': 1634490467}, 'timezone': 7200, 'id': 3128760, 'name': 'Barcelona', 'cod': 200}
        response = citys.get_data()
        print(response)
        self.assertIsNotNone(response)
        self.assertEqual(type(response["cod"]), int)
        self.assertEqual(response["cod"], 200)


if __name__ == "__main__":
    main()
