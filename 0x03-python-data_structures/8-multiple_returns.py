#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_character = None
    else:
        firs_character = sentence[0]

    new_tuple = (len(sentence), first_character)

    return (new_tuple)
