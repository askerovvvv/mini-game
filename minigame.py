
import random

class Hero:
    level = 0
    def __init__(self, id, team):
        self.id = id
        self.team = team
        
    def level_up(self):
        self.level += 1

class Soldier:
    def __init__(self, id, team):
        self.id = id
        self.team = team

    def __repr__(self) -> str: # ссылка на обьекта
        return f"{self.id} {self.team}" 

    def go_hero(self, hero):
        return f"Иду за {hero}"

hero1 = Hero(1, "Blue")
hero2 = Hero(2, "Red")

obj1 = [] # Солдаты одной команды
obj2 = [] # Солдаты другой команды

for i in range(10):
    team = random.choice(("Red", "Blue"))
    if team == "Blue":
        obj1.append(Soldier(random.randint(1,1000), team))
    
    else:
        obj2.append(Soldier(random.randint(1,1000), team))


if len(obj1) < len(obj2):
    print(f"первый герой победил у него было {len(obj2)} и команда называлась {hero2.team}")
    hero1.level_up()
elif len(obj1) > len(obj2):
    print(f"первый герой победил у него было {len(obj1)} и команда называлась {hero1.team}")
    hero2.level_up()
else:
    print("Ничья")

print(obj1[0].go_hero(hero1.id))
print(obj1)

