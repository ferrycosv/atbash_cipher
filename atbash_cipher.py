import re


def encode(input_string):
    res = ""
    for count, character in enumerate("".join(re.findall('[a-z]|[0-9]', input_string.lower()))):
        if re.search("[0-9]", character) is None:
            if count % 5 == 0 and count > 0:
                res += " "
            res += chr(ord("z") - ord(character) + ord("a"))
        else:
            res += character
    return res

