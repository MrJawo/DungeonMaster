import random
import knight_class
hero = knight_class.Hero("Orvar", "Riddare")
hero.add_knight()

def attack_val(hero):
    attack = hero.attack
    return attack

print(attack_val(hero))

def get_attack_val(hero_class):
    if hero_class == "Riddare":
        return 6
    elif hero_class == "Trollkarl":
        return 9
    elif hero_class == "Tjuv":
        return 5

def get_defend_val(hero_class):
    if hero_class == "Riddare":
        return 4
    elif hero_class == "Trollkarl":
        return 5
    elif hero_class == "Tjuv":
        return 7

def attack_func(get_attack_val):
    dice_rolls = 0
    sum_of_dice_rolls = 0
    while dice_rolls < get_attack_val:
        number = random.randint(1,6)
        sum_of_dice_rolls = sum_of_dice_rolls + number
    return sum_of_dice_rolls

