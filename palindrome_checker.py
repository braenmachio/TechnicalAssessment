#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:56:25 2026

@author: braen
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using a Two Pointer pattern on the sequence

    Parameters
    ----------
    s : str
        Input received from User

    Returns
    -------
    bool
        True is Palindrome else False
    """
    # intialize the pointer steps
    start = 0
    end = len(s) - 1

    # comparison loop to check start vs end
    while start < end:
        # check if characters at the position do not match
        if s[start] != s[end]:
            return False  # not a palindrome. Exit!

        # shift the pointers inwards

        start += 1
        end -= 1

    return True


print(is_palindrome(input(">  ")))
