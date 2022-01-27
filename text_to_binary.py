"""
Jay Breen
Jan 2022

Main binary / text app
"""

# import the binary conversion module
from binary_conversion_module import *

choose = ""

while choose != "quit" or "q":
    choose = input("(B)inary to text, (T)ext to binary, (Q)uit? > ").lower()
    if choose == "b":
        input_text = input("Input binary to convert to text > ").lower()
        print(binary_to_text(input_text))
    elif choose == "t":
        input_text = input("Input text to convert to binary > ").lower()
        print(text_to_binary(input_text))
    elif choose == "quit" or "q":
        break

