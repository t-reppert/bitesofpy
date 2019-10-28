THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs(int):
    def __mul__(self, other):
        if other < 4 and other > 0:
            return THUMBS_UP * other
        elif other >= 4:
            return f'{THUMBS_UP} ({other}x)'
        elif other < 0 and other > -4:
            return THUMBS_DOWN * abs(other)
        elif other <= -4:
            return f'{THUMBS_DOWN} ({abs(other)}x)'
        elif other == 0:
            raise ValueError('Specify a number')

    def __rmul__(self, other):
        if other < 4 and other > 0:
            return THUMBS_UP * other
        elif other >= 4:
            return f'{THUMBS_UP} ({other}x)'
        elif other < 0 and other > -4:
            return THUMBS_DOWN * abs(other)
        elif other <= -4:
            return f'{THUMBS_DOWN} ({abs(other)}x)'
        elif other == 0:
            raise ValueError('Specify a number')
