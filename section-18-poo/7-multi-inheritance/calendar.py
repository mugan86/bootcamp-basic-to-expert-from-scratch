class Calendar:

    def __init__(self, day, month, year):
        print("Clase Base - Calendar")
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}-{}-{}".format(self.day,
                                 self.month,
                                 self.year)