'''
    Script:      ptm_test.py
    Description: Python pretty tree maker test harness
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        12 May 2020
'''

import ptm

# create a tree object
tree = ptm.Tree()

# add an element to the tree
tree.add("welcome", 1)
tree.add("this is a new level", 2)
tree.add("this follows the same level as above", 2)
tree.add("ohn wow back to level 1", 1)
tree.add("this is a new level", 2)
tree.add("this follows the same level as above", 2)
tree.add("lets stay on this level", 2)
tree.add("i like it here", 2)

# pretty print the tree!
tree.print()
