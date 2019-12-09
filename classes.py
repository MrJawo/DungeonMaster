import game_functions
import random


class Creatures:
    def __init__(self):

        self.name = ""
        self.initiative = 0
        self.initiative_dice_sum = 0
        self.resistance = 0
        self.attack = 0
        self.agility = 0

    def spider_initiation(self):
        """Updates creature attributes to spider"""

        self.name = "Jättespindel"
        self.initiative = 7
        self.resistance = 1
        self.attack = 2
        self.agility = 3

    def skeleton_initiation(self):
        """Updates creature attributes to skeleton"""

        self.name = "Skelett"
        self.initiative = 4
        self.resistance = 2
        self.attack = 3
        self.agility = 3

    def orc_initiation(self):
        """Updates creature attributes to orc"""

        self.name = "Orc"
        self.initiative = 6
        self.resistance = 3
        self.attack = 4
        self.agility = 4

    def troll_initiation(self):
        """Updates creature attributes to troll"""

        self.name = "Troll"
        self.initiative = 2
        self.resistance = 4
        self.attack = 7
        self.agility = 2

    def throw_initiative_dice(self):
        """Updates the initiative dice sum in the beginning of every fight"""

        dice_list = []
        for i in range(self.initiative):
            dice_list.append(random.randint(1, 6))
        dice_sum = game_functions.number_sum(dice_list)

        self.initiative_dice_sum = dice_sum

    def lost_health_point(self):
        """Take of one resistance point """

        self.resistance -= 1


class Heroes(Creatures):
    def __init__(self, name, hero_class):
        super().__init__()

        self.name = name
        self.hero_class = hero_class
        self.total_treasure = 0
        self.map_treasure = 0

        self.coordinates = (0,0)
        self.previous_coordinates = (0,0)
        self.start_coordinates = (0,0)
        self.special_ability = False

    def knight_initiation(self):
        """Updates hero attributes to knight"""

        self.initiative = 5
        self.resistance = 9
        self.attack = 6
        self.agility = 4
        self.special_ability = True

    def wizard_initiation(self):
        """Updates hero attributes to wizard"""

        self.initiative = 6
        self.resistance = 4
        self.attack = 9
        self.agility = 5

    def thief_initiation(self):
        """Updates hero attributes to thief"""

        self.initiative = 7
        self.resistance = 5
        self.attack = 5
        self.agility = 7

    def update_player_coordinates(self, new_coordinates):
        """Updates and hold the players position on board"""

        self.previous_coordinates = self.coordinates
        self.coordinates = new_coordinates


class Rooms:
    def __init__(self):

        self.coordinates = (0,0)
        self.monster_list = []
        self.treasure_list = []
        self.symbol = "[ ]"
        self.exit = False

    def generate_room_content(self):
        """Generates monsters and treasures for a room"""

        self.monster_list = game_functions.get_monster_list()
        self.treasure_list = game_functions.get_treasures()

    def set_finished_room_symbol(self):
        """Sets room instances symbol to finished"""

        self.symbol = "[.]"

    def set_start_room_symbol(self):
        """Sets room instances symbol to exit"""

        self.symbol = "[O]"

    def remove_dead_monsters(self):
        """Removes monsters from list where resistance is 0"""

        for monster in self.monster_list:
            if monster.resistance == 0:
                self.monster_list.remove(monster)

    def heal_remaining_monster(self):
        """Heals damaged monsters when player flees"""

        for monster in self.monster_list:
            if monster.name == "Jättespindel":
                monster.resistance = 1
            if monster.name == "Skelett":
                monster.resistance = 2
            if monster.name == "Orc":
                monster.resistance = 3
            if monster.name == "Troll":
                monster.resistance = 4


