class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Char_info(self):
        print(f"""Имя: {self.name} Возраст: {self.age}""")

class SpecificationСhar(Char):
    def __init__(self, name, age):#Bafs - Временные эффекты (health, skils, bafs)
        super().__init__(name, age)
        self.point = 0 #Выполнено
        self.level = 0 #Выполнено
        self.health = 100
        self.skils = {}
        self.bafs = {}
        

    def Level(self):#Уровень персонажа
        print("Ваш уровень повышен!")
        print(f"Ваш уровень: {self.level}")

    def LevelPoint(self):
            self.point += 3
            if self.point > 2:
                self.level += 1
                self.Level()

    def Damage(self):
        self.health -= int() #Функция отвечающая за изменение здоровья