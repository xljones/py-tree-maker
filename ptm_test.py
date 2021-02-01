'''
    Script:      ptm_test.py
    Description: Python pretty tree maker test harness
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        12 May 2020
'''

import ptm

# create a tree object
myTree = ptm.Tree()

# add an element to the tree
myTree.add_element("root1")
myTree.add_branch("bra1")
myTree.add_element("el1", "bra1")
myTree.add_element("el2", "bra1")
myTree.add_branch("bra2")
myTree.add_branch("bra3")
myTree.add_element("el3", "bra2")

myTree.print_tree()

