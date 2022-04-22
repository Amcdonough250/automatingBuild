import random


def create_deck():
    """ Takes no parameter
    Returns a 2D-list """

    # an initially empty deck
    deck = []
    suits = ["SP", "CL", "HR", "DM"]
    faces = []

    # creates a list of all face values
    for x in range(2, 10):
        faces.append(x)
    # faces = [x for x in range(2,10)] # an alternative technique - list comprehension
    # creates cards [s,f] and inserting them to the deck
    for s in suits:
        for f in faces:
            deck.append([s, f])
    return deck


def shuffle(deck):
    """Takes a 2D-list
    Returns a shuffled 2D-list"""

    # copies the deck, so the original deck remains same
    c_deck = deck
    random.shuffle(c_deck)
    return c_deck


def deal(shuffle_deck):
    """
    Take out first 9 cards
    :param shuffle_deck:
    :return: Board, updated deck
    """
    if len(shuffle_deck) < 32:
        return shuffle_deck.pop(0), shuffle_deck
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(shuffle_deck[0])
            del shuffle_deck[0]
        board.append(row)
    return board, shuffle_deck


def print_board(board):
    """
    print the board
    :param board:
    :return: None
    """
    for i in board:
        print(end='| ')
        for j in i:
            print(j, end=' |')
        print()


def update_card(board, new_card, index):
    """
    Updating the board
    :param board:
    :param new_card:
    :param index:
    :return: updated board
    """
    board[index[0]][index[1]] = new_card
    return board


def verify_matching(board, current_score):
    if board[0][0][0] == board[0][1][0] == board[0][2][0] and board[0][0][1] - board[0][1][1] == board[0][1][1] - \
            board[0][2][1]:
        return True, 25 + current_score, 'Run'
    elif board[1][0][0] == board[1][1][0] == board[1][2][0] and board[1][0][1] - board[1][1][1] == board[1][1][1] - \
            board[1][2][1]:
        return True, 25 + current_score, 'Run'
    elif board[2][0][0] == board[2][1][0] == board[2][2][0] and board[2][0][1] - board[2][1][1] == board[2][1][1] - \
            board[2][2][1]:
        return True, 25 + current_score, 'Run'
    elif board[0][0][0] == board[1][0][0] == board[2][0][0] and board[0][0][1] - board[1][0][1] == board[1][0][1] - \
            board[2][0][1]:
        return True, 25 + current_score, 'Run'
    elif board[0][1][0] == board[1][1][0] == board[2][1][0] and board[0][1][1] - board[1][1][1] == board[1][1][1] - \
            board[2][1][1]:
        return True, 25 + current_score, 'Run'
    elif board[0][2][0] == board[1][2][0] == board[2][2][0] and board[0][2][1] - board[1][2][1] == board[1][2][1] - \
            board[2][2][1]:
        return True, 25 + current_score, 'Run'
    elif board[0][0][0] == board[1][1][0] == board[2][2][0] and board[0][0][1] - board[1][1][1] == board[1][1][1] - \
            board[2][2][1]:
        return True, 25 + current_score, 'Run'
    elif board[0][2][0] == board[1][1][0] == board[2][0][0] and board[0][2][1] - board[1][1][1] == board[1][1][1] - \
            board[2][0][1]:
        return True, 25 + current_score, 'Run'

    if board[0][0][1] - board[0][1][1] in (-1, 1) and board[0][1][1] - board[0][2][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[1][0][1] - board[1][1][1] in (-1, 1) and board[1][1][1] - board[1][2][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[2][0][1] - board[2][1][1] in (-1, 1) and board[2][1][1] - board[2][2][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[0][0][1] - board[1][0][1] in (-1, 1) and board[1][0][1] - board[2][0][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[0][1][1] - board[1][1][1] in (-1, 1) and board[1][1][1] - board[2][1][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[0][2][1] - board[1][2][1] in (-1, 1) and board[1][2][1] - board[2][2][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[0][0][1] - board[1][1][1] in (-1, 1) and board[1][1][1] - board[2][2][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'
    elif board[0][2][1] - board[1][1][1] in (-1, 1) and board[1][1][1] - board[2][0][1] in (-1, 1):
        return True, 20 + current_score, 'Simple Run'

    if board[0][0][1] == board[0][1][1] == board[0][2][1]:
        return True, 15 + current_score, 'Set'
    elif board[1][0][1] == board[1][1][1] == board[1][2][1]:
        return True, 15 + current_score, 'Set'
    elif board[2][0][1] == board[2][1][1] == board[2][2][1]:
        return True, 15 + current_score, 'Set'
    elif board[0][0][1] == board[1][0][1] == board[2][0][1]:
        return True, 15 + current_score, 'Set'
    elif board[0][1][1] == board[1][1][1] == board[2][1][1]:
        return True, 15 + current_score, 'Set'
    elif board[0][2][1] == board[1][2][1] == board[2][2][1]:
        return True, 15 + current_score, 'Set'
    elif board[0][0][1] == board[1][1][1] == board[2][2][1]:
        return True, 15 + current_score, 'Set'
    elif board[0][2][1] == board[1][1][1] == board[2][0][1]:
        return True, 15 + current_score, 'Set'

    if board[0][0][0] == board[0][1][0] == board[0][2][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[1][0][0] == board[1][1][0] == board[1][2][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[2][0][0] == board[2][1][0] == board[2][2][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[0][0][0] == board[1][0][0] == board[2][0][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[0][1][0] == board[1][1][0] == board[2][1][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[0][2][0] == board[1][2][0] == board[2][2][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[0][0][0] == board[1][1][0] == board[2][2][0]:
        return True, 10 + current_score, 'Simple Set'
    elif board[0][2][0] == board[1][1][0] == board[2][0][0]:
        return True, 10 + current_score, 'Simple Set'

    return False, current_score, "Lost"


def game(shuffle_deck, continues_steps, board):
    """
    Main game
    :param shuffle_deck:
    :param continues_steps:
    :param board:
    :return: boolean for true or false, score, category of win
    """
    print_board(board)
    choice = input(f'Score: {continues_steps}, Deal or Done? ').lower()
    if choice == 'deal':
        new_card, shuffle_deck = deal(shuffle_deck)
        index = list(map(int, input(f'New card: {new_card}, enter location to replace card <row col>: ').split()))
        board = update_card(board, new_card, index)
        return game(shuffle_deck, continues_steps - 1, board)
    elif choice == 'done':
        t, v, s = verify_matching(board, continues_steps)
        return t, v, s


def main():
    # create a deck
    deck = create_deck()

    # shuffle deck
    shuffle_deck = shuffle(deck)
    board, updated_deck = deal(shuffle_deck)

    continues_steps = 0
    is_won, score, category = game(shuffle_deck, continues_steps, board)

    if is_won:
        print(f'Congrats!! You\'ve got a {category} on the board, Score: {score}')
    else:
        print(f'You\'he lost the game with negative score of {score}.')


if __name__ == '__main__':
    main()
