from dog import Dog
from cat import Cat
from pig import Pig
dog = Dog("AVD/Ezozia 20")
dog.name = "Txuri"
dog.chip_number = "eueuej3"
dog.genre = "Macho"
dog.day_birth = "2020-06-06"

dog.clean()
dog.eat()
dog.show_details()
dog.talk()
dog.run()
del dog

cat = Cat(True)
cat.name = "Cosquillas"
cat.chip_number = "---"
cat.genre = "Hembra"
cat.day_birth = "¿?"

cat.eat()
cat.show_details()
cat.talk()
cat.run()
cat.climb()
cat.jump()
del cat

pig = Pig(True)
pig.name = "Babe"
pig.chip_number = "739902020"
pig.genre = "Hembra"
pig.day_birth = "2021-01-15"

pig.eat()
pig.show_details()
pig.talk()
pig.run()
pig.take_sunny()
pig.investigate_environment()
del pig



