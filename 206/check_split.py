from decimal import *

def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    i_total = Decimal(item_total.strip('$'))
    t_rate = Decimal(tax_rate.strip('%'))/100
    tip_val = Decimal(tip.strip('%'))/100

    total_with_tax = (i_total + i_total * t_rate).quantize(Decimal('.01'))
    grand_total = (total_with_tax + total_with_tax * tip_val).quantize(Decimal('.01'))

    divided = (grand_total / people).quantize(Decimal('.01'),rounding=ROUND_DOWN)
    remaining = (grand_total - (divided * (people - 1))).quantize(Decimal('.01'))
    str_total = f'${grand_total}'
    split_list = []
    split_list.append(remaining)
    split_list.extend([ divided for i in range(people-1) ])
    return ( str_total, split_list )
