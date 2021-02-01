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
myTree.print_tree()

myTree.add_branch("bra1")
myTree.add_element("el1")
myTree.add_element("el2", "bra1")
myTree.add_element("el3", "bra1")
myTree.add_branch("bra1a", "bra1")
myTree.add_element("el3", "bra1.bra1a")

#myTree.add_element("testonbra1", "bra1")
#myTree.add_element("test2onbra1", "bra1")

myTree.print_tree()

