import classes
import game_functions
from os import system, name

def position_numbers(hero):
    numbers = hero.points_current_game
    string_numbers = str(numbers)
    string_length = len(string_numbers)
    number_of_spaces = 14 - string_length
    spaces = ""
    for i in range(number_of_spaces):
        spaces += " "
    return f"{spaces}{string_numbers}"


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("\n[Dungeon Run]")


def get_character_name():
    while True:

        clear_screen()
        print("__________________________________________________________")
        print("\nInitiativ   Tålighet    Attack  Smidighet   Insamlad skatt")
        print("        0          0         0          0                0")
        print("__________________________________________________________")

        character_name = input("\nSkriv in namnet på din nya karaktär: ")
        character_name = character_name.strip(" ")
        if len(character_name) > 0:
            return character_name.title()
        else:
            print('\nAnvändarnamnet måste innehålla minst ett tecken\n')
            input('-- Tyck på valfri tangent för att fortsätta --')


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
    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board


def start_position(choice, grid_size, room_list, hero):
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
    while True:
        print_board(game_board, hero)
        print("\n[1] - Uppe till vänster\n"
              "[2] - Uppe till höger\n"
              "[3] - Nere till vänster\n"
              "[4] - Nere till höger\n")
        number_list = ["1","2","3","4"]
        start_corner = input('Välj ett hörn att starta i: ')
        if start_corner in number_list:
            break
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på valfri tangent för att fortsätta --')

    return start_corner


def choose_path():
    path = ""
    while path != "UPP" and path != "NER" and path != "VÄNSTER" and path != "HÖGER":
        path = input("\nVilket håll vill du gå? (UPP, NER, VÄNSTER, HÖGER): ")
        path = path.upper()
    return path


def chosen_path(path, coordinates, grid_size):
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


def take_step(coordinates, grid_size):
    while True:
        path = choose_path()
        coordinates_list = chosen_path(path, coordinates, grid_size)
        if coordinates_list is not False:
            break
    return coordinates_list


def make_board(grid_size):
    grid = [['[ ]' for number in range(grid_size)] for number in range(grid_size)]
    return grid


def update_board(game_board, coordinates_list, start_coordinates):
    new_coordinates = coordinates_list[0]
    old_coordinates = coordinates_list[1]
    game_board[new_coordinates[0]][new_coordinates[1]] = "[x]"
    if old_coordinates == start_coordinates:
        game_board[old_coordinates[0]][old_coordinates[1]] = "[O]"
    else:
        game_board[old_coordinates[0]][old_coordinates[1]] = "[.]"


def get_grid_size(menu_choice):
    if menu_choice == "1":
        return 4
    elif menu_choice == "2":
        return 5
    elif menu_choice == "3":
        return 8


def board_size_choice(hero):
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
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')


def choose_character(character_name):

    while True:
        clear_screen()
        new_game_text(character_name)
        print("\n[1] - Riddaren\n"
              "[2] - Trollkarlen\n"
              "[3] - Tjuven")

        character_choice = input("\nVälj karaktär: ")
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
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')


def exit_map(game_board, start_coordinates, hero):
    exit_choice = ''

    while True:
        if game_board[start_coordinates[0]][start_coordinates[1]] == '[x]':
            print("\nRummet innehåller en utgång\n\n"
                            "[1] - Lämna kartan\n"
                            "[2] - Stanna kvar")
            exit_choice = input("\nSkriv in ditt val: ")
        if exit_choice == '1':
            return True
        elif exit_choice == '2':
            return False
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')

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


def walk_on_board(hero, grid_size, game_board, room_list):
    while True:
        coordinates_list = take_step(hero.coordinates, grid_size)
        current_coordinates = coordinates_list[0]
        hero.update_coordinates(current_coordinates)
        update_board(game_board, coordinates_list, hero.start_coordinates)
        game_functions.check_room(current_coordinates, room_list, hero, game_board, hero.start_coordinates, grid_size)


def main_menu_choice(menu_choice):
    while True:

        if menu_choice == "1":
            character_name = get_character_name()
            hero = choose_character(character_name)
            size_choice = board_size_choice(hero)
            grid_size = get_grid_size(size_choice)
            game_board = make_board(grid_size)
            room_list = create_rooms(grid_size)
            start_corner = choose_corner(game_board, hero)
            start_coordinates = start_position(start_corner, grid_size, room_list, hero)
            hero.coordinates = start_coordinates
            place_hero(start_coordinates, game_board)
            print_board(game_board, hero)
            walk_on_board(hero, grid_size, game_board, room_list)
        elif menu_choice == "2":
            pass
        else:
            exit()


def main_menu():
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
            print("\n-- Felaktig input, ange en siffra från menyn. --")
            input('-- Tyck på enter för att fortsätta --')


if __name__ == '__main__':

    while True:
        main_menu()

