"""
Jay Breen
Jan 2022

This is the binary / text conversion function module
"""

# import everything from the binary / text dictionary module
from binary_dict_module import *


def text_to_binary(text):
    output = ""

    for ch in text:
        output += text_convert.get(ch, ch) + " "
        # if the item doesn't exist in the dictionary then the second "ch" acts as the default
        # basically it will output the same that's been input
    return output


def binary_to_text(binary):
    bits = binary.split(" ")
    output = ""

    for ch in bits:
        output += binary_convert.get(ch, ch)
    return output
