import main
import knight_class
import random


def int_list_sum(int_list):
    sum = 0
    for number in int_list:
        sum += number
    return sum


def treasure_generator():
    treasure_list = []

    print("\nSkatter hittade:")
    random_number = random.randint(1,100)
    if random_number <= 40:
        treasure_list.append(2)
        print("Lösa slantar: 2")

    random_number = random.randint(1, 100)
    if random_number <= 20:
        treasure_list.append(6)
        print("Pengapung: 6")

    random_number = random.randint(1, 100)
    if random_number <= 15:
        treasure_list.append(10)
        print("Guldsmycke: 10")

    random_number = random.randint(1, 100)
    if random_number <= 10:
        treasure_list.append(14)
        print("Ädelsten: 14")

    random_number = random.randint(1, 100)
    if random_number <= 5:
        treasure_list.append(20)
        print("Liten skattkista: 20")

    sum = int_list_sum(treasure_list)
    print(f"\nTotal skatt hittad: {sum}")

    # TODO Either return the treasure sum to a suitable variable or update instance attribute


treasure_generator()