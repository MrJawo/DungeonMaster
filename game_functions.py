import random
import classes
import main
import time


def number_sum(int_list):
    """Returns the sum of integers from a list"""

    list_sum = 0
    for number in int_list:
        list_sum += number

    return list_sum


def treasure_sum(treasure_list):
    """Returns the sum of first element in tuple"""

    t_sum = 0
    for treasure in treasure_list:
        t_sum += treasure[1]
    return t_sum


def generate_treasure(chance, treasure_type, treasure_value, random_int):
    """Returns the a tuple of treasure type and its value if it spawns"""

    if random_int <= chance:
        treasure_tuple = (treasure_type, treasure_value)
        return treasure_tuple
    else:
        return 0


def get_treasures():
    """Returns an int with sum of all found treasures"""

    treasure_list = [generate_treasure(40, 'Lösa slantar: 2', 2, random.randint(1, 100)),
                     generate_treasure(20, 'Pengapung: 6', 6, random.randint(1, 100)),
                     generate_treasure(15, 'Guldsmycke: 10', 10, random.randint(1, 100)),
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


def bubble_sort(character_list, tuple_list):
    """Sorts objects by highest initiative dice throws"""

    length = len(character_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if tuple_list[j][1] < tuple_list[j + 1][1]:
                tuple_list[j], tuple_list[j + 1] = tuple_list[j + 1], tuple_list[j]

    return tuple_list


def strip_tuple_list(tuple_list):
    """Strips tuple of second element"""

    sorted_list = []
    for element in tuple_list:
        sorted_list.append(element[0])

    return sorted_list


def sort_turn_list(character_list):
    """Returns a list of characters in right turn order"""

    tuple_list = []
    for character in character_list:
        character.initiative_sum()
        tuple_list.append((character, character.initiative_dice_sum))
    tuple_list = bubble_sort(character_list, tuple_list)

    return strip_tuple_list(tuple_list)


def dice(number_of_dices):
    """Generates a number between 1 and 6 the selected amount of times and returns the sum"""

    list_of_numbers = []
    for i in range(number_of_dices):
        list_of_numbers.append(random.randint(1, 6))
    sum_of_dices = number_sum(list_of_numbers)
    return sum_of_dices


def hero_ability(hero):
    """Returns true or false if special ability works or not"""

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
    """Attack function for all creatures"""

    attack = dice(attacker.attack)
    defend = dice(defender.agility)

    print(f"\n{attacker.name} attackerar {defender.name}!")
    delay_in_fight()

    if attack > defend:
        defender.resistance -= 1
        print(f"\nAttack lyckades! {defender.name} har {defender.resistance} liv kvar.")
        if hero.ai:
            time.sleep(2.5)
        else:
            input('\n-- Tyck på enter för att fortsätta --')

        if attacker.name == hero.name:
            if attacker.hero_class == "Tjuv":
                ability_success = hero_ability(attacker)
                if ability_success and defender.resistance > 0:
                    defender.resistance -= 1
                    print(f'\nKritisk träff! Dubbel skada utdelad, {defender.name} har {defender.resistance} liv kvar.')
                    if hero.ai:
                        time.sleep(2.5)
                    else:
                        input('\n-- Tyck på enter för att fortsätta --')

    else:
        print(f"\nAttack misslyckades!")
        if hero.ai:
            time.sleep(1)
        else:
            input('\n-- Tyck på enter för att fortsätta --')


def dead_message(hero):
    """Handles user choice upon death"""

    while True:
        main.clear_screen()

        print(f"\n{hero.name} har dött.")
        # TODO Sammanfattning av AI's spelrunda

        print("\n[1] - Main menu"
              "\n[2] - Avsluta spelet")
        choice = input("\nSkriv in ditt val: ")

        if choice == "1":
            if not hero.ai:
                save_collected_treasure(hero)
                hero.heal_hero()
                hero.nbr_of_games += 1
                main.save_hero(hero)
            main.main_menu()
        elif choice == "2":
            if not hero.ai:
                save_collected_treasure(hero)
                hero.heal_hero()
                hero.nbr_of_games += 1
                main.save_hero(hero)
            exit()
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tryck på enter för att fortsätta --')


def delay_in_fight():
    """Makes a 1,5 sec delay in action situations"""

    print('\n.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)


def did_monster_die(monster, hero):
    """Checks if current monster died"""

    if monster.resistance >= 0:
        killed_monster_counter(monster, hero)
        main.clear_screen()
        main.print_hero_stats(hero)
        print(f"\n{monster.name} dog!")
        monster.died()
        if hero.ai:
            time.sleep(2)
        else:
            input('\n-- Tryck på enter för att fortsätta --')


def check_for_living_monsters(room, game_board, hero, grid_size, room_list):
    """Checks if any monsters are still alive"""

    monsters_alive = []
    for monster in room.monster_list:

        if monster.resistance > 0:
            monsters_alive.append(monster)

    if len(monsters_alive) == 0:
        room.monster_list = []
        room.set_room_symbol()
        # TODO Sätt in room +1 counter här
        room.sum_of_treasures = 0
        main.print_board(game_board, hero)

        check_for_treasures(room, hero, game_board, True)
        main.walk_on_board(hero, grid_size, game_board, room_list)


def start_fight_message(monster_list, hero):
    """Prints message every fight beginning"""

    print('\nBesegra alla monster för att eventuellt hitta en skatt!')
    print('Du kommer alltid att attackera monstret som är först i listan.\n'
          'När det monstret är besegrat kommer din uppmärksamhet att \n'
          'riktas mot nästa monster i listan.')


def monster_attacks(knight_ability, creature, hero):
    """Monsters attack turn"""

    if not knight_ability:
        attack_func(creature, hero, hero)
        if hero.resistance <= 0:
            dead_message(hero)
        return False
    else:
        print(f"\n{creature.name} attackerar {hero.name}!")
        delay_in_fight()
        print(f"\n{hero.name} använder sköldblock och ignorerade attacken!")
        if hero.ai is False:
            input('\n-- Tryck på enter för att fortsätta --')
        else:
            time.sleep(2)
        return False


def escape_monster(hero):
    """Escape from fight"""

    if hero.name == "Trollkarl":
        threshold = 8 * 10
    else:
        threshold = hero.agility * 10
    num = random.randint(1, 100)
    if threshold >= num:
        return True
    else:
        return False


def hero_attack(hero, monster_list, current_monster, room, game_board, grid_size, room_list):
    """Heroes turn to attack"""

    monster = monster_list[current_monster]
    if monster.resistance == 0:
        try:
            current_monster += 1
            monster = monster_list[current_monster]
        except IndexError:
            check_for_living_monsters(room, game_board, hero, grid_size, room_list)

    attack_func(hero, monster, hero)
    did_monster_die(monster, hero)
    check_for_living_monsters(room, game_board, hero, grid_size, room_list)


def hero_statistics(hero):
    print("\nStatistik för", hero.name, ":")
    print("Totalt spelade äventyr: ", hero.nbr_of_games)
    print("Insamlade skatter: ", hero.point)
    print("Antal dödade jättespindlar: ", hero.giant_spider_kills)
    print("Antal dödade skelett: ", hero.skeleton_kills)
    print("Antal dödade troll: ", hero.troll_kills)
    print("Antal dödade orcs: ", hero.orc_kills)
    input('\n-- Tyck på enter för att fortsätta --')


def killed_monster_counter(monster, hero):
    if monster.name == "Jättespindel":
        hero.giant_spider_kills += 1
    elif monster.name == "Troll":
        hero.troll_kills += 1
    elif monster.name == "Orc":
        hero.orc_kills += 1
    elif monster.name == "Skelett":
        hero.skeleton_kills += 1


def hero_flee(hero, game_board, monster_list, room, grid_size, room_list):
    print(f"\n{hero.name} Försöker att fly...")
    escape_try = escape_monster(hero)
    delay_in_fight()
    if escape_try:
        if hero.hero_class == "Trollkarl":
            print("\nLjussken!")
        print('\nDu lyckades fly från monstret')
        game_board[hero.coordinates[0]][hero.coordinates[1]] = '[ ]'
        hero.coordinates = hero.previous_coordinates
        main.place_hero(hero.coordinates, game_board)
        if hero.ai:
            time.sleep(2)
        else:

            input('\n-- Tryck på enter för att fortsätta --')

        for monster in monster_list:
            if monster.resistance > 0:
                monster.heal_remaining_monster()
            else:
                room.remove_dead_monsters()

        main.print_board(game_board, hero)
        main.walk_on_board(hero, grid_size, game_board, room_list)

    else:
        print(f'\n{hero.name} lyckades inte fly ')
        if hero.ai:
            time.sleep(2)
        else:
            input('\n-- Tryck på enter för att fortsätta --')


def heroes_turn(hero, monster_list, current_monster, room, game_board, grid_size, room_list):
    while True:
        if hero.ai:
            if hero.resistance is 1:
                menu_choice = '2'
            else:
                menu_choice = '1'
        else:
            print(f"\n-{hero.name}s tur-\n\n"
                  f"[1] - Attackera\n"
                  "[2] - Pröva att fly")

            menu_choice = input("\nSkriv in ditt val: ")
        if menu_choice == "1":
            hero_attack(hero, monster_list, current_monster, room, game_board, grid_size, room_list)
            break
        elif menu_choice == "2":
            hero_flee(hero, game_board, monster_list, room, grid_size, room_list)
            break

        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')
            main.clear_screen()
            main.print_hero_stats(hero)


def set_turn_order(monster_list, hero):

    creature_list = monster_list.copy()
    creature_list.append(hero)
    creature_list = sort_turn_list(creature_list)

    main.clear_screen()
    main.print_hero_stats(hero)
    print("\nSpelordningen följer:\n")
    i = 1
    for creature in creature_list:
        print(f"{i}. {creature.name}")
        i += 1
    if hero.ai:
        time.sleep(3)
    else:
        input('\n-- Tryck på enter för att fortsätta --')
    return creature_list


def fight(hero, grid_size, game_board, room_list, room):

    knight_ability = False
    if hero.hero_class == "Riddare":
        knight_ability = True

    monster_list = room.monster_list
    current_monster = 0
    creature_list = set_turn_order(monster_list, hero)

    while True:
        for creature in creature_list:
            if creature.is_alive:
                if creature.name == hero.name:
                    main.clear_screen()
                    main.print_hero_stats(hero)
                    heroes_turn(hero, monster_list, current_monster, room, game_board, grid_size, room_list)
                else:
                    main.clear_screen()
                    main.print_hero_stats(hero)
                    knight_ability = monster_attacks(knight_ability, creature, hero)


def check_for_treasures(room,hero, game_board, monsters_in_room):

    t_sum = 0
    for treasure in room.treasure_list:
        t_sum += treasure[1]
    hero.points_current_game += t_sum
    main.print_board(game_board, hero)


    if len(room.treasure_list) > 0:

        if not monsters_in_room:
            print('\nInga monster i rummet.')
        else:
            print('\nAlla monster besegrade.')
        print('Du hittade skatter i rummet:\n')

        i = 0
        for treasure in room.treasure_list:
            print(treasure[0])
            i += treasure[1]

        print(f'\nTotalt värde: {i}')
        print('Skatten är tillagd i din ryggsäck.')

        room.treasure_list = []
        room.set_room_symbol()
        # TODO Sätt in room +1 counter här
        if hero.ai:
            time.sleep(3)
    else:
        if not monsters_in_room:
            print('\nInga monster i rummet.')
        else:
            print('\nAlla monster besegrade.')
        print('Inga skatter hittades i rummet.')
        if hero.ai:
            time.sleep(3)
        room.set_room_symbol()
        # TODO Sätt in room +1 counter här


def check_for_monsters(hero, grid_size, game_board, room_list, room):
    if len(room.monster_list) > 0:

        main.print_board(game_board, hero)

        print(f"\nDu gick in i ett rum med {len(room.monster_list)} monster:")
        i = 1
        for monster in room.monster_list:
            print(f"{i}. {monster.name}")
            i += 1
        start_fight_message(room.monster_list, hero)
        if hero.ai:
            time.sleep(3)
        else:
            input('\n-- Tryck på enter för att fortsätta --')
        fight(hero, grid_size, game_board, room_list, room)
    else:
        return False


def undiscovered_room(room, hero, room_list, game_board, grid_size):

    monsters_in_room = check_for_monsters(hero, grid_size, game_board, room_list, room)
    check_for_treasures(room, hero, game_board, monsters_in_room)


def save_collected_treasure(hero):

    main.print_hero_stats(hero)
    print(f"\n{hero.name} samlade på sig {hero.points_current_game} poäng.")
    hero.update_total_points()
    hero.points_current_game = 0

    print(f"Totalt insamlat är {hero.point} poäng.")
    if hero.ai:
        time.sleep(2)
    else:
        main.update_pickle_hero(hero, "hero_list.pickle")
        input('\n-- Tryck på enter för att fortsätta --')


def check_room(coordinates, room_list, hero, game_board, start_coordinates, grid_size):

    for room in room_list:
        if room.coordinates == coordinates:
            if room.symbol == "[ ]":
                undiscovered_room(room, hero, room_list, game_board, grid_size)
            elif room.symbol == "[O]":
                main.print_board(game_board, hero)
                exit_to_menu = main.exit_map(game_board, (start_coordinates[0], start_coordinates[1]), hero)
                if exit_to_menu:
                    main.clear_screen()
                    if not hero.ai:
                        save_collected_treasure(hero)
                        hero.heal_hero()
                        hero.nbr_of_games += 1
                    else:
                        # TODO Sammanfattning av AI's spelrunda
                        pass

                    main.clear_screen()
                    main.main_menu()
            elif room.symbol == "[.]":
                main.print_board(game_board, hero)
                if not hero.ai:
                    print('\nInga monster i rummet.')
                    print('Inga skatter hittades i rummet.')

