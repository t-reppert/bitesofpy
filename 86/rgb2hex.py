def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    r, g, b = rgb
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        r = hex(r).split('x')[-1].zfill(2).upper()
        g = hex(g).split('x')[-1].zfill(2).upper()
        b = hex(b).split('x')[-1].zfill(2).upper()
        return "#" + r + g + b
    else:
        raise ValueError
    
