import unittest
import main
import game_functions
import classes
import pickle


class TestCases(unittest.TestCase):
    def test_make_board(self):
        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(4)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(5)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(8)
        self.assertEqual(expected_result, actual_result)

    def test_get_grid_size(self):

        menu_choice1 = "1"
        menu_choice2 = "2"
        menu_choice3 = "3"

        expected_result1 = 4
        expected_result2 = 5
        expected_result3 = 8

        actual_result1 = main.get_grid_size(menu_choice1)
        actual_result2 = main.get_grid_size(menu_choice2)
        actual_result3 = main.get_grid_size(menu_choice3)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)

    def test_start_position(self):

        choice1 = "1"
        choice2 = "2"
        choice3 = "3"
        choice4 = "4"
        grid_size = 4

        expected_result1 = (0, 0)
        expected_result2 = (0, grid_size-1)
        expected_result3 = (grid_size-1, 0)
        expected_result4 = (grid_size-1, grid_size - 1)

        room = classes.Rooms()
        room_list = [room]

        hero = classes.Hero("Orvar", "Riddare")

        actual_result1 = main.start_position(choice1, grid_size, room_list, hero)
        actual_result2 = main.start_position(choice2, grid_size, room_list, hero)
        actual_result3 = main.start_position(choice3, grid_size, room_list, hero)
        actual_result4 = main.start_position(choice4, grid_size, room_list, hero)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)

    def test_place_hero(self):

        coordinates1 = (0, 0)
        coordinates2 = (0, 3)
        coordinates3 = (3, 0)
        coordinates4 = (3, 3)

        expected_result1 = [['[x]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result1 = main.place_hero(coordinates1, board)
        self.assertEqual(expected_result1, actual_result1)

        expected_result2 = [['[ ]', '[ ]', '[ ]', '[x]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result2 = main.place_hero(coordinates2, board)
        self.assertEqual(expected_result2, actual_result2)

        expected_result3 = [['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[x]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result3 = main.place_hero(coordinates3, board)
        self.assertEqual(expected_result3, actual_result3)

        expected_result4 = [['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[ ]'],
                            ['[ ]', '[ ]', '[ ]', '[x]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result4 = main.place_hero(coordinates4, board)
        self.assertEqual(expected_result4, actual_result4)

    def test_generate_treasure(self):
        chance = 40
        treasure_type = ''
        treasure_value = 2

        expected_result_1 = ('', 2)
        expected_result_2 = 0
        actual_result_1 = game_functions.generate_treasure(chance, treasure_type, treasure_value, 15)
        actual_result_2 = game_functions.generate_treasure(chance, treasure_type, treasure_value, 50)

        self.assertEqual(expected_result_1, actual_result_1)
        self.assertEqual(expected_result_2, actual_result_2)

    def test_number_sum(self):

        test_list = [1, 2, 3]
        expected_result = 6
        actual_result = game_functions.number_sum(test_list)
        self.assertEqual(expected_result, actual_result)

    def test_treasure_sum(self):

        test_list = [('Slantar: 2', 2), ('Ädelstenar: 14', 14)]
        expected_result = 16
        actual_result = game_functions.treasure_sum(test_list)
        self.assertEqual(expected_result, actual_result)

    def test_clean_list(self):

        test_list = [0, 0, (1, 2), 0, (1, 2)]
        expected_result = [(1, 2), (1, 2)]
        actual_result = game_functions.clean_list(test_list)
        self.assertEqual(expected_result, actual_result)

    def test_bubble_sort(self):
        class Creatures:
            def __init__(self, initiative_dice_sum):
                self.initiative_dice_sum = initiative_dice_sum

        creature_1 = Creatures(9)
        creature_2 = Creatures(18)
        creature_3 = Creatures(16)

        tuple_list = [(creature_1, creature_1.initiative_dice_sum),
                      (creature_2, creature_2.initiative_dice_sum),
                      (creature_3, creature_3.initiative_dice_sum)]

        character_list = [creature_1, creature_2, creature_3]
        expected_result = [(creature_2, 18), (creature_3, 16), (creature_1, 9)]
        actual_result = game_functions.bubble_sort(character_list, tuple_list)
        self.assertEqual(expected_result, actual_result)

    def test_strip_tuple_list(self):

        tuple_list = [(1, 2), (1, 2)]
        expected_result = [1, 1]
        actual_result = game_functions.strip_tuple_list(tuple_list)
        self.assertEqual(expected_result, actual_result)

    def test_dice(self):

        number_of_dices = 2
        possible_sums_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result = game_functions.dice(number_of_dices)
        self.assertIn(result, possible_sums_)

    # CLASS TEST

    def test_knight_initiation(self):

        test_character = classes.Hero('Orvar', 'Knight')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_knight()
        expected_result_1 = 5
        expected_result_2 = 9
        expected_result_3 = 6
        expected_result_4 = 4
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_thief_initiation(self):
        test_character = classes.Hero('Orvar', 'Thief')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_thief()
        expected_result_1 = 7
        expected_result_2 = 5
        expected_result_3 = 5
        expected_result_4 = 7
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_wizard_initiation(self):
        test_character = classes.Hero('Orvar', 'Wizard')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_wizard()
        expected_result_1 = 6
        expected_result_2 = 4
        expected_result_3 = 9
        expected_result_4 = 5
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_spider_initiation(self):
        test_character = classes.Monster()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_giant_spider()
        expected_result_1 = 7
        expected_result_2 = 1
        expected_result_3 = 2
        expected_result_4 = 3
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_skeleton_initiation(self):
        test_character = classes.Monster()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_skeleton()
        expected_result_1 = 4
        expected_result_2 = 2
        expected_result_3 = 3
        expected_result_4 = 3
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_orc_initiation(self):
        test_character = classes.Monster()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_orc()
        expected_result_1 = 6
        expected_result_2 = 3
        expected_result_3 = 4
        expected_result_4 = 4
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_troll_initiation(self):
        test_character = classes.Monster()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.add_troll()
        expected_result_1 = 2
        expected_result_2 = 4
        expected_result_3 = 7
        expected_result_4 = 2
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_update_player_coordinates(self):

        test_character = classes.Hero('Orvar', 'Knight')

        old_coordinates = (0, 0)
        new_coordinates = (0, 3)

        self.assertEqual(old_coordinates, test_character.coordinates)
        test_character.update_coordinates(new_coordinates)
        self.assertEqual(new_coordinates, test_character.coordinates)

    def test_set_room_symbol(self):

        test_room = classes.Rooms()

        expected_result = "[ ]"
        self.assertEqual(expected_result, test_room.symbol)
        test_room.set_room_symbol()
        expected_result = "[.]"
        self.assertEqual(expected_result, test_room.symbol)

    def test_set_start_room_symbol(self):

        test_room = classes.Rooms()

        expected_result = "[ ]"
        self.assertEqual(expected_result, test_room.symbol)
        test_room.set_start_room_symbol()
        expected_result = "[O]"
        self.assertEqual(expected_result, test_room.symbol)

    def test_remove_dead_monsters(self):

        monster_1 = classes.Monster()
        monster_1.add_giant_spider()
        monster_1.resistance = 0
        monster_2 = classes.Monster()
        monster_2.add_giant_spider()
        monster_2.resistance = 1
        room = classes.Rooms()
        room.monster_list = [monster_1, monster_2]

        room.remove_dead_monsters()
        expected_result = [monster_2]
        self.assertEqual(expected_result, room.monster_list)

    def test_heal_remaining_monster(self):

        monster_1 = classes.Monster()
        monster_1.add_skeleton()
        monster_1.resistance = 1
        room = classes.Rooms()
        room.monster_list = [monster_1]

        monster_1.heal_remaining_monster()
        expected_result = 2
        monster_1 = room.monster_list[0]
        actual_result = monster_1.resistance
        self.assertEqual(expected_result, actual_result)

    def test_heal_hero(self):

        hero1 = classes.Hero('Orvar', 'Riddare')
        hero1.resistance = 1
        hero2 = classes.Hero('Orvar', 'Trollkarl')
        hero2.resistance = 1
        hero3 = classes.Hero('Orvar', 'Tjuv')
        hero3.resistance = 1

        hero1.heal_hero()
        hero2.heal_hero()
        hero3.heal_hero()

        expected_result1 = 9
        expected_result2 = 4
        expected_result3 = 5

        self.assertEqual(expected_result1, hero1.resistance)
        self.assertEqual(expected_result2, hero2.resistance)
        self.assertEqual(expected_result3, hero3.resistance)

    def test_get_hero_list(self):
        hero1 = classes.Hero('Orvar1', 'Riddare')
        hero2 = classes.Hero('Orvar2', 'Trollkarl')
        hero3 = classes.Hero('Orvar3', 'Tjuv')

        expected_result = [hero1, hero2, hero3]
        with open("test_list.pickle", "wb") as file:
            pickle.dump(expected_result, file)

        actual_result = main.get_hero_list('test_list.pickle')
        test_hero1 = actual_result[0]
        test_hero2 = actual_result[1]
        test_hero3 = actual_result[2]

        self.assertEqual(hero1.name, test_hero1.name)
        self.assertEqual(hero2.name, test_hero2.name)
        self.assertEqual(hero3.name, test_hero3.name)

    def test_open__write_pickle_file(self):

        hero1 = classes.Hero('Orvar1', 'Riddare')
        hero_list = [hero1]
        main.write_in_pickle_file(hero_list, 'test_list.pickle')
        expected_result = hero1.name

        loaded_list = main.open_pickle_file('test_list.pickle')
        hero2 = loaded_list[0]
        self.assertEqual(expected_result, hero2.name)

    def test_update_pickle_hero(self):
        hero1 = classes.Hero('Orvar1', 'Riddare')
        hero1.add_knight()
        hero1.point = 1

        hero_list = [hero1]
        main.write_in_pickle_file(hero_list, 'test_list.pickle')

        hero1.point = 5
        main.update_pickle_hero(hero1, 'test_list.pickle')

        hero_list2 = main.open_pickle_file('test_list.pickle')
        hero2 = hero_list2[0]

        self.assertEqual(5, hero2.point)

    def test_create_rooms(self):

        expected_result1 = 9
        room_list = main.create_rooms(3)
        self.assertEqual(expected_result1, len(room_list))

        expected_result2 = (0, 0)
        expected_result3 = (2, 2)

        room1 = room_list[0]
        room2 = room_list[-1]

        self.assertEqual(expected_result2, room1.coordinates)
        self.assertEqual(expected_result3, room2.coordinates)

    def test_return_hero(self):

        expected_result1 = "Riddare"
        expected_result2 = "Trollkarl"
        expected_result3 = "Tjuv"

        hero1 = main.return_hero('1', 'Orvar45')
        hero2 = main.return_hero('2', 'Orvar45')
        hero3 = main.return_hero('3', 'Orvar45')

        self.assertEqual(expected_result1, hero1.hero_class)
        self.assertEqual(expected_result2, hero2.hero_class)
        self.assertEqual(expected_result3, hero3.hero_class)

    def test_update_total_points(self):

        hero = classes.Hero('Orvar', 'Riddare')
        hero.points_current_game = 5
        expected_result = 0
        expected_result2 = 5
        self.assertEqual(expected_result, hero.point)
        hero.update_total_points()
        self.assertEqual(expected_result2, hero.point)


if __name__ == '__main__':
    unittest.main()
    input()
