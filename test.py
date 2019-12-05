import unittest
import main

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
        expected_result2 = [['[ ]', '[ ]', '[ ]', '[x]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]
        expected_result3 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[x]', '[ ]', '[ ]', '[ ]']]
        expected_result4 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result1 = main.place_hero(coordinates1, board)
        actual_result2 = main.place_hero(coordinates2, board)
        actual_result3 = main.place_hero(coordinates3, board)
        actual_result4 = main.place_hero(coordinates4, board)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)

def place_hero(coordinates, game_board):
    print(coordinates)
    game_board[coordinates[0]][coordinates[1]] = "[x]"
    return game_board

if __name__ == '__main__':
    unittest.main()