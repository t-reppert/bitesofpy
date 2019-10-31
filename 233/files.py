from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile
import os
import time

TMP = Path('/tmp')
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    logs = list(directory.glob('*.log'))
    last_n_sorted_logs = sorted(logs, key=lambda x: os.path.getctime(x))[-n:]

    with ZipFile(zip_file, 'w') as new_zip:
        for name in last_n_sorted_logs:
            ctime = time.ctime(os.path.getctime(name))
            cdate = datetime.strptime(ctime, "%a %b %d %H:%M:%S %Y")
            date = cdate.strftime('%Y-%m-%d')
            shortname = os.path.basename(name.with_suffix(''))
            arcname = shortname + '_' + date + '.log'
            new_zip.write(str(name), arcname=arcname)
        

