import csv
import os
from urllib.request import urlretrieve

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)

rps = [ "Rock", "Gun", "Lightning", "Devil", "Dragon", "Water", "Air",
        "Paper", "Sponge", "Wolf", "Tree", "Human", "Snake", "Scissors",
        "Fire" ]

def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    battle_table = {}
    with open(BATTLE_DATA,'r') as f:
        data = csv.DictReader(f)
        for row in data:
            for defender in rps:
                key = row['Attacker'] + "_" + defender
                value = row[defender]
                battle_table[key] = value
    return battle_table


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if player1 not in rps or player2 not in rps:
        raise ValueError
    key = player1+"_"+player2
    if defeat_mapping[key] == 'win':
        return player1
    elif defeat_mapping[key] == 'lose':
        return player2
    elif defeat_mapping[key] == 'draw':
        return "Tie"

