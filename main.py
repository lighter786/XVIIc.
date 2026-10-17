class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Char_info(self):
        print(f"""Имя: {self.name} Возраст: {self.age}""")


class SpecificationСhar(Char):
    def __init__(self, name, age):#Bafs - Временные эффекты (health, skils, bafs)
        super().__init__(name, age)
        self.level = 0
        self.health = 100
        self.skils = {}
        self.bafs = {}
        self.point = 0

    def Level(self):#Уровень персонажа
        print("Ваш уровень повышен!")
        print(f"Ваш уровень: {self.level}")