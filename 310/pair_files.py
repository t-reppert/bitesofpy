import re


def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    matched = {}
    good_file_re = re.compile(r'^[\/a-zA-Z0-9_\.]+_[sS][1-9][0-9]*_[lL][0-9][0-9][1-9]_[rR][12]_[0-9][0-9][1-9]\.fastq\.gz$', flags=re.I)
    file_queue = filenames
    while file_queue:
        file = file_queue.pop()
        if not file_queue:
            break
        search_r1 = re.sub(r'_[rR][12]_', '_[rR]1_', file)
        search_r2 = re.sub(r'_[rR][12]_', '_[rR]2_', file)
        if re.match(search_r1, file):
            for f in filenames:
                if re.match(search_r2, f, re.I) and good_file_re.match(file):
                    matched[file] = f
                    file_queue.remove(f)
        elif re.match(search_r2, file):
            for f in filenames:
                if re.match(search_r1, f, re.I) and good_file_re.match(file):
                    matched[f] = file
                    file_queue.remove(f)
    return sorted(matched.items(), key=lambda x: x[1])


# Set up for your convenience during testing
if __name__ == "__main__":
    filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    for pair in pair_files(filenames):
        print(pair)