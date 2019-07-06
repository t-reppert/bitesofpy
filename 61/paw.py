from collections import namedtuple
import random

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError
    total_actions = ACTIONS * (n//4)
    letters_total = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_chosen = letters_total[:n]
    cards = [ l+i for l in letters_chosen for i in ['1','2','3','4']]
    paw_cards = []
    action_choice = None
    for i in range(len(cards)):
        if len(total_actions) >= 1:
            action_choice = random.choice(total_actions)
            total_actions.remove(action_choice)
        else:
            action_choice = None

        card_choice = random.choice(cards)
        cards.remove(card_choice)
        paw_cards.append(PawCard(card=card_choice,action=action_choice))
    return paw_cards

