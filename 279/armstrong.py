def is_armstrong(n: int) -> bool:
    digits = [int(x) for x in str(n)]
    numlen = len(digits)
    arm = sum([ x**numlen for x in digits])
    if n == arm:
        return True
    return False