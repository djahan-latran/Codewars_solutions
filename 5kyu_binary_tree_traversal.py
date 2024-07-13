# Given the root node of a binary tree (but not necessarily a binary search tree,)
# write three functions that will print the tree in pre-order, in-order, and post-order.
#
# A Node has the following properties:
#
# data    # A number or a string
# left    # A Node, which is None if there is no left child.
# right   # A Node, which is None if there is no right child.


"""My solution"""
# Pre-order traversal
def pre_order(node):
    results = []

    if node is None:
        return results

    def traverse(current_node):

        results.append(current_node.data)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(node)
    return results


# In-order traversal
def in_order(node):
    results = []

    if node is None:
        return results

    def traverse(current_node):

        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.data)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(node)
    return results


# Post-order traversal
def post_order(node):
    results = []

    if node is None:
        return results

    def traverse(current_node):

        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.data)

    traverse(node)
    return results