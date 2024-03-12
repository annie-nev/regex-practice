"""
Purpose: First question functions
Author: Annie_nev
Created:12.3.2024
"""
import re


def count_lines(the_text: any) -> int:
    """
    Counts lines in a text file
    :param the_text: file contents
    :return: number of lines
    """
    lines_list = re.findall("\n", the_text, re.S)
    return len(lines_list)


def get_z_row(the_text: any) -> str:
    """
    returns first row with capital Z
    :param the_text: file contents
    :return: line as string
    """
    the_z_line = re.search(".*Z.*\n", the_text)
    return the_z_line.group()
