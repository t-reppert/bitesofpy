from pathlib import Path
from urllib.request import urlretrieve
import re

tmp = Path('/tmp')
timings_log = tmp / 'pytest_timings.out'
if not timings_log.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
        timings_log
    )


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    bite_regex = re.compile(r'^(\d+) =+ (\d+) passed.* in ([0-9\.]+) seconds =+.*')
    tests = []
    for timing in timings:
        s = bite_regex.search(timing)
        if s:
            bite = s.group(1)
            passed = int(s.group(2))
            time = float(s.group(3))
            tests.append((bite, time/passed))
    return min(tests, key=lambda x:x[1])[0]
