
import game_functions


# Main class used give attributes to all characters
class Creature:
    def __init__(self):
        self.name = ""
        self.initiative = 0
        self.initiative_dice_sum = 0
        self.resistance = 0
        self.attack = 0
        self.agility = 0


    def initiative_sum(self):
        self.initiative_dice_sum = game_functions.dice(self.initiative)


# Sub class used to give unique attributes to Knight
class Hero(Creature):
    def __init__(self, name, hero_class):
        super().__init__()
        self.name = name
        self.point = 0
        self.points_current_game = 0
        self.hero_class = hero_class
        self.coordinates = (0, 0)
        self.previous_coordinates = (0, 0)
        self.start_coordinates = (0, 0)

    def update_coordinates(self, new_coordinates):

        self.previous_coordinates = self.coordinates
        self.coordinates = new_coordinates

    def update_total_points(self):

        self.point = self.points_current_game
        self.points_current_game = 0

    def update_current_points(self, found_points):

        self.points_current_game += found_points

    # Function to add a Knight to list.
    def add_knight(self):
        self.initiative = 5
        self.resistance = 9
        self.attack = 6
        self.agility = 4
        self.point = 0

    def add_wizard(self):
        self.initiative = 6
        self.resistance = 4
        self.attack = 9
        self.agility = 5
        self.point = 0

    def add_thief(self):
        self.initiative = 7
        self.resistance = 5
        self.attack = 5
        self.agility = 7
        self.point = 0


class Monster(Creature):
    def __init__(self):
        super().__init__()


    def add_giant_spider(self):

        self.name = "Jättespindel"
        self.initiative = 7
        self.resistance = 1
        self.attack = 2
        self.agility = 3

    def add_skeleton(self):

        self.name = "Skelett"
        self.initiative = 4
        self.resistance = 2
        self.attack = 3
        self.agility = 3

    def add_orc(self):

        self.name = "Orc"
        self.initiative = 6
        self.resistance = 3
        self.attack = 4
        self.agility = 4

    def add_troll(self):

        self.name = "Troll"
        self.initiative = 2
        self.resistance = 4
        self.attack = 7
        self.agility = 2



class Rooms:
    def __init__(self):

        self.coordinates = (0, 0)
        self.monster_list = []
        self.treasure_list = []
        self.symbol = "[ ]"
        self.exit = False

    def generate_room_content(self):
        self.monster_list = game_functions.get_monster_list()
        self.treasure_list = game_functions.get_treasures()

    def set_room_symbol(self):
        self.symbol = "[.]"

    def set_start_room_symbol(self):
        self.symbol = "[O]"

    def remove_dead_monsters(self):
        for monster in self.monster_list:
            if monster.resistance == 0:
                self.monster_list.remove(monster)

    def heal_remaining_monster(self):
        for monster in self.monster_list:
            if monster.name == "Jättespindel":
                monster.resistance = 1
            if monster.name == "Skelett":
                monster.resistance = 2
            if monster.name == "Orc":
                monster.resistance = 3
            if monster.name == "Troll":
                monster.resistance = 4


