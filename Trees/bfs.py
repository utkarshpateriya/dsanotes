import collections
# Make a tree first
class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

Node = ListNode(3)
Node.left = ListNode(9)
Node.right = ListNode(20)
Node.right.left = ListNode(15)
Node.right.right = ListNode(7)

def verticalOrderTraversal(A):
	root = A
	if not root:
		return []
	column_items = collections.defaultdict(list)
	queue = collections.deque([(root,0)])
	min_x = float('inf')
	max_x = float('-inf')
	res = []
	while queue:
		node, x = queue.popleft()
		column_items[x].append(node.val)
		min_x = min(min_x,x)
		max_x = max(max_x,x)
		if node.left:
			queue.append((node.left, x-1))
		if node.right:
			queue.append((node.right, x+1))
	
	for level in range(min_x, max_x):
		res.append(column_items[level])
	return res

print(verticalOrderTraversal(Node))