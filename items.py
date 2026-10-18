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