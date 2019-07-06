from random import choice

defeated_by = dict(paper='scissors',
                   rock='paper',
                   scissors='rock')
lose = '{} beats {}, you lose!'
win = '{} beats {}, you win!'
tie = 'tie!'


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by.values()))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if defeated_by[computer_choice] == player_choice:
        return win.format(player_choice, computer_choice)
    elif defeated_by[player_choice] == computer_choice:
        return lose.format(computer_choice, player_choice)
    else:
        return tie


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    init = True
    while True:
        if init:
            print('Welcome to Rock Paper Scissors')
            init = False
        val = yield
        if val == 'q':
            raise StopIteration
        if val == None:
            print('Welcome to Rock Paper Scissors')
        print(_get_winner(_get_computer_move(), val))
