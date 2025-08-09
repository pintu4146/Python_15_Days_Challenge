class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Data: {self.data} and next pointer: {self.next} '


class LinkedListOperations:

    def __init__(self):
        self.head = Node(10)

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        return new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next



head = Node(10)
current = head

for i in range(1, 10):
    new_node = Node(i * 10)
    current.next = new_node  # link current node to new node
    current = new_node  # move current to the new node

# print(head)
while head is not None:
    print(head.data, end=' -> ')
    head = head.next


ll=LinkedListOperations()
ll.insert_at_begining(20)
ll.insert_at_end(100)
print()
ll.print_list()
