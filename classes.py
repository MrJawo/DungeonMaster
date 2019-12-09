

class Rooms:
    def __init__(self):

        self.coordinates = (0,0)
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


