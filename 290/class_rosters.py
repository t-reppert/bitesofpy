import csv
import re


def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    output = []
    class_regex = re.compile(r'^[A-Z0-9\-]+')
    with open(input_file) as f:
        reader = csv.reader(f)
        for line in reader:
            student_id = line[0]
            year = 2020
            classes = line[2:]
            for c in line[2:]:
                if c:
                    class_check = class_regex.search(c)
                    if class_check:
                        output.append(f"{class_check.group(0)},{year},{student_id}")
    return output