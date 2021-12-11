import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    decoded_bytes = base64.b64decode(data)
    decoded = decoded_bytes.decode('ascii')
    new_list = []
    for d in decoded.splitlines()[1:]:
        l = d.split(',')
        new_list.append(l[2])
    return new_list