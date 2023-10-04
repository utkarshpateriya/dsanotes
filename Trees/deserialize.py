from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

A = [1,2,3,4,5,-1,-1,-1,-1,-1,-1]

def constructBT(A):
    n = len(A)
    root = TreeNode(A[0])
    queue = deque([(root,1)])
    pos = 1
    while queue:
        node, exists = queue.popleft()
        if exists == -1:
            continue
        else:
            if A[pos] != -1:
                node.left = TreeNode(A[pos])
                queue.append([node.left, 1])
            elif A[pos] == -1:
                queue.append([-1,-1])
            if A[pos+1] != 1:
                node.right = TreeNode(A[pos+1])
                queue.append([node.right, 1])
            elif A[pos+1] == -1:
                queue.append([-1,-1])
            pos+=1
    return root

print(constructBT(A))