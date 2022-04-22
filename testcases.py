import Game_01
import unittest


class UnitTestCases(unittest.TestCase):
    def test_case_create_deck(self):
        deck = Game_01.create_deck()
        self.assertEqual(len(deck), 32)

    def test_case_for_shuffle(self):
        deck = Game_01.create_deck()
        deck_1 = deck[:]
        shuffled_deck = Game_01.shuffle(deck)
        self.assertTrue(deck_1 != shuffled_deck)

    def test_case_for_deal_9_cards(self):
        deck_1 = Game_01.create_deck()
        shuffled_deck_1 = Game_01.shuffle(deck_1)
        _, shuffled_deck_1 = Game_01.deal(shuffled_deck_1)

        deck_2 = Game_01.create_deck()
        shuffled_deck_2 = Game_01.shuffle(deck_2)

        self.assertTrue(len(shuffled_deck_1) == 23)
        self.assertTrue(len(shuffled_deck_2) == 32)

    def test_case_for_deal_1_cards(self):
        deck = Game_01.create_deck()
        shuffled_deck = Game_01.shuffle(deck)
        _, shuffled_deck = Game_01.deal(shuffled_deck)
        shuffled_deck_1 = shuffled_deck[:]
        _, shuffled_deck_2 = Game_01.deal(shuffled_deck)

        self.assertEqual(len(shuffled_deck_1) - 1, len(shuffled_deck_2))

    def test_case_for_update_card(self):
        new_card = ['CL', 3]
        deck = Game_01.create_deck()
        shuffled_deck = Game_01.shuffle(deck)
        board, _ = Game_01.deal(shuffled_deck)
        board = Game_01.update_card(board, new_card, [0, 0])

        self.assertEqual(board[0][0], new_card)

    def test_case_for_verify_matching_for_run(self):
        row_one = ['DM', 1], ['DM', 8], ['HR', 9]
        row_two = ['HR', 2], ['HR', 1], ['SP', 4]
        row_three = ['CL', 2], ['CL', 3], ['CL', 4]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(won)
        self.assertEqual(score, 25)
        self.assertEqual(state, 'Run')

    def test_case_for_verify_matching_for_simple_run(self):
        row_one = ['DM', 1], ['DM', 8], ['HR', 9]
        row_two = ['HR', 2], ['HR', 1], ['SP', 4]
        row_three = ['CL', 3], ['DM', 3], ['CL', 4]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(won)
        self.assertEqual(score, 20)
        self.assertEqual(state, 'Simple Run')

    def test_case_for_verify_matching_for_set(self):
        row_one = ['DM', 2], ['DM', 8], ['HR', 1]
        row_two = ['HR', 2], ['HR', 1], ['SP', 4]
        row_three = ['CL', 2], ['DM', 5], ['CL', 7]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(won)
        self.assertEqual(score, 15)
        self.assertEqual(state, 'Set')

    def test_case_for_verify_matching_for_simple_set(self):
        row_one = ['DM', 2], ['DM', 8], ['HR', 1]
        row_two = ['HR', 1], ['HR', 1], ['SP', 4]
        row_three = ['HR', 3], ['DM', 5], ['CL', 7]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(won)
        self.assertEqual(score, 10)
        self.assertEqual(state, 'Simple Set')

    def test_case_for_verify_matching_for_lost(self):
        row_one = ['DM', 2], ['DM', 8], ['HR', 1]
        row_two = ['HR', 1], ['HR', 1], ['SP', 4]
        row_three = ['DM', 3], ['DM', 5], ['CL', 7]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(not won)
        self.assertEqual(score, 0)
        self.assertEqual(state, 'Lost')

    def test_case_for_verify_matching_for_run_among_all_other(self):
        row_one = ['DM', 1], ['DM', 8], ['HR', 3]
        row_two = ['DM', 2], ['DM', 3], ['SP', 4]
        row_three = ['DM', 3], ['DM', 3], ['CL', 5]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, 0)

        self.assertTrue(won)
        self.assertEqual(score, 25)
        self.assertEqual(state, 'Run')

    def test_case_for_verify_matching_for_lost_by_calculate_number_of_steps(self):
        row_one = ['DM', 2], ['DM', 8], ['HR', 1]
        row_two = ['HR', 1], ['HR', 1], ['SP', 4]
        row_three = ['DM', 3], ['DM', 5], ['CL', 7]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, -5)

        self.assertTrue(not won)
        self.assertEqual(score, -5)
        self.assertEqual(state, 'Lost')

    def test_case_for_verify_matching_for_run_by_calculate_number_of_steps(self):
        row_one = ['DM', 1], ['DM', 8], ['HR', 9]
        row_two = ['HR', 2], ['HR', 1], ['SP', 4]
        row_three = ['CL', 2], ['CL', 3], ['CL', 4]
        board = [row_one, row_two, row_three]

        won, score, state = Game_01.verify_matching(board, -7)

        self.assertTrue(won)
        self.assertEqual(score, 18)
        self.assertEqual(state, 'Run')


if __name__ == '__main__':
    unittest.main()

