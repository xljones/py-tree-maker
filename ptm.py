'''
    Script:      ptm.py
    Description: Python pretty tree maker
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        12 May 2020
'''

import argparse
import os
import sys

_VERSION = "1.0.0"

class Branch:
    _text = None
    _level = -1

    def __init__(self, branch_text, branch_level):
        self._text = branch_text
        self._level = branch_level

    def edit(self, new_text, new_level):
        print("edit this branch")


class Tree:
    _tree = []
    _style = 0

    def __init__(self):
        print("init")

    def print(self):
        print("im printing!")
        print(self._tree)

    def add(self, text, level):
        new_branch = Branch(text, level)
        self._tree.append(new_branch)
        print("New branch '{0}' added at level {1}".format(text, level))

    def prune(self, count):
        print("prune the last {0} off the list".format(count))

    def pop(self):
        print("pop from top of list")

    def delete(self, index):
        print("delete the item at index {0}".format(index))

if (__name__ == "__main__"):
    print("This file 'ptm.py' is a library and cannot be called directly, please see the README.md for this script")
