from datetime import date
from typing import Dict, Sequence, NamedTuple
from collections import defaultdict

class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    months = defaultdict(int)
    for item in renting_history:
        months[item.date.strftime("%Y-%m")] += item.price
    new_dict = {}
    for month, value in months.items():
        if value > STREAMING_COST_PER_MONTH:
            new_dict[month] = 'stream'
        else:
            new_dict[month] = 'rent'
    return new_dict