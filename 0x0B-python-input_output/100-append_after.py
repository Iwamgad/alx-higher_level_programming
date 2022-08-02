#!/usr/bin/python3
"""My file writer module"""

def append_after(filename="", search_string="", new_string=""):
    """Insert a text to a file, after each line containing a special string"""
    document = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            document.append(line)
            if line.find(search_string) != -1:
                document.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        for line in document:
            f.write(line)
