import random
import classes
import main
from time import sleep


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
        character.initiative_sum()
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

def hero_ability(hero):
    if hero.hero_class == "Trollkarl":
        wizard_num = 80
        r1 = random.randint(1, 100)
        if wizard_num >= r1:
            return True
        else:
            return False
    if hero.hero_class == "Tjuv":
        thief_num = 25
        r2 = random.randint(1, 100)
        if thief_num >= r2:
            return True
        else:
            return False


def attack_func(attacker, defender, hero):
    attack = dice(attacker.attack)
    defend = dice(defender.agility)

    main.clear_screen()
    main.print_hero_stats(hero)
    print(f"\n{attacker.name} attackerar {defender.name}!")
    delay_in_fight()

    if attack > defend:
        defender.resistance -= 1
        print(f"\nAttack lyckades! {defender.name} har {defender.resistance} liv kvar.")
        input('\n-- Tyck på valfri tangent för att fortsätta --')

        if attacker.name == hero.name:
            if attacker.hero_class == "Tjuv":
                ability_success = hero_ability(attacker)
                if ability_success:
                    print('\nKritisk träff! Dubbel skada utdelad')
                    input('\n-- Tyck på valfri tangent för att fortsätta --')
                    defender.resistance -= 1
    else:
        print(f"\nAttack misslyckades!")
        input('\n-- Tyck på valfri tangent för att fortsätta --')


def dead_message(hero):
    while True:
        main.clear_screen()

        print(f"\n{hero.name} har dött.")
        print("Du samlade på dig ", hero.points_current_game, " poäng.")
        hero.update_total_points()

        print("\n[1] - Main menu\n"
                  "[2] - Avsluta spelet")
        choice = input("\nSkriv in ditt val: ")

        if choice == "1":
            main.main_menu()
        elif choice == "2":
            exit()
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på valfri tangent för att fortsätta --')





def delay_in_fight():

    print('\n.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)


def did_monster_die(monster, room, game_board, hero, grid_size, room_list):
    if monster.resistance == 0:
        print(f"\n{monster.name} dog!")
        monster.died()
        input('\n-- Tryck på valfri knapp för att fortsätta --')


def check_for_living_monsters(room, game_board, hero, grid_size, room_list):
    for monster in room.monster_list:
        if monster.resistance > 0:
            return True
        return False


def start_fight_message(monster_list):

    print("\n[Dungeon Run]")
    print(f"\nDu gick in i ett rum med {len(monster_list)} monster:")
    i = 1
    for monster in monster_list:
        print(f"{i}. {monster.name}")
        i += 1
    print('\nBesegra dessa för att eventuellt hitta en skatt!')
    print('Du kommer alltid att attackera monstret som är först i listan.\n'
          'När det monstret är besegrat kommer din uppmärksamhet att \n'
          'riktas mot nästa monster i listan.')
    input('\n-- Tryck på valfri knapp för att fortsätta --')


def monster_attacks(knight_ability, creature, hero):

    if not knight_ability:
        attack_func(creature, hero, hero)
        if hero.resistance == 0:
            dead_message(hero)
        return False
    else:
        print(f"\n{creature.name} attackerar {hero.name}!")
        delay_in_fight()
        main.clear_screen()
        main.print_hero_stats(hero)
        print(f"\n{hero.name} använder sköldblock och ignorerade attacken!")
        input('\n-- Tryck på valfri knapp för att fortsätta --')
        return False


def fight(hero, grid_size, game_board, room_list, room):

    main.clear_screen()

    knight_ability = False
    if hero.hero_class == "Riddare":
        knight_ability = True

    monster_list = room.monster_list
    start_fight_message(monster_list)
    creature_list = monster_list.copy()
    creature_list.append(hero)
    creature_list = sort_turn_list(creature_list)
    current_monster = 0

    print("\nSpelordningen följer:\n")
    i = 1
    for creature in creature_list:
        print(f"{i}. {creature.name}")

    input('\n-- Tryck på valfri knapp för att fortsätta --')

    while True:
        for creature in creature_list:
            if creature.is_alive:
                main.clear_screen()
                main.print_hero_stats(hero)

                if creature.name == hero.name:
                    while True:
                        print(f"\n-{hero.name}s tur-\n\n"
                              f"[1] - Attackera\n"
                              "[2] - Pröva att fly")

                        menu_choice = input("\nSkriv in ditt val: ")
                        if menu_choice == "1":

                            monster = monster_list[current_monster]
                            if monster.resistance == 0:

                                try:
                                    current_monster += 1
                                    monster = monster_list[current_monster]
                                except IndexError:
                                    pass

                            attack_func(hero, monster, hero)
                            did_monster_die(monster, room, game_board, hero, grid_size, room_list)
                            living_monster_remains = check_for_living_monsters(room, game_board, hero, grid_size, room_list)

                            if not living_monster_remains:
                                main.clear_screen()
                                room.monster_list = []
                                main.print_board(game_board, hero)
                                print('\nAlla monster besegrade!')

                                check_for_treasures(room)
                                main.print_board(game_board, hero)
                                main.walk_on_board(hero, grid_size, game_board, room_list)
                            break

                        elif menu_choice == "2":
                            pass
                        else:
                            print("\n-- Felaktig input, ange en siffra från menyn. --")
                            input('-- Tyck på valfri tangent för att fortsätta --')
                else:
                    knight_ability = monster_attacks(knight_ability, creature, hero)


def check_for_treasures(room):
    if len(room.treasure_list) > 0:
        print('Du hittade skatter i rummet:\n')

        i = 0
        for treasure in room.treasure_list:
            print(f"{treasure[0]}")
            i += treasure[1]

        print(f'\nTotalt värde: {i}')
        print('Skatten är tillagd i din ryggsäck')
        room.treasure_list = []
        room.set_room_symbol()
    else:
        print('\nInga skatter i rummet')


def check_for_monsters(hero, grid_size, game_board, room_list, room):
    if len(room.monster_list) > 0:
        fight(hero, grid_size, game_board, room_list, room)
    else:
        print('\nInga monster i rummet')


def undiscovered_room(room, hero, room_list, game_board, grid_size):

    check_for_monsters(hero, grid_size, game_board, room_list, room)
    check_for_treasures(room)


def check_room(coordinates, room_list, hero, game_board, start_coordinates, grid_size):

    for room in room_list:
        if room.coordinates == coordinates:
            if room.symbol == "[ ]":
                undiscovered_room(room, hero, room_list, game_board, grid_size)
            elif room.symbol == "[O]":
                exit_to_menu = main.exit_map(game_board, (start_coordinates[0],start_coordinates[1]))
                if exit_to_menu:
                    main.main_menu()