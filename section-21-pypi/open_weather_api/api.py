
from open_weather_api.config import Config
from open_weather_api.constants import URL

class Api(Config):

    def __init__(self, config):
        print('Api start')
        super().__init__(config)


    def get_url(self, find_params):
        '''
        Information to define URL
        ------------------------
        Use find_params => coordinates or location name\n
        metric or default system units\n
        language
        '''
        lang = self.get_lang()
        units = self.get_units()
        api_key = self.get_api_key()
        params = f'{find_params}{lang}{units}{api_key}'
        url = f'{URL}{self.get_type()}{params}'
        print(url)
        return url
