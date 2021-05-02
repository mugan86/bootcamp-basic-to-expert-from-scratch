

from open_weather_api.api import Api


class Coordinates(Api):

    def __init__(self, config = None, lat = None , lon = None):
        if (lat == '' or lat == None or lon == '' or lon == None):
            raise ValueError('Need location coordinates to take weather data')
        if (config == None):
            raise ValueError('Need config data')
        self.set_coordinates(lat, lon)
        # especificar el paráemtro de búsqueda el lugar
        super().__init__(config)

    def set_coordinates(self, lat, lon):
        self.__location = f'lat={lat}&lon={lon}'

    def get_coordinates(self):
        return self.__location

    def get_data(self):
        return super().get_data(self.get_coordinates())