from digital_clock import DigitalClock
complete_clock = DigitalClock(8, 30, 54, 7, 4, 2021)

print("Hora: {}".format(complete_clock.get_hour()))
print("Fecha: {}".format(complete_clock.get_data()))
print("Hora / Fecha: {}".format(complete_clock))

print(DigitalClock.__mro__)