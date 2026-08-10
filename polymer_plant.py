#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:28:16 2026

@author: braen
"""

import logging
from log_config import polymer_logging

# create a module level logger
logger = logging.getLogger(__name__) 


def reaction(polymer: str) -> str:
    """
    Outputs a stable and a fullt reacted polymer given a polymer chain input.

    Parameters
    ----------
    polymer : str
        Reactive | Passive elemets.

    Returns
    -------
    str
        Reacted chain.
    """

    # intialize the stack to hold the polymer
    polymer_stack = []

    # from the given chain: check if element exists in stack
    for monomer in polymer:
        # check for reactive pair
        if (
            polymer_stack  # existing
            and polymer_stack[-1] != monomer  # yX
            and polymer_stack[-1].lower() == monomer.lower()  # yY
        ):
            popped = polymer_stack.pop()
            logger.debug("Reaction Occured: %s%s ", monomer, popped)
        else:
            polymer_stack.append(monomer)
    return "".join(polymer_stack)


if __name__ == "__main__":
    polymer_logging()  # Safely binds to the log file before logic runs
    print(reaction("mJYBPpluUqQrleJjgGUWwTtsywWdDuMmNOSsLlfXxOtTCcFfgXxZGgthHb"))
