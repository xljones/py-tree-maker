'''
    Script:      ptm_test.py
    Description: Python pretty tree maker example
    Author:      Xander Jones (xander@xljones.com)
    Web:         xljones.com
    Date:        2 Feb 2021
'''

# import the lib
import ptm

# create a new tree
myTree = ptm.Tree()

# adding a branch on the tree root
myTree.add_branch("Recipe")

# adding a branch onto the branch "Recipe"
myTree.add_branch("Ingredients", "Recipe")
ingredients = ["100g plain flour", "2 large eggs", "300ml milk", "butter", "lemon", "caster sugar"]
for ingredient in ingredients:
    myTree.add_element(ingredient, "Recipe.Ingredients")

myTree.add_branch("Instructions", "Recipe")
myTree.add_element("It's a secret", "Recipe.Instructions")

myTree.add_branch("Results", "Recipe")
myTree.add_element("A mess", "Recipe.Results")

myTree.print()
