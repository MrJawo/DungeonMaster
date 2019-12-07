import unittest
import main
import game_functions

class TestCases(unittest.TestCase):
    def test_make_board(self):
        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(4)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(5)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
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

        expected_result1 = (0,0)
        expected_result2 = (0, grid_size-1)
        expected_result3 = (grid_size-1, 0)
        expected_result4 = (grid_size-1, grid_size -1)

        actual_result1 = main.start_position(choice1, grid_size)
        actual_result2 = main.start_position(choice2, grid_size)
        actual_result3 = main.start_position(choice3, grid_size)
        actual_result4 = main.start_position(choice4, grid_size)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)

    def test_place_hero(self):

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        coordinates1 = (0,0)
        coordinates2 = (0,3)
        coordinates3 = (3,0)
        coordinates4 = (3,3)

        expected_result1 = [['[x]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result1 = main.place_hero(coordinates1, board)
        self.assertEqual(expected_result1, actual_result1)

        expected_result2 = [['[ ]', '[ ]', '[ ]', '[x]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result2 = main.place_hero(coordinates2, board)
        self.assertEqual(expected_result2, actual_result2)

        expected_result3 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[x]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result3 = main.place_hero(coordinates3, board)
        self.assertEqual(expected_result3, actual_result3)

        expected_result4 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[x]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result4 = main.place_hero(coordinates4, board)
        self.assertEqual(expected_result4, actual_result4)

    def test_generate_treasure(self):
        chance = 40
        treasure_type = ''
        treasure_value = 2

        expected_result_1 = 2
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

    def test_clean_list(self):

        test_list = [0, 0, (1,2), 0, (1,2)]
        expected_result = [(1,2), (1,2)]
        actual_result = game_functions.clean_list(test_list)
        self.assertEqual(expected_result,actual_result)

    def test_bubble_sort(self):
        class Creatures:
            def __init__(self, initiative_dice_sum):
                self.initiative_dice_sum = initiative_dice_sum
        creature_1 = Creatures(9)
        creature_2 = Creatures(18)
        creature_3 = Creatures(16)

        character_list = [creature_1, creature_2, creature_3]
        expected_result = [(creature_2, 18), (creature_3, 16), (creature_1, 9)]
        actual_result = game_functions.bubble_sort(character_list)
        self.assertEqual(expected_result, actual_result)

    def test_sort_turn_list(self):

        class Creatures:
            def __init__(self, initiative_dice_sum):
                self.initiative_dice_sum = initiative_dice_sum

        creature_1 = Creatures(9)
        creature_2 = Creatures(18)
        creature_3 = Creatures(16)

        character_list = [creature_1, creature_2, creature_3]
        expected_result = [creature_2, creature_3, creature_1]

        actual_result = game_functions.sort_turn_list(character_list)
        self.assertEqual(expected_result, actual_result)

    def test_dice(self):

        number_of_dices = 2
        possible_sums_ = [2,3,4,5,6,7,8,9,10,11,12]
        result = game_functions.dice(number_of_dices)
        self.assertIn(result,possible_sums_)

    # CLASS TEST

    def test_knight_initiation(self):

        test_character = game_functions.Heroes('Orvar', 'Knight')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)
        self.assertFalse(test_character.special_ability)

        test_character.knight_initiation()
        expected_result_1 = 5
        expected_result_2 = 9
        expected_result_3 = 6
        expected_result_4 = 4
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)
        self.assertTrue(test_character.special_ability)

    def test_thief_initiation(self):
        test_character = game_functions.Heroes('Orvar', 'Thief')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.thief_initiation()
        expected_result_1 = 7
        expected_result_2 = 5
        expected_result_3 = 5
        expected_result_4 = 7
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_wizard_initiation(self):
        test_character = game_functions.Heroes('Orvar', 'Wizard')
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.wizard_initiation()
        expected_result_1 = 6
        expected_result_2 = 4
        expected_result_3 = 9
        expected_result_4 = 5
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_spider_initiation(self):
        test_character = game_functions.Creatures()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.spider_initiation()
        expected_result_1 = 7
        expected_result_2 = 1
        expected_result_3 = 2
        expected_result_4 = 3
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_skeleton_initiation(self):
        test_character = game_functions.Creatures()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.skeleton_initiation()
        expected_result_1 = 4
        expected_result_2 = 2
        expected_result_3 = 3
        expected_result_4 = 3
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_orc_initiation(self):
        test_character = game_functions.Creatures()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.orc_initiation()
        expected_result_1 = 6
        expected_result_2 = 3
        expected_result_3 = 4
        expected_result_4 = 4
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_troll_initiation(self):
        test_character = game_functions.Creatures()
        expected_result = 0
        self.assertEqual(expected_result, test_character.initiative)

        test_character.troll_initiation()
        expected_result_1 = 2
        expected_result_2 = 4
        expected_result_3 = 7
        expected_result_4 = 2
        self.assertEqual(expected_result_1, test_character.initiative)
        self.assertEqual(expected_result_2, test_character.resistance)
        self.assertEqual(expected_result_3, test_character.attack)
        self.assertEqual(expected_result_4, test_character.agility)

    def test_throw_initiative_dice(self):

        test_character = game_functions.Heroes('Orvar', 'Knight')
        test_character.knight_initiation()
        self.assertEqual(test_character.initiative_dice_sum, 0)

        test_character.throw_initiative_dice()
        expected_result = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.assertIn(test_character.initiative_dice_sum, expected_result)

    def test_lost_health_point(self):

        test_character = game_functions.Heroes('Orvar', 'Knight')
        test_character.knight_initiation()
        self.assertEqual(test_character.resistance, 9)

        test_character.lost_health_point()
        self.assertEqual(test_character.resistance, 8)

    def test_update_player_coordinates(self):

        test_character = game_functions.Heroes('Orvar', 'Knight')

        first_position = [['[ ]', '[ ]', '[ ]', '[x]'], ['[ ]', '[ ]', '[ ]', '[ ]']]
        second_position = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[x]']]

        expected_coordinate_1 = (0, 0)
        expected_coordinate_2 = (0, 3)
        expected_coordinate_3 = (1, 3)

        self.assertEqual(expected_coordinate_1, test_character.coordinates)
        test_character.update_player_coordinates(first_position)
        self.assertEqual(expected_coordinate_2, test_character.coordinates)
        test_character.update_player_coordinates(second_position)
        self.assertEqual(expected_coordinate_3, test_character.coordinates)


if __name__ == '__main__':
    unittest.main()