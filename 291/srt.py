from datetime import timedelta, datetime
from typing import List
import re


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    section_regex = re.compile(r'([0-9]+)\n([0-9\:]+),[0-9]+ --> ([0-9\:]+),[0-9]+\n(.*)',re.I)
    lines = re.split('\n\n', text)
    sections = {}
    for line in lines:
        found = section_regex.search(line)
        num = found.group(1)
        t1 = found.group(2)
        t2 = found.group(3)
        chars = len(found.group(4))
        time1 = datetime.strptime(t1, "%H:%M:%S")
        time2 = datetime.strptime(t2, "%H:%M:%S")
        diff = time2 - time1
        sections[int(num)] = chars / diff.total_seconds()
    return sorted(sections.keys(), key=lambda k:sections[k], reverse=True)
