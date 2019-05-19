import requests
import operator
import json
STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    else:
        cap = cap.lstrip('$')
        if 'M' in cap:
            cap = cap.replace('M','')
            return float(cap)
        elif 'B' in cap:
            cap = cap.replace('B','')
            cap = float(cap) * 1000
            return cap


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_cap = 0.0
    for d in data:
        if industry == d['industry']:
            industry_cap += _cap_str_to_mln_float(d['cap'])
    return round(industry_cap,2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    top_symbol = ""
    top_cap = 0.0
    for d in data:
        cap = _cap_str_to_mln_float(d['cap'])
        if  cap > top_cap:
            top_cap = cap
            top_symbol = d['symbol']
    return top_symbol

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = {}
    for d in data:
        if 'n/a' in d['sector']:
            continue
        if d['sector'] in sectors:
            sectors[d['sector']] += 1
        else:
            sectors[d['sector']] = 1
    return (max(sectors.items(),key=operator.itemgetter(1))[0],min(sectors.items(),key=operator.itemgetter(1))[0])
    
