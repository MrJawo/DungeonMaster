
#Main class used give attributes to all characters
class Creature():
    def __init__(self, name, initiative, resistance, attack, agility):
        self.name = name
        self.initiative = initiative
        self.resistance = resistance
        self.attack = attack
        self.agility = agility

#Sub class used to give unique attributes to Knight
class Knight(Creature):
    def __init__(self, name, initiative, resistance, attack, agility, point):
        super().__init__(name, initiative, resistance, attack, agility)
        self.point = point

#List to temp save newly created object
hero_list = []

#Function to add a Knight to list.
def add_knight(hero_list, name):

    initiative = 5
    resistance = 9
    attack = 6
    agility = 4
    point = 0

    #Add hero to list
    hero_list.append(Knight(name,initiative,resistance,attack,agility,point))


#Function to print all objects in list
def print_hero_list(list):
    print("Name\t\tinitiative\tResistance\tAttack\tAgility\tPoints")
    for Knight in hero_list:
        print("%s\t%d\t\t%d\t\t%d\t%d\t%d" % (Knight.name,Knight.initiative,Knight.resistance,Knight.attack,Knight.agility,Knight.point))

