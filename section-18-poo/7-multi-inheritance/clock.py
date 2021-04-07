class Clock:

    def __init__(self, hour, minute, second):
        print("Clase Base - Clock")
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{}:{}".format(self.hour,
                                 self.minute,
                                 self.second)
