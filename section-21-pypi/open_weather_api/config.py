from open_weather_api.constants import CURRENT, FORECAST
class Config:

    def __init__(self, config):
        self.set_api_key(config['key'])
        self.set_units(config['units'])
        self.set_type(config['type'])
        self.set_lang(config['lang'])

    def set_api_key(self, api_key):
        if (api_key == '' or api_key == None):
            raise ValueError('Need API Key')
        self.__api_key = f'&appid={api_key}'

    def get_api_key(self):
        return self.__api_key
    
    def set_units(self, units):
        self.__units = '&units=metric' if (units == 'metric') else ''

    def get_units(self):
        return self.__units
    
    def set_lang(self, lang):
        self.__lang = '&lang=en' if (lang == '' or lang == None) else f'&lang={lang}'

    def get_lang(self):
        return self.__lang

    def set_type(self, type):
        if (type != CURRENT and type != FORECAST):
            raise ValueError('Need correct type (CURRENT or FORECAST)')
        self.__type = type

    def get_type(self):
        return self.__type
    