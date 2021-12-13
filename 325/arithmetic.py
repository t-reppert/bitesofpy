from typing import Generator
from decimal import Decimal
import decimal
import json
VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"


def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    decimal.getcontext().prec = 4
    floats = json.loads(values)
    length = len(floats)
    for idx,f in enumerate(floats):
        if idx < length-1:
            total = Decimal(floats[idx] + floats[idx+1]).quantize(Decimal("1.000"))
            yield f"The sum of {floats[idx]} and {floats[idx+1]}, rounded to two decimal places, is {total:.2f}."