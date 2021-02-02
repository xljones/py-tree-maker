# py-tree-maker v1.0.0

Creates an ordered tree that can output with customizable styles.

## Usage

#### Creating a new tree

```py
import ptm
myTree = ptm.Tree()
```

#### Creating a style

You can add a new style to the `_STYLES` constant in `ptm.py`. It must have:
* `indent`
* `symbol_first`
* `symbol_mid`
* `symbol_last`

```
_STYLES = {
    "Default": {
        "indent"      : 4,      # the number of spaces to leave per increase in depth
        "symbol_first": "┌── ", # used for the very first element or branch @ index 0, depth 0.
        "symbol_mid"  : "├── ", # used by all elements or branches that are not last in their depth.
        "symbol_last" : "└── ", # used by element or branch that is the last in its depth, OR
                                # by an branch which has > 0 sub-elements
    },
    "New_Style": {
        "indent"      : 0,      # the number of spaces to leave per increase in depth
        "symbol_first": "",     # used for the very first element or branch @ index 0, depth 0.
        "symbol_mid"  : "",     # used by all elements or branches that are not last in their depth.
        "symbol_last" : "",     # used by element or branch that is the last in its depth, OR
                                # by an branch which has > 0 sub-elements
    }
}
```


#### Adding a new branch

```py
myTree.add_branch(the_branch_id [str], dot_notation_path_to_parent_branch [str])
```
#### Adding a new element

```py
myTree.add_element(the_element [str], dot_notation_path_to_parent_branch [str])
```

#### Printing the tree
```py
myTree.print_tree(style [str, optional])
```

## Example

```py
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

# print the tree
myTree.print()
# =>
# └── Recipe
#     └── Ingredients
#         ├── 100g plain flour
#         ├── 2 large eggs
#         ├── 300ml milk
#         ├── butter
#         ├── lemon
#         └── caster sugar
#     └── Instructions
#         └── It's a secret
#     └── Results
#         └── A mess
```
