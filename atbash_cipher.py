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

<<<<<<< HEAD
=======


>>>>>>> 1e666c45f81b887dfbacb81219d785d886f5399c
def decode(text):
    alpha='a'
    alphabet=[]
    for i in range(26):
        alphabet.append(alpha)
        alpha = chr(ord(alpha) + 1)
    regular_alphabet=alphabet.copy()
    alphabet.reverse()
    encode_dict = dict(zip(regular_alphabet,alphabet))
<<<<<<< HEAD
    decode_dict = dict(zip(alphabet,regular_alphabet))  
    text=text.replace(' ','')
=======
    decode_dict = dict(zip(alphabet,regular_alphabet))
>>>>>>> 1e666c45f81b887dfbacb81219d785d886f5399c
    reply=""
    for i in text:
        reply=reply+decode_dict[i]
    return reply 
