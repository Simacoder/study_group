"""
Explanation
Initialization:

If the head is None or there's only one node without a cycle, return False.
Traversal:

Move slow one step (slow = slow.next).
Move fast two steps (fast = fast.next.next).
Cycle Detection:

If slow and fast meet, it means there's a cycle.
If fast or fast.next is None, it means there's no cycle.
This approach has a time complexity of 

O(n) and a space complexity of 

O(1), making it very efficient for detecting cycles in a linked list.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
