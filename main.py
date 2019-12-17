import classes
import game_functions
from os import system, name
import pickle
import random
import time

def position_numbers(hero):
    numbers = hero.points_current_game
    string_numbers = str(numbers)
    string_length = len(string_numbers)
    number_of_spaces = 14 - string_length
    spaces = ""
    for i in range(number_of_spaces):
        spaces += " "
    return f"{spaces}{string_numbers}"


def error_message():
    print("\n-- Felaktig input, ange en siffra från menyn. --")
    input('-- Tryck på enter för att fortsätta --')


def clear_screen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("\n[Dungeon Run]")


def get_character_name():
    while True:

        taken_names = []
        with open('hero_list.pickle', 'rb') as save_file:
            hero_list = pickle.load(save_file)
            if len(hero_list) > 0:
                for hero in hero_list:
                    taken_names.append(hero.name)
            taken_names.append('Jättespindel')
            taken_names.append('Skelett')
            taken_names.append('Orc')
            taken_names.append('Troll')

        clear_screen()
        print("__________________________________________________________")
        print("\nInitiativ   Tålighet    Attack  Smidighet   Insamlad skatt")
        print("        0          0         0          0                0")
        print("__________________________________________________________")

        character_name = input("\nSkriv in namnet på din nya karaktär: ")
        character_name = character_name.strip(" ")
        if len(character_name) > 0:
            character_name = character_name.title()
            if character_name not in taken_names:
                return character_name
            else:
                print('\nAnvändarnamnet är inte tillåtet, pröva ett annat!\n')
                input('-- Tryck på valfri tangent för att fortsätta --')
        else:
            print('\nAnvändarnamnet måste innehålla minst ett tecken!\n')
            input('-- Tryck på valfri tangent för att fortsätta --')


# Läser in och skriver ut printar text från textfil med karaktärerna och dess attribut.
def new_game_text(character_name):

    print("__________________________________________________________")
    print(f"{character_name}")
    print("Initiativ   Tålighet    Attack  Smidighet   Insamlad skatt")
    print("        0          0         0          0                0")
    print("__________________________________________________________")

    with open('introtext.txt', 'r', encoding="utf-8") as f:
        print(f.read())


def print_board(game_board, hero):
    clear_screen()
    print_hero_stats(hero)

    print('\nKARTA')
    for row in game_board:
        print(" ".join(row))


def print_hero_stats(hero):
    """Prints hero stats"""

    number_string = position_numbers(hero)

    print("__________________________________________________________")
    print(f"{hero.name} ({hero.hero_class})")
    print(f"Initiativ   Tålighet    Attack  Smidighet   Insamlad skatt")
    print(f"        {hero.initiative}          {hero.resistance}         {hero.attack}          {hero.agility}   {number_string}")
    print("__________________________________________________________")


def place_hero(coordinates, game_board):
    """Places the hero symbol och map"""

    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board


def ai_choose_path():
    path = ""
    path_list = ['UPP', 'NER', 'VÄNSTER', 'HÖGER']
    while path != "UPP" and path != "NER" and path != "VÄNSTER" and path != "HÖGER":
        random.shuffle(path_list)
        path = path_list[0]
    return path


def ai_chosen_path(path,coordinates, grid_size,game_board):
    old_coordinates = coordinates
    x, y = coordinates
    if path == "UPP":
        if x == 0:
            return False
        elif game_board[coordinates[0] - 1][coordinates[1]] == "[ ]":
            x = x - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
        elif x == 0 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == 0 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == grid_size - 1 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y ==0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y == grid_size - 1:
            if  game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size -1 and y == 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y == grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
            x = x - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]

    if path == "NER":
        if x == grid_size - 1:
            return False
        elif game_board[coordinates[0] + 1][coordinates[1]] == "[ ]":
            x = x + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
        elif x == 0 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == 0 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == grid_size - 1 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y ==0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y == grid_size - 1:
            if  game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size -1 and y == 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y == grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                x = x + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
            x = x + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]


    if path == "VÄNSTER":
        if y == 0:
            return False
        elif game_board[coordinates[0]][coordinates[1] - 1] == "[ ]":
            y = y - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
        elif x == 0 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == 0 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == grid_size - 1 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y ==0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y == grid_size - 1:
            if  game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size -1 and y == 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y == grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y - 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
            y = y - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]


    if path == "HÖGER":
        if y == grid_size - 1:
            return False
        elif game_board[coordinates[0]][coordinates[1] + 1] == "[ ]":
            y = y + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
        elif x == 0 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y != grid_size - 1 and y != 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == 0 and x != 0 and x != grid_size - 1 :
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif y == grid_size - 1 and x != 0 and x != grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y ==0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == 0 and y == grid_size - 1:
            if  game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size -1 and y == 0:
            if game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif x == grid_size - 1 and y == grid_size - 1:
            if game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
                y = y + 1
                coordinates = (x, y)
                return [coordinates, old_coordinates]
        elif game_board[coordinates[0]][coordinates[1] + 1] != "[ ]" \
            and game_board[coordinates[0]][coordinates[1] - 1] != "[ ]"\
            and game_board[coordinates[0] + 1][coordinates[1]] != "[ ]"\
            and game_board[coordinates[0] - 1][coordinates[1]] != "[ ]":
            y = y + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]


def start_position(choice, grid_size, room_list, hero):
    """Returns the coordinates from the chosen start corner"""

    start_coordinates = ""

    if choice == "1":
        start_coordinates = (0, 0)
    elif choice == "2":
        start_coordinates = (0, grid_size-1)
    elif choice == "3":
        start_coordinates = (grid_size-1, 0)
    elif choice == "4":
        start_coordinates = (grid_size-1, grid_size -1)

    hero.start_coordinates = start_coordinates
    for room in room_list:
        if room.coordinates == start_coordinates:
            room.set_start_room_symbol()

    return start_coordinates


def choose_corner(game_board, hero):
    number_list = ["1","2","3","4"]
    if hero.ai:
        random.shuffle(number_list)
        start_corner = number_list[0]

    else:
        while True:
            print_board(game_board, hero)
            print("\n[1] - Uppe till vänster\n"
                  "[2] - Uppe till höger\n"
                  "[3] - Nere till vänster\n"
                  "[4] - Nere till höger\n")

            start_corner = input('Välj ett hörn att starta i: ')
            if start_corner in number_list:
                break
            else:
                error_message()
    return start_corner



def choose_path():
    """Asks user which direction he/she wants to go"""

    path = ""
    while path != "UPP" and path != "NER" and path != "VÄNSTER" and path != "HÖGER":
        path = input("\nVilket håll vill du gå? (UPP, NER, VÄNSTER, HÖGER): ")
        path = path.upper()
    return path


def chosen_path(path, coordinates, grid_size):
    """Returns new and previous coordinates after taking a step"""

    old_coordinates = coordinates
    x, y = coordinates
    if path == "UPP":
        if x == 0:
            print("\n-- Du slog in i en vägg, välj ett annat håll --")
            return False
        else:
            x = x - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "NER":
        if x == grid_size - 1:
            print("\n-- Du slog in i en vägg, välj ett annat håll --")
            return False
        else:
            x = x + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "VÄNSTER":
        if y == 0:
            print("\n-- Du slog in i en vägg, välj ett annat håll --")
            return False
        else:
            y = y - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "HÖGER":
        if y == grid_size - 1:
            print("\n-- Du slog in i en vägg, välj ett annat håll --")
            return False
        else:
            y = y + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]


def take_step(coordinates, grid_size,hero, game_board):
    while True:
        if hero.ai:
            path = ai_choose_path()
            coordinates_list = ai_chosen_path(path, coordinates, grid_size, game_board)
            if coordinates_list:
                break
        else:

            path = choose_path()
            coordinates_list = chosen_path(path, coordinates, grid_size)
            if coordinates_list is not False:
                break
    return coordinates_list


def make_board(grid_size):
    """Returns the grid of selected size"""

    grid = [['[ ]' for number in range(grid_size)] for number in range(grid_size)]
    return grid


def update_board(game_board, coordinates_list, start_coordinates):
    """Sets the right visible symbol for user on map"""

    new_coordinates = coordinates_list[0]
    old_coordinates = coordinates_list[1]
    game_board[new_coordinates[0]][new_coordinates[1]] = "[x]"
    if old_coordinates == start_coordinates:
        game_board[old_coordinates[0]][old_coordinates[1]] = "[O]"
    else:
        game_board[old_coordinates[0]][old_coordinates[1]] = "[.]"


def get_grid_size(menu_choice):
    """Returns the right grid size from menu choice"""

    if menu_choice == "1":
        return 4
    elif menu_choice == "2":
        return 5
    elif menu_choice == "3":
        return 8


def board_size_choice(hero):
    """Returns the menu choice from preferred map size"""

    while True:
        clear_screen()
        print_hero_stats(hero)

        print("\n[1] - Liten (4x4)")
        print("[2] - Mellan (5x5)")
        print("[3] - Stor (8x8)")
        menu_choice = input("\nVilken storlek vill du ha på kartan? Ange 1, 2 eller 3: ")
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
            return menu_choice
        else:
            error_message()


def save_hero(hero):
    """Saves hero object in pickle file"""

    with open('hero_list.pickle', 'rb') as file:
        hero_list = pickle.load(file)
    hero_list.append(hero)
    with open('hero_list.pickle', 'wb') as file:
        pickle.dump(hero_list, file)


def return_hero(character_choice, character_name):
    """Returns hero with right attributes from menu choice"""

    if character_choice == "1":
        hero = classes.Hero(character_name, "Riddare")
        hero.add_knight()
        return hero
    elif character_choice == "2":
        hero = classes.Hero(character_name, "Trollkarl")
        hero.add_wizard()
        return hero
    elif character_choice == "3":
        hero = classes.Hero(character_name, "Tjuv")
        hero.add_thief()
        return hero
    elif character_choice == "4":
        hero = classes.Hero(character_name, "Riddare")
        hero.add_knight()
        hero.ai = True
        return hero
    elif character_choice == "5":
        hero = classes.Hero(character_name, "Trollkarl")
        hero.add_wizard()
        hero.ai = True
        return hero
    elif character_choice == "6":
        hero = classes.Hero(character_name, "Tjuv")
        hero.add_thief()
        hero.ai = True
        return hero
    else:
        print("\n-- Felaktig input, ange en siffra från menyn. --")
        input('-- Tyck på enter för att fortsätta --')

def choose_character(character_name):

    while True:
        clear_screen()
        new_game_text(character_name)
        print("\n[1] - Riddaren\n"
              "[2] - Trollkarlen\n"
              "[3] - Tjuven\n"
              "[4] - AI Riddaren\n"
              "[5] - AI Trollkarl\n"
              "[6] - AI Tjuv")

        character_choice = input("\nVälj karaktär: ")
        choice_list = ["1", "2", "3", "4", "5", "6"]
        if character_choice in choice_list:
            return character_choice
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')


def exit_map(game_board, start_coordinates, hero):
    """Checks if user wants to leave the board"""

    exit_choice = ''

    while True:
        if hero.ai and hero.escape_mode:
            # TODO Skriv ut sammanfattning, vänta på enter, gå till menyn
            print('')
            pass
        if game_board[start_coordinates[0]][start_coordinates[1]] == '[x]':
            print("\nRummet innehåller en utgång\n\n"
                            "[1] - Lämna kartan\n"
                            "[2] - Stanna kvar")
            exit_choice = input("\nSkriv in ditt val: ")
        if exit_choice == '1':
            hero.nbr_of_games += 1
            return True
        elif exit_choice == '2':
            return False
        else:
            error_message()
            print_board(game_board, hero)


def create_rooms(grid_size):
    """Creates an instance for each room on the map"""

    room_list = []

    for i in range(grid_size):
        for j in range(grid_size):
            room = classes.Rooms()
            room.coordinates = (i, j)
            room.generate_room_content()
            room_list.append(room)
    return room_list


def escape_board(hero):
    old_coordinates = hero.coordinates
    coordinates = hero.way_out_coordinates[0]
    hero.way_out_coordinates.pop(0)
    return [coordinates, old_coordinates]


def walk_on_board(hero, grid_size, game_board, room_list):
    """Makes user walk on board"""

    while True:
        if hero.ai and hero.escape_mode:
            coordinates_list = escape_board(hero)
            current_coordinates = coordinates_list[0]
            hero.update_coordinates(current_coordinates)
            update_board(game_board, coordinates_list, hero.start_coordinates)
            print_board(game_board, hero)
            time.sleep(1)
            game_functions.check_room(current_coordinates, room_list, hero, game_board, hero.start_coordinates,
                                      grid_size)
            time.sleep(1)
        else:
            coordinates_list = take_step(hero.coordinates, grid_size, hero, game_board)
            current_coordinates = coordinates_list[0]
            hero.way_out_coordinates.append(current_coordinates)
            hero.update_coordinates(current_coordinates)
            update_board(game_board, coordinates_list, hero.start_coordinates)
            print_board(game_board,hero)
            if hero.ai:
                time.sleep(1)
            game_functions.check_room(current_coordinates, room_list, hero, game_board, hero.start_coordinates, grid_size)


def open_pickle_file(path):
    """Open pickle file and returns the contained list"""

    with open(path, 'rb') as save_file:
        hero_list = pickle.load(save_file)
    return hero_list


def write_in_pickle_file(hero_list, path):
    """Writes in selected pickle file"""

    with open(path, 'wb') as save_file:
        pickle.dump(hero_list, save_file)


def update_pickle_hero(hero, path):
    """Updates selected hero in pickle file"""

    hero_list = open_pickle_file(path)
    i = 0
    for saved_hero in hero_list:
        if saved_hero.name == hero.name:
            hero_list.pop(i)
            hero_list.insert(i, hero)
        i += 1
    write_in_pickle_file(hero_list, path)


def get_hero_list(path):
    """Returns a list of object from selected pickle file"""

    with open(path, 'rb') as file:
        hero_list = pickle.load(file)
    return hero_list


def load_hero():
    """Returns the selected hero object from pickle file"""

    hero_list = get_hero_list('hero_list.pickle')

    while True:
        clear_screen()
        i = 1
        number_of_hero = []
        if len(hero_list) > 0:
            print()
            for hero in hero_list:
                print(f'[{i}] - {hero.name} - {hero.hero_class} - Poäng: {hero.point}')
                number_of_hero.append(str(i))
                i += 1

            print("[0] - Gå till huvud-menyn")
            hero_choice = input('\nVälj en hjälte: ')

            if hero_choice in number_of_hero:
                for number in number_of_hero:
                    if number == hero_choice:
                        hero_index = int(number)-1
                        return hero_list[hero_index]
            elif hero_choice == "0":
                main_menu()
            else:
                print("\n-- Felaktig input, ange en siffra från menyn. --")
                input('-- Tryck på enter för att fortsätta --')
        else:
            print("\n Inga hjältar finns sparade än.\n")
            input('-- Tryck på enter för att fortsätta --')
            main_menu()


def initiate_game(hero):
    """Initiates a game"""

    size_choice = board_size_choice(hero)
    grid_size = get_grid_size(size_choice)
    game_board = make_board(grid_size)
    room_list = create_rooms(grid_size)
    start_corner = choose_corner(game_board, hero)
    start_coordinates = start_position(start_corner, grid_size, room_list, hero)
    hero.coordinates = start_coordinates
    place_hero(start_coordinates, game_board)
    print_board(game_board, hero)
    if hero.ai:
        time.sleep(1.5)
    walk_on_board(hero, grid_size, game_board, room_list)


def main_menu_choice(menu_choice):
    """Handles main menu choice"""

    while True:
        if menu_choice == "1":
            character_name = get_character_name()
            hero_choice = choose_character(character_name)
            hero = return_hero(hero_choice, character_name)
            if not hero.ai:
                save_hero(hero)
            initiate_game(hero)
        elif menu_choice == "2":
            hero = load_hero()
            game_functions.hero_statistics(hero)
            initiate_game(hero)
        else:
            exit()


def main_menu():
    """Prints and receives main menu choice"""

    while True:
        clear_screen()

        print("\n[1] - Nytt spel\n"
              "[2] - Ladda sparad karaktär\n"
              "[3] - Avsluta")
        menu_choice = input('\nVälj en siffra från menyn: ')
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":

            main_menu_choice(menu_choice)
            break
        else:
            error_message()


if __name__ == '__main__':

    start_list = []
    with open("hero_list.pickle", "wb") as file:
        pickle.dump(start_list, file)
    while True:
        main_menu()
