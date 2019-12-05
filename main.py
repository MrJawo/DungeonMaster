import knight_class


def character_name():
    name = input("\nSkriv in namnet på din nya karaktär: ")
    return name.title()


# Läser in och skriver ut printar text från textfil med karaktärerna och dess attribut.
def new_game_text():
    with open('introtext.txt', 'r') as f:
        print(f.read())


def print_board(game_board):
    print()
    for row in game_board:
        print(" ".join(row))


def place_hero(coordinates, game_board):
    print(coordinates)
    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board


def start_position(choice, grid_size):
    start_coordinates = ""

    if choice == "1":
        start_coordinates = (0, 0)
    elif choice == "2":
        start_coordinates = (0, grid_size-1)
    elif choice == "3":
        start_coordinates = (grid_size-1, 0)
    elif choice == "4":
        start_coordinates = (grid_size-1, grid_size -1)

    return start_coordinates


def choose_corner(game_board):
    while True:
        print_board(game_board)
        print("\n[1] - Uppe till vänster\n"
              "[2] - Uppe till höger\n"
              "[3] - Nere till vänster\n"
              "[4] - Nere till höger\n")
        return input('Välj ett hörn att starta i: ')


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
            knight_class.add_knight(hero_list, name)
            break
        elif character_choice == "2":
            pass
        elif character_choice == "3":
            pass
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")


def main_menu_choice(menu_choice):
    if menu_choice == "1":
        name = character_name()
        new_game_text()
        choose_character(name)
        size_choice = board_size_choice()
        grid_size = get_grid_size(size_choice)
        game_board = make_board(grid_size)
        start_corner = choose_corner(game_board)
        start_coordinates = start_position(start_corner, grid_size)
        place_hero(start_coordinates, game_board)
        print_board(game_board)
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
    print("\nVälkommen till Dungeon Run!")

    while True:
        main_menu()
        break
