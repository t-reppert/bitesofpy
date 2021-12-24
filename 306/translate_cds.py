from Bio.Seq import Seq
import re

def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    cds = re.sub(r'[\t\n\W ]+', '', cds).upper()
    gene = Seq(cds)
    translation = gene.translate(table=translation_table, cds=True)
    return str(translation)