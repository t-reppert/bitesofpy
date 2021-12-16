import os
from urllib.request import urlretrieve
from collections import defaultdict, Counter
from pprint import pprint

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    table_list = translation_table_str.split('\n')
    new_table = [l.strip() for l in table_list if l]
    aa = new_table[0].lstrip('AAs  = ')
    base1 = new_table[2].lstrip('Base1  = ').replace('T','U')
    base2 = new_table[3].lstrip('Base2  = ').replace('T','U')
    base3 = new_table[4].lstrip('Base3  = ').replace('T','U')
    t_list = list(zip([''.join(t) for t in list(zip(base1,base2,base3))],aa))
    trans_table = dict(t_list)
    total_codons = 0
    codons = defaultdict(int)
    for line in sequences:
        seq_list = [line[i:i+3] for i in range(0, len(line), 3)]
        codon_count = Counter(seq_list)
        for k, v in codon_count.items():
            if k in trans_table:
                codons[k] += v
                total_codons += v
    title = "|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |\n"
    hr = "---------------------------------------------------------------------------------------------------------\n"
    s = title + hr
    for i in range(0, 64, 16):
        d = {
            't_list': t_list,
            'codons': codons,
            'total': total_codons
        }
        s += f"|  {values(d, i)}  |  {values(d, i+4)}  |  {values(d, i+8)}  |  {values(d, i+12)}  |\n"
        s += f"|  {values(d, i+1)}  |  {values(d, i+5)}  |  {values(d, i+9)}  |  {values(d, i+13)}  |\n"
        s += f"|  {values(d, i+2)}  |  {values(d, i+6)}  |  {values(d, i+10)}  |  {values(d, i+14)}  |\n"
        s += f"|  {values(d, i+3)}  |  {values(d, i+7)}  |  {values(d, i+11)}  |  {values(d, i+15)}  |\n"
        s += hr
    return s

def values(d, i):
    t_list = d['t_list']
    codons = d['codons']
    total_codons = d['total']
    return f"{t_list[i][0]}:  {t_list[i][1]:<2}  {round((codons[t_list[i][0]]/total_codons)*1000,1):>4}  {codons[t_list[i][0]]:>5}"


if __name__ == "__main__":
    print(return_codon_usage_table())



