STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    spaces = (rows * 2 - 2)//2
    points = 0
    xmas_tree = ""
    xmas_tree += " "*spaces + STAR + " "*spaces + "\n"
    for i in range(rows):
        line = " "*spaces+LEAF + LEAF*points + " "*spaces
        xmas_tree += line+"\n"
        spaces -= 1
        points += 2
    trunk_width = int(len(line) / 2) + (len(line) % 2 > 0)
    while (len(line) - trunk_width) % 2 != 0:
        trunk_width += 1
    trunk_spaces = (len(line) - trunk_width) // 2
    for i in range(2):
        line = " "*trunk_spaces + TRUNK*trunk_width + " "*trunk_spaces
        xmas_tree += line+"\n"
    return xmas_tree.rstrip()

