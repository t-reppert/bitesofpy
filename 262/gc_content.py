from collections import Counter
import re

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = re.sub(r'[\?\.\,\!\/ \n]','',sequence)
    sequence = sequence.lower()
    c = Counter(sequence)
    gc = sum([v for k,v in c.items() if k in ['g','G','c','C']])
    total = sum(c.values())
    return round((gc/total * 100), 2)