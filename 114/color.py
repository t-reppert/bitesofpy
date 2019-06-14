import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        if color.upper() in COLOR_NAMES:
            self.rgb = COLOR_NAMES[color.upper()]
        else:
            self.rgb = None
        self.color = color
    
    @classmethod
    def hex2rgb(cls, hexval):
        """Class method that converts a hex value into an rgb one"""
        if len(hexval) != 6 or '#' not in hexval:
            raise ValueError
        hexval = hexval.lstrip('#')
        return (int(hexval[0:1],base=16),int(hexval[2:3],base=16),int(hexval[4:5],base=16))

    @classmethod
    def rgb2hex(cls, rgbval):
        """Class method that converts an rgb value into a hex one"""
        if type(rgbval) != tuple or len(rgbval) != 3:
            raise ValueError
        elif max(rgbval) > 255 or min(rgbval) < 0:
            raise ValueError
        r,g,b = rgbval
        r = hex(r).lstrip('0x').zfill(2)
        g = hex(g).lstrip('0x').zfill(2)
        b = hex(b).lstrip('0x').zfill(2)
        return f'#{r}{g}{b}'

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb in COLOR_NAMES.values():
            return f'{self.rgb}'
        else:
            return 'Unknown'