import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*argv):
    for i in range(len(argv[0])):
        row = ""
        for j in range(len(argv)):
            if j == len(argv) - 1:
                row += str(argv[j][i])
                yield row
            else:
                row += str(argv[j][i]) + SEPARATOR

