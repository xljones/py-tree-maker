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

class Tree:
    _tree = None

    def __init__(self):
        self._tree = {}

    def add_branch(self, new_branch_id, path=""):
        obj = self._tree
        key_list = path.split(".")
        if key_list[0] != "":
            for k in key_list[:-1]:
                obj = obj[k]
            obj[key_list[-1]][new_branch_id] = {}
        else:
            obj[new_branch_id] = {}

    def add_element(self, new_element, path=""):
        obj = self._tree
        key_list = path.split(".")
        if key_list[0] != "":
            for k in key_list[:-1]:
                obj = obj[k]
            obj[key_list[-1]][uuid.uuid4().hex] = new_element
        else:
            obj[uuid.uuid4().hex] = new_element

    def print_tree(self):
        #print(self._tree)
        self._print_branch(self._tree, 0)
    
    def _print_branch(self, branch, depth):
        for id, element in branch.items():
            if type(element) == str:
               print("## [e] {0}{1}".format("--" * depth, element))
            elif type(element) == dict:
                print('## [b] {0}{1}'.format("--" * depth, id))
                self._print_branch(element, depth+1)
            else:
                raise TypeError("Unexpected data type [{0}] in tree".format(type(object)))

if (__name__ == "__main__"):
    print("'{0}' is a library and cannot be called directly, please see the README.md for this script".format(os.path.basename(__file__)))
