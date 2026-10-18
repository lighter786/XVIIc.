from random import choice

class Skills:
    def __init__(self):
        self.skils_for_add = ["Лесоруб", "Шахтер", "Рыбак", "Кузнец"]
        self.skills = {}

    def AddSkills(self):
        if not self.skils_for_add:
            print("Извесые навыки изучены")
            return

        new_skill = choice(self.skils_for_add)

        if new_skill in self.skills:
            self.skills[new_skill] += 1
            print(f"Навык {new_skill} изучен ранее | Навык повышен до {self.skills[new_skill]} уровня!")
        else:
            self.skills[new_skill] = 1
            print(f"Получен навык '{new_skill}' | Уровень навыка: 1")
    
    def ShowSkills(self):
        if not self.skills:
            print("Навыки не изучены")
            return

        print('=' * 10, "Навыки", '=' * 10)
        for name, level in self.skills.items():
            print(f"- {name} | Уровень навыка: {level})")
        print("--" * 25)