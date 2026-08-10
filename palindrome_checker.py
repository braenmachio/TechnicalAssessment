#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:56:25 2026

@author: braen
"""

import logging
from log_config import palindrome_logging

logger = logging.getLogger(__name__)


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
    logger.info("Starting palindrome check for string: '%s'", s)

    # initialize the pointer steps
    start = 0
    end = len(s) - 1

    # comparison loop to check start vs end
    while start < end:
        logger.debug(
            "Comparing indices: start=%d ('%s') vs end=%d ('%s')",
            start, s[start],
            end, s[end],
        )

        # check if characters at the position do not match
        if s[start] != s[end]:
            logger.warning(
                "Mismatch found: '%s' != '%s' at indices %d and %d. Not a palindrome.",
                s[start], s[end],
                start, end,
            )
            return False  # not a palindrome. Exit!

        # shift the pointers inwards
        start += 1
        end -= 1

    logger.info("Successfully verified string '%s' as a valid palindrome.", s)
    return True


if __name__ == "__main__":
    palindrome_logging()  # Triggers the file configurations behind the scenes

    try:
        print(is_palindrome(input(">  ")))
    except Exception:
        logger.exception("An unhandled runtime error occurred.")
