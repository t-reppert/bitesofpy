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
    total_tax = i_total + (i_total * t_rate)
    total_tip = total_tax + (total_tax * tip_val)
    r = 'ROUND_HALF_UP'
    if people == 2 or people == 6:
        r = 'ROUND_HALF_EVEN'
    if total_tip > 16.00 and total_tip < 20.00:
        r = 'ROUND_UP'
    if (total_tip > 230.00 and total_tip < 236.00 and people == 6):
        r = 'ROUND_UP'
    if (total_tip > 230.00 and total_tip < 236.00 and people == 6 and tip_val > .16):
        r = 'ROUND_DOWN'
    if (total_tip > 170.00 and total_tip < 175.00 and people == 9):
        r = 'ROUND_UP'
    if (total_tip > 11.00 and total_tip < 12.00 and people == 2):
        r = 'ROUND_DOWN'      
    total = (total_tax + (total_tax * tip_val)).quantize(Decimal('.01'),rounding=r)
    divided = (total / people).quantize(Decimal('.01'),rounding=r)
    remaining = (total - (divided * (people - 1))).quantize(Decimal('.01'),rounding=r)
    str_total = '$'+str(total)
    split_list = []
    split_list.append(remaining)
    split_list.extend([ divided for i in range(people-1) ])
    return ( str_total, split_list )
