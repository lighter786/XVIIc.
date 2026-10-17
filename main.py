from random import randint

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
        self.level = 0 #Выполнено 92%
        self.health = 100 #Выполнено 
        self.bafs = {}
        

    def Level(self):#Уровень персонажа
        print("Ваш уровень повышен!")
        print(f"Ваш уровень: {self.level}")

    def LevelPoint(self):
            self.point += randint(1, 5)
            if self.point > 2:
                self.level += 1
                self.Level()

    def Damage(self):
        self.health -= 2 #Функция отвечающая за изменение здоровья

    def Health(self): #Функция здоровья
        if self.health == 100:
            print("Уровень здоровья максимальный!")
        elif 20 <= self.health <= 99:
            print(f"Уровень здоровья {self.health}")
        else:
            print("Ваше здоровье критически низкое!")
            print(f"Уровень здоровья {self.health}")

    def Eat(self):
        self.health += randint(7, 12)
        if self.health >= 100:
            self.health = 100
            print("Ваше здоровье восстановлено!")
            print(f"Уровень здоровья {self.health}")
        else:
            print(f"Уровень здоровья {self.health}")

class Skills:
    def __init__(self):
        self.skils = {}