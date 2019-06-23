# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:00:44 2018

@author: Olena

Week 3 homework Cesar Cipher

"""

"""
A cipher is a secret code for a language. In this case study, 
we will explore a cipher that is reported by contemporary Greek historians 
to have been used by Julius Caesar to send secret messages 
to generals during times of war.

The Caesar cipher shifts each letter of a message to another letter 
in the alphabet located a fixed distance from the original letter. 
If our encryption key were 1, we would shift h to the next letter i, i 
to the next letter j, and so on. If we reach the end of the alphabet, 
which for us is the space character, we simply loop back to a. 
To decode the message, we make a similar shift, except we move the same number 
of steps backwards in the alphabet.

"""
#-----------------------------------------------------------------------------
# Task 1
"""
The string library has been imported. Create a string called alphabet 
consisting of the lowercase letters of the space character space ' ', 
concatenated with string.ascii_lowercase at the end.
"""

import string as str

alphabet = " " + str.ascii_lowercase

"""
alphabet has already defined from the last exercise. 
Create a dictioalphabetnary with keys consisting of the characters in alphabet, 
and values consisting of the numbers from 0 to 26.
"""
positions = {}
keys = [l for l in alphabet]
values = [i for i in range(0,27)]
positions = dict( zip(keys, values))
    
"""
`alphabet` and `positions` have already been defined from previous exercises. 
Use `positions` to create an `encoded message` based on `message` where each 
character in `message` has been shifted forward by `key` position, 
as defined by `positions`. 
Note that you can ensure the result remains within 0-26 using result % 27

Store this as encoded_message.

"""
message = "hi my name is caesar"

def encode(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string

encoded_message = encode(message, key = 3)
print(encoded_message)



