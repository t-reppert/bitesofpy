import re

position = { k: v for k,v in enumerate(['Su','Mo','Tu','We','Th','Fr','Sa'])}

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    cal_rx = re.compile(r'[0-9]+')
    cal = {}
    for line in calendar_output.splitlines()[2:]:
        pos = 0
        while line:
            col_data = line[:2]
            if line:
                line = line[3:]
            else:
                break
            if cal_rx.search(col_data):
                cal[int(col_data)] = position[pos]
            pos += 1
    return cal
            



    