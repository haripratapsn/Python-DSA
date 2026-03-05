class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Creating a Linked List
class LinkedList():
    def __init__(self):
        self.head = None  # head stores the reference to the first node

    # Insert element at the beginning
    def insert_at_begining(self, data):
        node = Node(data, self.head)  # new node points to current head
        self.head = node              # update head to new node

    # Insert element at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # Insert multiple values
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Get length of linked list
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    # Remove node at given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # Print linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        linkedliststring = ""

        while itr:
            linkedliststring += str(itr.data) + "-->"
            itr = itr.next

        print(linkedliststring)


# Testing the Linked List
ll = LinkedList()

ll.insert_at_begining(89)
ll.insert_at_begining(5)
ll.insert_at_end(71)
ll.insert_at_end(795)
ll.insert_at_end(19887)

ll.print()

ll.insert_values(["apple", "orange", "mango"])

ll.print()

ll.remove_at(2)

ll.print()