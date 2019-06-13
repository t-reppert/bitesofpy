import os
import glob
ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    files = glob.glob(dirname+'*')
    return list(filter( lambda x: (os.stat(x).st_size/ONE_KB) >= size_in_kb ,files))