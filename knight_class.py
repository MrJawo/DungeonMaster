
#Main class used give attributes to all characters
class Creature():
    def __init__(self):
        self.name = ""
        self.initiative = 0
        self.resistance = 0
        self.attack = 0
        self.agility = 0

#Sub class used to give unique attributes to Knight
class Hero(Creature):
    def __init__(self, name, hero_class):   
        super().__init__()
        self.name = name
        self.point = 0
        self.hero_class = hero_class
        self.coordinates = (0,0)
        self.previous_coordinates = (0,0)

    def update_coordinates(self, new_coordinates, old_coordinates):
        self.coordinates = new_coordinates
        self.previous_coordinates = old_coordinates

    #Function to add a Knight to list.
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
        self.initiative = 7
        self.resistance = 1
        self.attack = 2
        self.agility = 3
        self.name = "Jättespindel"

    def add_skeleton(self):
        self.initiative = 4
        self.resistance = 2
        self.attack = 3
        self.agility = 3
        self.name = "Skelett"

    def add_orc(self):
        self.initiative = 6
        self.resistance = 3
        self.attack = 4
        self.agility = 4
        self.name = "Orc"

    def add_troll(self):
        self.initiative = 2
        self.resistance = 4
        self.attack = 7
        self.agility = 2
        self.name = "Troll"