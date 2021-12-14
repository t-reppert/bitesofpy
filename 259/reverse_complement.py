# See tests for a more comprehensive complementary table
SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


# Recommended helper function
def _clean_sequence(sequence, str_table):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    table =  [s.strip() for s in str_table.split('\n')[2:] if s]
    table_dict = {s.split('\t')[0]:s.split('\t')[-1] for s in table}
    if isinstance(sequence, list):
        sequence = ''.join(sequence)
    sequence = sequence.upper()
    return_seq = ''.join([i for i in sequence if i in table_dict])
    return return_seq, table_dict


def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    sequence, table = _clean_sequence(sequence, str_table)
    return_seq = ''.join(list(reversed(sequence)))
    return return_seq


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    sequence, table = _clean_sequence(sequence, str_table)
    return_seq = ''.join([table[i] for i in sequence if i in table])
    return return_seq


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """
    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    sequence, table = _clean_sequence(sequence, str_table)
    return_seq = ''.join(list(reversed([table[i] for i in sequence if i in table])))
    return return_seq