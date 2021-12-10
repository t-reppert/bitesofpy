def round_to_next(number: int, multiple: int):
    if number == 0 or multiple == 0:
        return 0
    if number % multiple == 0:
        return number
    else:
        while number % multiple != 0:
            if number < 0 and multiple < 0:
                number -= 1
            else:
                number += 1
        return number
