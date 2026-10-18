from random import *

class Item:
    def __init__(self, name, item_type, effect = 0):
        self.name = name
        self.item_type = item_type
        self.effect = effect

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item
        print(f"{item.name} добвален в инвентарь")

class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Char_info(self):
        print(f"""Имя: {self.name} Возраст: {self.age}""")

class SpecificationСhar(Char):
    def __init__(self, name, age):
        super().__init__(name, age)#Bafs - Временные эффекты (health, skils, bafs)
        self.point = 0 #Выполнено
        self.level = 0 #Выполнено 92%
        self.health = 100 #Выполнено 
        self.bafs = {}
        self.skills = {}
        
    def Level(self):#Уровень персонажа
        print("Ваш уровень повышен!")
        print(f"Ваш уровень: {self.level}")

    def LevelPoint(self):
        pass

    def Damage(self):
        self.health -= randint(0, 99) #Функция отвечающая за изменение здоровья

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
        self.skils_for_add = ["Лесоруб"]
        self.skils = []

    def AddSkills(self):
        self.random_skills = choice(self.skils_for_add)
        if self.skils_for_add in self.skils:
            print(f"Навык {self.random_skills} ужеизучен!")
        else:
            print(f"Добавлен новый навык {self.random_skills}| 1ур.")

    def ShowSkills(self):
        return self.skils