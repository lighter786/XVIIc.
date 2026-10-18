from character import SpecificationСhar
from items import Item
from buffs import Buff

def main():
    print("=== СОЗДАНИЕ ПЕРСОНАЖА ===")
    hero = SpecificationСhar("Роберт", 24)
    hero.Char_info()

    print("\n=== ТЕСТ УРОВНЕЙ ===")
    # Вызываем 5 раз, чтобы набрать очки и повысить уровень
    for _ in range(5):
        hero.LevelPoint()

    print("\n=== ТЕСТ ЗДОРОВЬЯ И ЕДЫ ===")
    # Наносим урон, смотрим здоровье, лечимся едой
    hero.Damage()
    hero.Health()
    hero.Eat()

    print("\n=== ТЕСТ ИНВЕНТАРЯ ===")
    # Создаем предметы
    potion = Item("Зелье здоровья", "heal", 30)
    sword = Item("Стальной меч", "weapon", 15)
    
    # Кладем в рюкзак
    hero.inventory.add_item(potion)
    hero.inventory.add_item(sword)
    
    # Смотрим, что внутри
    hero.inventory.Show_Inventory()
    
    # Пьем зелье (должно исчезнуть из рюкзака)
    hero.Use_Item("Зелье здоровья")
    
    # Пытаемся выпить еще раз (должна быть ошибка "нет в инвентаре")
    hero.Use_Item("Зелье здоровья")
    
    # Смотрим инвентарь снова (должен остаться только меч)
    hero.inventory.Show_Inventory()

    print("\n=== ТЕСТ НАВЫКОВ ===")
    # Изучаем навыки (вызываем несколько раз, чтобы сработал рандом)
    hero.skills.AddSkills()
    hero.skills.AddSkills()
    hero.skills.AddSkills()
    
    # Смотрим список навыков
    hero.skills.ShowSkills()

    print("\n=== ТЕСТ БАФФОВ ===")
    # Создаем бафф "Ярость" на 2 хода
    rage_buff = Buff("Ярость", 2, 10)
    
    # Накладываем на героя
    hero.Add_Buffs(rage_buff)
    hero.Show_Baffs()
    
    # Имитируем ход 1
    print("\n--- Прошел 1 ход ---")
    hero.Tick_Buffs()
    
    # Имитируем ход 2 (бафф должен исчезнуть)
    print("\n--- Прошел 2 ход ---")
    hero.Tick_Buffs()
    
    # Проверяем, что баффов больше нет
    print("\n--- Проверка после ходов ---")
    hero.Show_Baffs()

main()