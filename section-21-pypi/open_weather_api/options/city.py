

from open_weather_api.api import Api


class City(Api):

    def __init__(self, config = None, city = None):
        if (city == '' or city == None):
            raise ValueError('Need city name to take weather data')
        if (config == None):
            raise ValueError('Need config data')
        self.set_city(city)
        # especificar el paráemtro de búsqueda el lugar
        super().__init__(config)

    def set_city(self, city):
        self.__name = f'q={city}'

    def get_city(self):
        return self.__name

    def get_data(self):
        return super().get_data(self.get_city())