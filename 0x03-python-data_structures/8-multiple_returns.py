#!/usr/bin/python3


def multiple_returns(sentence):
    """returns len of str with 1st char"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
