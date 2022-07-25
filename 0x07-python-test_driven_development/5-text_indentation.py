#!/usr/bin/python3
"""
    My text indenter module
"""

def text_indentation(text):
    """ Prints a text with 2 new lines after
        each of these characters: ., ? and :
    Args:
        text(str): The size of the square
    Raises:
        TypeError:  If text is not a string
    """
    # Checks for errors
    if not type(text) is str:
        raise TypeError("text must be a string")

    characList = ['.', '?', ':']
    newText = ""
    for letter in text:
        newText += letter
        if letter in characList:
            newText += "\n"
            print(newText.strip(" "))
            newText = ""
    if letter not in characList:
        print(newText.strip(" "), end="")
