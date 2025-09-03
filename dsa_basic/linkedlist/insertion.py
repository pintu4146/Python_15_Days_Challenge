from dsa_basic.linkedlist.node import Node

head = Node(0)
i = 1
currr = head
while i < 6:
    new_node = Node(i)
    currr.next = new_node
    currr = currr.next
    i += 1
curr = head
while curr:
    print(curr.data, end='->')
    curr = curr.next


# Insertion at the  middle of the LL
def insert_mid(head: Node, data:int):
    """

    :param head: type of Node class object
    """
    node_to_be_inserted = Node(data)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(f'\nmid node: {slow.data}')
    temp = slow.next
    slow.next = node_to_be_inserted
    node_to_be_inserted.next = temp
    return head


new_head = insert_mid(head, data=10)
curr = new_head
while curr:
    print(curr.data, end='->')
    curr = curr.next

