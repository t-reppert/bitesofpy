
def island_size(map_):
    """
    Input: the map
    Output: the perimeter of the island
    """
    p = 0
    height = len(map_)
    width = len(map_[0])
    for i in range(height):
        for j in range(width):
            if map_[i][j] == 1:
                if i == 0:
                    p += 1
                    if map_[i+1][j] == 0:
                        p += 1
                elif i == height - 1:
                    p += 1
                    if map_[i-1][j] == 0:
                        p += 1
                else:
                    if map_[i-1][j] == 0:
                        p += 1
                    if map_[i+1][j] == 0:
                        p += 1
                if j == 0:
                    p += 1
                    if map_[i][j+1] == 0:
                        p += 1
                elif j == width - 1:
                    p += 1
                    if map_[i][j-1] == 0:
                        p += 1
                else:
                    if map_[i][j-1] == 0:
                        p += 1
                    if map_[i][j+1] == 0:
                        p += 1
    return p