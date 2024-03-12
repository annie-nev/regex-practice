import re


def count_lines(the_text):
    lines_list = re.findall("\n", the_text, re.S)
    return len(lines_list)


def get_z_row(the_text):
    the_z_line = re.search(".*Z.*\n", the_text)
    return the_z_line.group()
