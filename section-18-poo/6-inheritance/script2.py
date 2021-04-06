from dog import Dog
from cat import Cat
from pig import Pig
dog = Dog("Txuri", "eueuej3", "Macho", "2020-06-06", "AVD/Ezozia 20")

dog.clean()
dog.eat()
dog.show_details()
dog.talk()
dog.run()
del dog

cat = Cat("Cosquillas", "---", "Hembra", "¿?", True)

cat.eat()
cat.show_details()
cat.talk()
cat.run()
cat.climb()
cat.jump()
del cat

pig = Pig("Babe", "739902020", "Hembra", "2021-01-15", True)

pig.eat()
pig.show_details()
pig.talk()
pig.run()
pig.take_sunny()
pig.investigate_environment()
del pig



