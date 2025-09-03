
from dsa_basic.linkedlist.node import Node


head = Node(0)
curr = head
currr = head
i = 1
while i < 6:
    new_node = Node(i)
    currr.next = new_node
    currr = currr.next
    i += 1
curr = head
while curr:
    print(curr.data, end=' -> ')

    curr = curr.next
print('None ')


class Solution:
    def reverseList(self, head):
        pre = None
        current = head
        # nxt = None
        while current:
            nxt = current.next
            current.next = pre
            pre = current
            current = nxt
        head = pre
        return head


obj = Solution()
rev = obj.reverseList(head)
while rev:
    print(rev.data, end=' -> ')

    rev = rev.next
print('None ')

