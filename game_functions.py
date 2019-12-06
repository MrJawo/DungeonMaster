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

    int_list = []
    print('\nHittade skatter:')
    int_list.append(generate_treasure(40, 'Lösa slantar: 2', 2, random.randint(1, 100)))
    int_list.append(generate_treasure(20, 'Pengapung: 6', 6, random.randint(1, 100)))
    int_list.append(generate_treasure(15, 'Gukdsmycke: 10', 10, random.randint(1, 100)))
    int_list.append(generate_treasure(10, 'Ädelsten: 14', 14, random.randint(1, 100)))
    int_list.append(generate_treasure(5, 'Liten skattkista: 20', 20, random.randint(1, 100)))

    sum = treasure_sum(int_list)
    print(f'\nSumman av hittade skatter: {sum}')
    return sum
