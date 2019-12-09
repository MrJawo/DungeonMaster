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


def generate_monster(chance, monster_type, random_int):
    """Creates a monster instance based of monster type"""

    if random_int <= chance:
        if monster_type == "Jättespindel":
            monster = classes.Creatures()
            monster.spider_initiation()
            return monster
        elif monster_type == "Skelett":
            monster = classes.Creatures()
            monster.skeleton_initiation()
            return monster
        elif monster_type == "Orc":
            monster = classes.Creatures()
            monster.orc_initiation()
            return monster
        elif monster_type == "Troll":
            monster = classes.Creatures()
            monster.troll_initiation()
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


def thief_special_ability(defender):
    """Checks if thief gets another hit on enemy"""

    percent = random.randint(1, 100)
    if percent <= 25:
        defender.lost_health_point()
        return True
    else:
        return False


def attack(attacker, defender, hero):
    """Function for attack"""

    attack_value = dice(attacker.attack)
    defend_value = dice(defender.agility)

    if defender == hero and hero.hero_class == "Knight" and hero.special_ability:
        print('\nSköldblock! Din hjälte skadade sig inte denna runda.')
        hero.special_ability = False
    else:
        if attack_value > defend_value:
            defender.lost_health_point()
            if attacker.hero_class == "Thief":
                if thief_special_ability(defender):
                    print('\nKritisk träff! En extra skada utdelat.')
                else:
                    print('\nKritisk träff missade.')
        else:
            print(f"\n{attacker.name}s attack missade {defender.name}.")


def print_character_turns(character_list):
    """Prints the correct turn order"""

    i = 1
    for character in character_list:
        print('\nTurordningen för denna strid är:')
        print(f"{i}. {character.name}")


def menu_choice_attack(monster_list, hero):
    """Handles fight choice in battle"""

    attack(hero, monster_list[0], hero)
    current_monster = monster_list[0]
    if current_monster.resistance == 0:
        print(f"{current_monster.name} dog!")
        monster_list.remove(current_monster)
        if len(monster_list) > 0:
            print(f"\nNästa monster att döda: {monster_list[0]}")


def menu_choice_flee(hero):
    """Handles escape choice in battle"""

    escape_chance = hero.agility * 10
    if hero.hero_class == "Wizard":
        escape_chance = 80
        print('\nDu använder ljussken och får 80% chans att lyckas fly.')
    random_number = random.randint(1, 100)
    if escape_chance >= random_number:
        # TODO Escape scenario
        pass


def menu_choice_battle(choice, monster_list, hero):
    """Directs user to right function depending on choice"""

    if choice == 1:
        menu_choice_attack(monster_list, hero)
    else:
        menu_choice_flee(hero)


def battle(hero, character_list):
    """Battle function"""

    monster_list = character_list
    character_list.append(hero)

    for character in character_list:
        character.throw_initiative_dice()

    character_list = sort_turn_list(character_list)

    for monster in monster_list:
        monster.throw_initiative_dice()

    monster_list = sort_turn_list(monster_list)

    while True:
        if hero.resistance == 0:
            # TODO Handle hero death scenario
            if hero.hero_class == "Knight":
                hero.special_ability = True
        if len(monster_list) == 0:
            # TODO Handle won battle scenario
            if hero.hero_class == "Knight":
                hero.special_ability = True

        for character in character_list:
            if character.name == hero.name:
                print('\nStriden har börjat! Vad vill du göra?')
                print(f"\n[1] - Attackera"
                      f"\n[2] - Försök att fly")
                choice = input('\nSkriv in ditt val: ')
                menu_choice_battle(choice, monster_list, hero)

            else:
                for monster in monster_list:
                    attack(monster, hero, hero)


def enter_room_event(hero, start_coordinates, room):
    """Function that runs every time the player enters a room"""

    # TODO make function that gets coordinates for room
    coordinates = room.coordinates
    hero.update_player_coordinates(coordinates)

    if len(room.monster_list) > 0:

        character_list = room.monster_list
        battle(hero, character_list)

    else:
        sum_of_treasure = treasure_sum(room.treasure_list)
        if sum_of_treasure > 0:
            hero.map_treasure += treasure
            print("\nDu plockade upp skatten!")
        else:
            print("\n Inga skatter hittades i rummet.")

    # TODO Implement exit function
    if coordinates == start_coordinates:
        # If character stands on start position
        pass

