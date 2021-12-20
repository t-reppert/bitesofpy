import logging
from typing import List  # python 3.9 we can drop this

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger('app')



def sum_even_numbers(numbers: List[float]) -> float:
    """
    1. Of the numbers passed in sum the even ones
       and return the result.
    2. If all goes well log an INFO message:
       Input: {numbers} -> output: {ret}
    3. If bad inputs are passed in
       (e.g. one of the numbers is a str), catch
       the exception log it, then reraise it.
    """
    even_nums = []
    try:
        for n in numbers:
            if n % 2 == 0:
                even_nums.append(n)
        total = sum(even_nums)
    except TypeError:
        logger.exception(f"Bad inputs: {numbers}")
        raise TypeError('not all arguments converted during string formatting')
    logger.info(f"Input: {numbers} -> output: {total}")
    return total