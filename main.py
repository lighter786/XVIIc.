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

    def remove_item(self, item_name):
            if item_name in self.items:
                del self.items[item_name]
                print(f"{item_name} удален из инвенторя")
            else:
                print(f"Предмета {item_name} нет в инвентаре")

    def Show_Inventory(self):
            if not self.items:
                return "Инвентарь пуст"
    
            print("Ваш инвентарь")
            for name, item in self.items.items():
                print(f"- {name} (Тип {item.item_type}, эффект {item.effect})")
            print("--" * 10)

class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Char_info(self):
        print(f"""Имя: {self.name} Возраст: {self.age}""")

class SpecificationСhar(Char):
    def __init__(self, name, age):
        super().__init__(name, age)#Bafs - Временные эффекты (health, skils, bafs)
        self.inventory = Inventory()
        self.point = 0 #Выполнено
        self.level = 0 #Выполнено 92%
        self.health = 100 #Выполнено 
        self.bafs = {}
        self.skills = {}
        
    def Level(self):#Уровень персонажа
        print("Ваш уровень повышен!")
        print(f"Ваш уровень: {self.level}")

    def LevelPoint(self):
        earned = randint(1, 3)
        self.point += earned
        print(f"Получено {earned} очков | Очки: {self.point}")

        need_point = (self.level + 1) * 3
        
        if self.point >= need_point:
            self.level += 1
            self.point -= need_point
            self.Level()
        
        next_point = (self.level + 1) * 3
        print(f"До следующего уровня {next_point - self.point} очков")

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

    def Use_Item(self, item_name):
        if item_name not in self.inventory.items:
            print(f"Предмета {item_name} нет в инвентаре")
            return

        item = self.inventory.items[item_name]

        if item.item_type == "heal":
            self.health = min(100, self.health + item.effect)
            print(f"Вы приняли {item.name} здоровье {self.health}")

            self.inventory.remove_item(item_name)
        else:
            print(f"Вы не знаете как использовать {item_name}")            

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