#Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: 
#(i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1.
# For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree
#which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false.
#All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.

from collections import Counter

def TreeConstructorTwo(strArr):
  try:
    parents = list(map(lambda x:x.replace('(','').replace(')','').split(',')[1],strArr))
    children = list(map(lambda x:x.replace('(','').replace(')','').split(',')[0],strArr))
    count_parents = Counter(parents)
    if count_parents.most_common(1)[0][1] > 2:
      return 'false'
    count_children = Counter(children)
    if count_children.most_common(1)[0][1] > 1:
      return 'false'
    roots = 0
    root_list = []
    for element in count_parents.elements():
      if element not in count_children.elements():
        if element not in root_list:
          root_list.append(element)
          roots +=1
    if roots != 1:
      return 'false'
    leafs = [node for node in count_children.keys() if node not in count_parents.keys()]
    root = [node for node in count_parents.keys() if node not in count_children.keys()]
    nodes = []
    for leaf in leafs:
      actual = leaf
      while actual != root[0]:
        index = children.index(actual)
        actual = parents[index]
        if index not in nodes:
          nodes.append(index)
    if len(nodes) != len(children):
      return 'false'

    return 'true'
  except IndexError:
    return 'true'

# keep this function call here 
print(TreeConstructorTwo(input()))