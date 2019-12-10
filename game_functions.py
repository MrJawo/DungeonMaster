import random
import classes


def number_sum(int_list):
    """Returns the sum of integers from a list"""

    list_sum = 0
    for number in int_list:
        list_sum += number

    return list_sum


def treasure_sum(treasure_list):
    """Returns the sum of first element in tuple"""

    treasure_sum = 0
    for treasure in treasure_list:
        treasure_sum += treasure[1]
    return treasure_sum


def generate_treasure(chance, treasure_type, treasure_value, random_int):
    """Returns the a tupl of treasure type and its value if it spawns"""

    if random_int <= chance:
        treasure_tuple = (treasure_type, treasure_value)
        return treasure_tuple
    else:
        return 0


def get_treasures():
    """Returns an int with sum of all found treasures"""

    treasure_list = [generate_treasure(40, 'Lösa slantar: 2', 2, random.randint(1, 100)),
                     generate_treasure(20, 'Pengapung: 6', 6, random.randint(1, 100)),
                     generate_treasure(15, 'Gukdsmycke: 10', 10, random.randint(1, 100)),
                     generate_treasure(10, 'Ädelsten: 14', 14, random.randint(1, 100)),
                     generate_treasure(5, 'Liten skattkista: 20', 20, random.randint(1, 100))]

    treasure_list = clean_list(treasure_list)
    return treasure_list


def generate_monster(spawn_rate, monster_type, percent):
    """Creates a monster instance based of monster type"""

    if percent <= spawn_rate:
        if monster_type == "Jättespindel":
            monster = classes.Monster()
            monster.add_giant_spider()
            return monster
        elif monster_type == "Skelett":
            monster = classes.Monster()
            monster.add_skeleton()
            return monster
        elif monster_type == "Orc":
            monster = classes.Monster()
            monster.add_orc()
            return monster
        elif monster_type == "Troll":
            monster = classes.Monster()
            monster.add_troll()

            return monster
    else:
        return 0


def clean_list(element_list):
    """Returns a list stripped of zeros"""

    cleansed_list = []
    for element in element_list:
        if element != 0:
            cleansed_list.append(element)
    return cleansed_list


def get_monster_list():
    """Generates a list with potential monsters based on their commonness"""

    monster_list = [generate_monster(20, 'Jättespindel', random.randint(1, 100)),
                    generate_monster(15, 'Skelett', random.randint(1, 100)),
                    generate_monster(10, 'Orc', random.randint(1, 100)),
                    generate_monster(5, 'Troll', random.randint(1, 100))]

    monster_list = clean_list(monster_list)
    return monster_list


def bubble_sort(character_list):
    """Sorts objects by highest initiative dice throws"""

    tuple_list = []
    for character in character_list:
        tuple_list.append((character, character.initiative_dice_sum))

    length = len(character_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if tuple_list[j][1] < tuple_list[j + 1][1]:
                tuple_list[j], tuple_list[j + 1] = tuple_list[j + 1], tuple_list[j]

    return tuple_list


def sort_turn_list(character_list):
    """Returns a list of characters in right turn order"""

    sorted_list = []
    tuple_list = bubble_sort(character_list)
    for element in tuple_list:
        sorted_list.append(element[0])

    return sorted_list


def dice(number_of_dices):
    """Generates a number between 1 and 6 the selected amount of times and returns the sum"""

    list_of_numbers = []
    for i in range(number_of_dices):
        list_of_numbers.append(random.randint(1, 6))
    sum_of_dices = number_sum(list_of_numbers)
    return sum_of_dices

def attack_func(attacker, defender):
    attack = dice(attacker.attack)
    defend = dice(defender.agility)
    if attack > defend:
        defender.resistance -= 1
        print("Attack lyckades")
    else:
        print("Attack misslyckades")