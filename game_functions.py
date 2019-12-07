import random


def treasure_sum(int_list):
    sum = 0
    for number in int_list:
        sum += number

    return sum


def generate_treasure(chance, treasure_type, treasure_value, random_int):

    if random_int <= chance:
        print(treasure_type)
        return treasure_value
    else:
        return 0


def get_trasures_list():

    print('\nHittade skatter:')
    treasure_list = [generate_treasure(40, 'Lösa slantar: 2', 2, random.randint(1, 100)),
                generate_treasure(20, 'Pengapung: 6', 6, random.randint(1, 100)),
                generate_treasure(15, 'Gukdsmycke: 10', 10, random.randint(1, 100)),
                generate_treasure(10, 'Ädelsten: 14', 14, random.randint(1, 100)),
                generate_treasure(5, 'Liten skattkista: 20', 20, random.randint(1, 100))]

    sum = treasure_sum(treasure_list)
    print(f'\nSumman av hittade skatter: {sum}')
    return sum


def generate_monster(chance, monster_type, random_int):

    if random_int <= chance:
        # TODO Make monster instance here
        monster_tuple = ("Jättespindel", "Objekt")
        print(f"\n{monster_type} spawned!")
        return monster_tuple
    else:
        return 0


def clean_list(monster_list):

    cleaned_list = []
    for element in monster_list:
        if element != 0:
            cleaned_list.append(element)
    return cleaned_list


def get_monster_list():

    monster_list = [generate_monster(20, 'Jättespindel', random.randint(1, 100)),
                    generate_monster(15, 'Skelett', random.randint(1, 100)),
                    generate_monster(10, 'Orc', random.randint(1, 100)),
                    generate_monster(5, 'Troll', random.randint(1, 100))]

    monster_list = clean_list(monster_list)
    return monster_list
