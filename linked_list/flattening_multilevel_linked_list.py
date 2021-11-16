def flatten(node):
    """
    merge same as merge 2 sorted lists
    """
    if node == None or node.right == None:
        return node
        
    node.right = flatten(node.right)
    res = merge(node, node.right)
    return res