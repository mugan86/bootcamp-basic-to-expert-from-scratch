from calendar import Calendar
from clock import Clock

class DigitalClock(Clock, Calendar):

    def __init__(self, hour, minute, second, day, month, year):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, day, month, year)
        print("Clase Hija - DigitalClock")

    def get_data(self):
        return Calendar.__str__(self)
    
    def get_hour(self):
        return Clock.__str__(self)

    def __str__(self):
        return self.get_hour() + " " + self.get_data()