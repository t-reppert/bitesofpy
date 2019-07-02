from functools import singledispatch
from itertools import compress
import re
from datetime import datetime

@singledispatch
def count_down(data_type):
    if type(data_type) == compress or type(data_type) == re.Pattern or type(data_type) == datetime:
       raise ValueError
    data = [ x for x in str(data_type) ]
    process_data(data)

@count_down.register
def _(data_type: list):
    data = [ str(x) for x in data_type ]
    process_data(data)
    
@count_down.register
def _(data_type: tuple):
    data = [ str(x) for x in data_type ]
    process_data(data)

@count_down.register
def _(data_type: set):
    data = sorted([str(x) for x in data_type])
    process_data(data)

@count_down.register
def _(data_type: dict):
    data = [ str(x) for x in data_type.keys()]
    process_data(data)

@count_down.register
def _(data_type: range):
    data = [ str(x) for x in data_type]
    process_data(data)

def process_data(data):
    while data:
        print(''.join(data))
        data.pop()