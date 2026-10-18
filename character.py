from random import randint
from items import Item, Inventory
from skills import Skills
from buffs import Buff

class Char:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Char_info(self):
        print(f"""Имя: {self.name} Возраст: {self.age}""")

class SpecificationСhar(Char):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.inventory = Inventory() #Выполнено
        self.skills = Skills() #Выполнено
        self.bafs = {}
        self.point = 0 #Выполнено
        self.level = 0 #Выполнено
        self.health = 100 #Выполнено
        
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

    def Add_Buffs(self, buff):
            self.bafs[buff.name] = buff
            print(f"Наложен бафф {buff.name} на {buff.duration} ходов")
    
    def Tick_Buffs(self):
        if not self.bafs:
            return

        for buff_name in list(self.bafs.keys()):
            buff = self.bafs[buff_name]
            buff.duration -= 1

            if buff.duration <= 0:
                del self.bafs[buff_name]
                print(f"Бафф {buff_name} кочнился!")
            else:
                print(f"Бафф {buff_name} продлится еще {buff.duration} хода")
    
    def Show_Baffs(self):
        if not self.bafs:
            print("У вас нет активных баффов")
            return

        print("Активные баффы")
        for name, buff in self.bafs.items():
            print(f"{name} (Эффект:{buff.stat_modifier} продлится еще {buff.duration} ходов")