WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(1,size+1):
        line = ''
        for column in range(1,size+1):
            if column % 2 == 0 and row % 2 == 0:
                line += WHITE
            elif column % 2 != 0 and row % 2 == 0:
                line += BLACK
            elif column % 2 == 0 and row % 2 != 0:
                line += BLACK
            elif column % 2 != 0 and row % 2 != 0:
                line += WHITE
        print(line)

    