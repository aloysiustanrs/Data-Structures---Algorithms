class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # At initialization only one Node , no head yet
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        temp = self.head
        llString = ''

        while temp:
            llString += str(temp.data)+'->'
            temp = temp.next

        print(llString)

    # Neetcode https://www.youtube.com/watch?v=G0_I-ZF0S38

    # Iterative using 2 pointers | T O(n) M O(1)
    def reverse_iterative(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # Recursive | T O(n) M O(n)
    # def reverse_recursive(self):
    #     if not head:
    #         return None


ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtBeginning(3)
ll.insertAtBeginning(3)
ll.insertAtBeginning(21)
ll.insertAtBeginning(3)
ll.reverse_iterative()
ll.print()
