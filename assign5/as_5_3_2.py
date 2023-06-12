
# The recursive function
def VisitTwice(root, visited):
    visited[root] = true

    if not visited[root.left]:
        # traver this edge for the first time
        traverse(root, root.left)
        visited[root.left] = true
        # Recursive call
        VisitTwice(root.left, visited)
        # traver this edge for the second time
        # in reversed order
        traverse(root.left, root)

    # do the same for the right child
    if not visited[root.right]:
        traverse(root, root.right)
        visited[root.right] = true
        VisitTwice(root.right, visited)
        traverse(root.right, root)