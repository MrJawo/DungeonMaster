import classes


def get_character_name():

    character_name = input("\nSkriv in namnet på din nya karaktär: ")
    return character_name.title()


# Läser in och skriver ut printar text från textfil med karaktärerna och dess attribut.
def new_game_text():
    with open('introtext.txt', 'r') as f:
        print(f.read())


def print_board(game_board, hero):
    print('\n' * 100)
    print_hero_stats(hero)

    print('\nKARTA')
    for row in game_board:
        print(" ".join(row))


def print_hero_stats(hero):
    """Prints hero stats"""

    print("\n__________________________________________")
    print(f"{hero.name} ({hero.hero_class})")
    print(f"Initiativ   Tålighet    Attack  Smidighet")
    print(f"        {hero.initiative}          {hero.resistance}         {hero.attack}          {hero.agility}")
    print("__________________________________________")


def place_hero(coordinates, game_board):
    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board


def start_position(choice, grid_size, room_list):
    start_coordinates = ""

    if choice == "1":
        start_coordinates = (0, 0)
    elif choice == "2":
        start_coordinates = (0, grid_size-1)
    elif choice == "3":
        start_coordinates = (grid_size-1, 0)
    elif choice == "4":
        start_coordinates = (grid_size-1, grid_size -1)

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

    return start_corner


def choose_path():
    path = ""
    while path != "UPP" and path != "NER" and path != "VÄNSTER" and path != "HÖGER":
        path = input("Vilket håll vill du gå? (UPP, NER, VÄNSTER, HÖGER): ")
        path = path.upper()
    return path


def chosen_path(path, coordinates, grid_size):
    old_coordinates = coordinates
    x, y = coordinates
    if path == "UPP":
        if x == 0:
            print("Du slog in i en vägg, välj ett annat håll")
            return False
        else:
            x = x - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "NER":
        if x == grid_size - 1:
            print("Du slog in i en vägg, välj ett annat håll")
            return False
        else:
            x = x + 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "VÄNSTER":
        if y == 0:
            print("Du slog in i en vägg, välj ett annat håll")
            return False
        else:
            y = y - 1
            coordinates = (x, y)
            return [coordinates, old_coordinates]
    if path == "HÖGER":
        if y == grid_size - 1:
            print("Du slog in i en vägg, välj ett annat håll")
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


def board_size_choice():
    while True:
        print("\n[1] - Liten (4x4)")
        print("[2] - Mellan (5x5)")
        print("[3] - Stor (8x8)")
        menu_choice = input("\nVilken storlek vill du ha på kartan? Ange 1, 2 eller 3: ")
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
            return menu_choice


def choose_character(character_name):
    while True:
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
            hero = classes.Hero(character_name, "Thief")
            hero.add_thief()
            return hero
        else:
            print("\n-- Felaktig input, ange en siffra från menyn. --")


def exit_map(game_board, start_coordinates):
    exit_choice = ''

    if game_board[start_coordinates[0]][start_coordinates[1]] == '[x]':
        exit_choice = input("Rummet innehåller en utgång\n"
                            "[1] - Lämna kartan\n"
                            "[2] - Stanna kvar")
    if exit_choice == '1':
        return True
    elif exit_choice == '2':
        return False


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



def main_menu_choice(menu_choice):
    while True:
        if menu_choice == "1":
            character_name = get_character_name()
            new_game_text()
            hero = choose_character(character_name)
            size_choice = board_size_choice()
            grid_size = get_grid_size(size_choice)
            game_board = make_board(grid_size)
            room_list = create_rooms(grid_size)
            start_corner = choose_corner(game_board, hero)
            start_coordinates = start_position(start_corner, grid_size, room_list)

            place_hero(start_coordinates, game_board)
            print_board(game_board, hero)
            current_coordinates = start_coordinates


            # #Test för att se om det är några monter/skatter i varje rum. Testa om ni vill :)
            # for room in room_list:
            #     print()
            #     print(f"Room: {room.coordinates}")
            #     i = 1
            #     for monster in room.monster_list:
            #         print(f"Monster {i}: {monster.name}")
            #         i += 1
            #     if len(room.treasure_list) > 0:
            #         print(f"Treasures: {room.treasure_list}")
            #     print()

            while True:
                coordinates_list = take_step(current_coordinates, grid_size)
                current_coordinates = coordinates_list[0]
                update_board(game_board, coordinates_list, start_coordinates)
                print_board(game_board, hero)
                exit_to_menu = exit_map(game_board, (start_coordinates[0],start_coordinates[1]))
                if exit_to_menu:
                    main_menu()


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

