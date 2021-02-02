'''
    Script:      ptm.py
    Description: Python pretty tree maker
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        2 Feb 2021
'''

import os
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
        "indent"      : 4,      # the number of spaces to leave per increase in depth
        "symbol_first": "┌── ", # used for the very first element or branch @ index 0, depth 0.
        "symbol_mid"  : "├── ", # used by all elements or branches that are not last in their depth.
        "symbol_last" : "└── ", # used by element or branch that is the last in its depth, OR
                                # by an branch which has > 0 sub-elements
    }
}

class Tree:
    _tree = None
    _style = None

    ''' PRIVATE
        initialize the object with an empty tree
        and a default styling
    '''
    def __init__(self):
        self._tree = {}
        self._style = _STYLES["Default"]

    ''' PRIVATE
        add a new element or branch to the tree.
            elements use new_key = a UUID
                         new_value = the desired value of the element
            branches use new_key = the ID of the branch
                         new_value = {} (empty dict)
    '''
    def _add_to_tree(self, new_key, new_value, path):
        ttree = self._tree # set a new tree to traverse and find the object at 'path'
        key_list = path.split(".")
        if key_list[0] != "":
            for key in key_list[:-1]:
                ttree = ttree[key]
            ttree[key_list[-1]][new_key] = new_value
        else:
            ttree[new_key] = new_value

    ''' PRIVATE
        returns the symbol that should lead up
        to an element or a branch to create the tree
    '''
    def _calc_symbol(self, index, depth, branch, is_branch, element):
        if (len(element) > 0 and is_branch):    # is this a branch that contains no sub-elements?
           return self._style["symbol_last"]
        elif index == 0 and depth == 0:         # is this the first symbol of the entire tree?
            return self._style["symbol_first"]
        elif index == len(branch.items())-1:    # is this the last symbol of this branch?
            return self._style["symbol_last"]
        else:                                   # else, this must be a mid-way part of a branch
            return self._style["symbol_mid"] 

    ''' PRIVATE
        returns whether a value is a branch, 
        or if it is just an element. Raises a TypeError
        exception if the data type is unexpected
    '''
    def _is_branch(self, value):
        if type(value) == str: 
            return False
        elif type(value) == dict:
            return True
        else:
            raise TypeError("Unexpected data type [{0}] in tree".format(type(value)))

    ''' PRIVATE
        print an individual element (str) of the branch
        using the associated format for the depth

        TODO: improve tree tracing from parent branch to next
              parent branch
    '''
    def _print_element(self, symbol, data, depth):
        print("{0}{1}{2}".format(
            " " * self._style["indent"] * depth,
            symbol, 
            data))

    ''' PRIVATE
        prints the root_branch, recursively calls this function
        for each new branch found within the root_branch
    '''
    def _print_branch(self, root_branch, depth):
        index = 0
        for key, value in root_branch.items():
            element_is_branch = self._is_branch(value)
            symbol = self._calc_symbol(index, depth, root_branch, element_is_branch, value)
            if self._is_branch(value):
                self._print_element(symbol, key, depth)
                self._print_branch(value, depth+1)
            else:
                self._print_element(symbol, value, depth)
            index += 1

    ''' PUBLIC
        function to add a new branch to the tree
            new_branch_id : the name of the new branch to add
            path          : a dotnotation to the root of the new branch
                            defaults to use the tree root
    '''
    def add_branch(self, new_branch_id, path=""):
        self._add_to_tree(new_branch_id, {}, path)
        
    ''' PUBLIC
        function to add a new element to the tree
            new_element   : the name of the new branch to add
            path          : a dotnotation to the root of the new element
                            defaults to use the tree root
    '''
    def add_element(self, new_element, path=""):
        self._add_to_tree(uuid.uuid4().hex, new_element, path)

    ''' PUBLIC
        function to print the tree
            style (optional) : select a style to print with, 
                               defaults to using the default style
    '''
    def print(self, style="Default"):
        self._style = _STYLES[style]
        self._print_branch(self._tree, 0)

if (__name__ == "__main__"):
    # Uhoh, this is a library, do not pass go, do not collect $200.
    print("'{0}' is a library and cannot be called directly, please see the README.md for this script".format(os.path.basename(__file__)))
