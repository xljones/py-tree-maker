'''
    Script:      ptm.py
    Description: Python pretty tree maker
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        12 May 2020
'''

import os
import sys
import uuid

'''
---- root branch with elements
    \
     ---- new branch - all of - its - elements
          \                     \
           --- can have lots     --- of elements on lots of branches

{
    "uuid" : "an element",
    "branch" : {
        "uuid" : "branch element 1",
        "uuid" : "branch element 2"
    ]}
]}
'''

_VERSION = "1.0.0"
_STYLES = {
    "Default": {
        "indent" : 4,
        "symbol_first": "┌── ", # used for the very first element or branch @ index 0, depth 0.
        "symbol_mid"  : "├── ", # used by all elements or branches that are not last in their depth.
        "symbol_last" : "└── ", # used by element or branch that is the last in its depth, OR
                                # by an branch which has > 0 sub-elements
    }
}

class Tree:
    _tree = None
    _style = None

    def __init__(self):
        self._tree = {}
        self._style = _STYLES["Default"]

    def _add_to_tree(self, new_key, new_value, path):
        ttree = self._tree # set a new tree to traverse and find the object at 'path'
        key_list = path.split(".")
        if key_list[0] != "":
            for key in key_list[:-1]:
                ttree = ttree[key]
            ttree[key_list[-1]][new_key] = new_value
        else:
            ttree[new_key] = new_value

    def _calc_symbol(self, index, depth, branch):
        if index == 0 and depth == 0:
            return self._style["symbol_first"]
        elif index == len(branch.items())-1:
            return self._style["symbol_last"]
        else:
            return self._style["symbol_mid"]

    def _print_branch(self, branch, depth):
        index = 0
        for id, element in branch.items():
            _symbol = self._calc_symbol(index, depth, branch)
            if type(element) == str:
               print("{0}{1}{2}".format(
                   " " * self._style["indent"] * depth,
                   _symbol, 
                   element))
            elif type(element) == dict:
                if (len(element) > 0):
                    _symbol = self._style["symbol_last"]
                print('{0}{1}{2}'.format(
                    " " * self._style["indent"] * depth,
                    _symbol, 
                    id))
                self._print_branch(element, depth+1)
            else:
                raise TypeError("Unexpected data type [{0}] in tree".format(type(object)))
            index += 1

    def add_branch(self, new_branch_id, path=""):
        self._add_to_tree(new_branch_id, {}, path)
        
    def add_element(self, new_element, path=""):
        self._add_to_tree(uuid.uuid4().hex, new_element, path)

    def print_tree(self, style="Default"):
        self._style = _STYLES[style]
        self._print_branch(self._tree, 0)

if (__name__ == "__main__"):
    print("'{0}' is a library and cannot be called directly, please see the README.md for this script".format(os.path.basename(__file__)))
