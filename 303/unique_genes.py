import gzip
from collections import defaultdict
from Bio import SeqIO, SeqRecord  # Recommended
from io import StringIO


def convert_to_unique_genes(filename_in, filename_out):
    """
    Takes a standard FASTA file or gzipped FASTA file,
    de-duplicates the file, sorts by number of occurrences and
    outputs the result in a standard FASTA file

    filename_in: str Filename of FASTA file containing duplicated genes
    filename_out: str Filename of FASTA file to output reduced file

    returns None
    """
    def process_records(f):
        gene_dict = defaultdict(list)
        gene_names = {}
        for record in SeqIO.parse(f, "fasta"):
            tag = record.description.split('=')
            tag = tag[1].rstrip(']')
            seq = str(record.seq).upper()
            name = record.name.lower()
            if seq in gene_names:
                if gene_names[seq].lower() != name:
                    raise NameError(f"Gene names differ between entries: '{gene_names[seq]}' vs. '{record.name}'")
            else:
                gene_names[seq] = name
            gene_dict[seq].append(tag)
        return gene_dict, gene_names

    if ".gz" in filename_in:
        with gzip.open(filename_in, 'rt') as f:
            gene_dict, gene_names = process_records(f)
    else:
        with open(filename_in) as f:
            gene_dict, gene_names = process_records(f)
    if ".gz" in filename_out:
        with gzip.open(filename_out, 'wt') as f:
            for k, v in sorted(gene_dict.items(), key=lambda x:len(x[1]), reverse=True):
                f.write(f">{gene_names[k]} [locus_tags={','.join(v)}]\n")
                f.write(f"{k}\n")
    else:
        with open(filename_out, 'wt') as f:
            for k, v in sorted(gene_dict.items(), key=lambda x:len(x[1]), reverse=True):
                f.write(f">{gene_names[k]} [locus_tags={','.join(v)}]\n")
                f.write(f"{k}\n")
