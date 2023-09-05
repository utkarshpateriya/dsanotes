class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(0)
head.next = ListNode(10)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(3)
B = 3

# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
