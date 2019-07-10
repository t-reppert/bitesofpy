DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def print_sequence_route(grid, start_coordinates=None):
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    gridlines = [ [ int(x) for x in line.replace('-','').split()] for line in grid.splitlines() if '|' not in line and line ]
    length = len(gridlines)
    size = length * length
    start = START_VALUE
    next_val = 0
    if start_coordinates == None:
        coords = [ (length-1)//2, (length-1)//2 ]
        
    else:
        coords = start_coordinates
    i = coords[0]
    j = coords[1]
    curr_direction = 'right'
    if start == gridlines[i][j]:
        
        print(str(gridlines[i][j])+' ',end='')
        
        while start < size:
            
            next_val = start + 1
            
            # check down for match           
            if i+1 <= length - 1:
                if gridlines[i+1][j] == next_val:
                    # found match down, increment i, print value, increment start
                    i += 1
                    if curr_direction == 'right':
                        print(DOWN)
                        curr_direction = 'down'
                        print(str(gridlines[i][j])+' ',end='')
                    else:
                        print(str(gridlines[i][j])+' ',end='')
                    
                    start += 1
                    
            # check up for match
            if i-1 >= 0:
                if gridlines[i-1][j] == next_val:
                    # found match up, decrement i, print value, increment start
                    i -= 1
                    if curr_direction == 'left':
                        print(UP)
                        curr_direction = 'up'
                        print(str(gridlines[i][j])+' ',end='')
                    else:
                        print(str(gridlines[i][j])+' ',end='')
                    start += 1
                    

            # check right for match
            if j+1 <= length - 1:
                if gridlines[i][j+1] == next_val:
                    # found match to right, increment j, print value, increment start
                    j += 1
                    if curr_direction == 'up':
                        print(RIGHT)
                        curr_direction = 'right'
                        print(str(gridlines[i][j])+' ',end='')
                    else:
                        print(str(gridlines[i][j])+' ',end='')
                    start += 1
                    
                    
            # check left for match
            if j-1 >= 0:
                if gridlines[i][j-1] == next_val:
                    # found match to left, decrement j, print value, increment start
                    j -= 1
                    if curr_direction == 'down':
                        print(LEFT)
                        curr_direction = 'left'
                        print(str(gridlines[i][j])+' ',end='')
                    else:
                        print(str(gridlines[i][j])+' ',end='')
                    start += 1
                    
                      
    else:
        raise ValueError('Bad grid configuration!')
    
