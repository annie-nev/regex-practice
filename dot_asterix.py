import re


def count_lines(the_text):
    lines_list = re.findall("\n", the_text, re.S)
    return len(lines_list)

