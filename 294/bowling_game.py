def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    current_score = 0
    bowling = frames.replace('-','0')
    bowling = bowling.replace(' ','')
    bowling = bowling.upper()
    shots = [x for x in bowling]
    frame = 1
    i = 0
    throws = len(bowling)
    throw = 1
    while throws > 0:
        if shots[i] == 'X':
            # strike frame
            # Ten plus the neXt two shots
            current_score += 10
            if i+1 > len(shots) - 1:
                break
            if shots[i+1] == 'X':
                current_score += 10
                if shots[i+2] == 'X':
                    current_score += 10
                    if frame == 10:
                        break
                elif i+3 <= len(shots)-1 and shots[i+3] == '/':
                    current_score += int(shots[i+2])
                else:
                    current_score += int(shots[i+2])
                    if frame == 10:
                        break
            elif i+2 <= len(shots)-1 and shots[i+2] == '/':
                current_score += 10
                if frame == 10:
                    break
            else:
                if i+2 <= len(shots)-1:
                    current_score += int(shots[i+1]) + int(shots[i+2])
                    if frame == 10:
                        break
                else:
                    current_score += int(shots[i+1])
            throws -= 1
            throw += 1
            frame += 1
            i += 1
        elif i+1 <= len(shots)-1 and '/' in shots[i+1]:
            # spare frame - 10 plus the next shot
            if i+2 > len(shots) - 1:
                current_score += 10
                break
            if i+2 <= len(shots)-1 and shots[i+2] == 'X':
                current_score += 20
                if frame == 10:
                    break
            else:
                current_score += 10 + int(shots[i+2])
                if frame == 10:
                    break
            throws -= 2
            throw += 2
            frame += 1
            i += 2
        else:
            # open frame
            if i+1 <= len(shots) - 1:
                current_score += int(shots[i]) + int(shots[i+1])
            else:
                current_score += int(shots[i])
            throws -= 2
            throw += 2
            frame += 1
            i += 2
    return current_score