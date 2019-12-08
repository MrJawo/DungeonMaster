import knight_class
from classes import Heroes, Creatures, Rooms
import game_functions


def character_name():
    name = input("\nSkriv in namnet på din nya karaktär: ")
    return name.title()


# Läser in och skriver ut printar text från textfil med karaktärerna och dess attribut.
def new_game_text():
    with open('introtext.txt', 'r') as f:
        print(f.read())


def print_hero_stats(hero):
    print("\n__________________________________________")
    print(f"{hero.name} ({hero.hero_class})")
    print(f"Initiativ   Tålighet    Attack  Smidighet")
    print(f"        {hero.initiative}          {hero.resistance}         {hero.attack}          {hero.agility}")
    print("__________________________________________")

def print_board(game_board, hero):

    print_hero_stats(hero)

    print('\nKARTA')
    for row in game_board:
        print(" ".join(row))


def place_hero(coordinates, game_board):
    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board


def get_selected_room(start_coordinates, room_list):
    for room in room_list:
        if room.coordinates == start_coordinates:
            room.set_start_room_symbol()
            room.exit = True
            room.monster_list = []
            room.treasure_list = []


def start_position(choice, grid_size, room_list):

    if choice == "1":
        start_coordinates = (0, 0)
        get_selected_room(start_coordinates, room_list)
    elif choice == "2":
        start_coordinates = (0, grid_size-1)
    elif choice == "3":
        start_coordinates = (grid_size-1, 0)
    elif choice == "4":
        start_coordinates = (grid_size-1, grid_size -1)
    else:
        print("\n-- Felaktig input, ange en siffra från menyn. --")
        return False
    return start_coordinates


def choose_corner(game_board, grid_size, room_list, hero):
    while True:
        print_board(game_board, hero)
        print("\n[1] - Uppe till vänster\n"
              "[2] - Uppe till höger\n"
              "[3] - Nere till vänster\n"
              "[4] - Nere till höger\n")
        coordinates = start_position(input('Välj ett hörn att starta i: '), grid_size, room_list)

        if not coordinates:
            print("\n-- Felaktig input, ange en siffra från menyn. --")
        else:
            return coordinates


def make_board(grid_size):
    grid = [['[ ]' for number in range(grid_size)] for number in range(grid_size)]
    return grid


def get_grid_size(menu_choice):
    if menu_choice == "1":
        return 4
    elif menu_choice == "2":
        return 5
    elif menu_choice == "3":
        return 8


def board_size_choice():
    while True:
        print("\n[1] - Liten (4x4)")
        print("[2] - Mellan (5x5)")
        print("[3] - Stor (8x8)")
        menu_choice = input("\nVilken storlek vill du ha på kartan? Ange 1, 2 eller 3: ")
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
            return menu_choice


def choose_character(name):
    while True:
        print("\n[1] - Riddaren\n"
              "[2] - Trollkarlen\n"
              "[3] - Tjuven")

        character_choice = input("\nVälj karaktär: ")
        if character_choice == "1":
            hero = Heroes(name, "Riddare")
            hero.knight_initiation()
            return hero
        elif character_choice == "2":
            hero = Heroes(name, "Trollkarl")
            hero.wizard_initiation()
            return hero
        elif character_choice == "3":
            hero = Heroes(name, "Tjuv")
            hero.thief_initiation()
            return hero
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")


def create_rooms(grid_size):

    room_list = []

    for i in range(grid_size):
        for j in range(grid_size):
            room = Rooms()
            room.coordinates = (i, j)
            room.generate_room_content()
            room_list.append(room)
    return room_list


def main_menu_choice(menu_choice):
    if menu_choice == "1":
        name = character_name()
        new_game_text()
        hero = choose_character(name)
        size_choice = board_size_choice()
        grid_size = get_grid_size(size_choice)
        game_board = make_board(grid_size)
        room_list = create_rooms(grid_size)
        start_coordinates = choose_corner(game_board, grid_size, room_list, hero)

        place_hero(start_coordinates, game_board)
        print_board(game_board, hero)

        # TODO Move loop

    elif menu_choice == "2":
        pass
    elif menu_choice == "3":
        exit()


def main_menu():
    while True:
        print("\n[1] - Nytt spel\n"
              "[2] - Ladda sparad karaktär\n"
              "[3] - Avsluta")
        menu_choice = input('\nVälj en siffra från menyn: ')
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
            main_menu_choice(menu_choice)
            break
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")


if __name__ == '__main__':

    hero_list = []
    monster_list = []
    treasure_list = []

    print("\nVälkommen till Dungeon Run!")

    while True:
        main_menu()
        break
