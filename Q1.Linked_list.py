
#Node is the structure which has the data and the next node's address in it
class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


# Creating a linked list 
class LinkedList():
    def __init__(self):
        self.head=None  # head stores the reference to the first node of the linked list

    def insert_at_begining(self,data):
        node = Node(data,self.head)  # create a new node whose next points to the current head
        self.head = node             # update head to the new node
    

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr=self.head
        linkedliststring=""

        while itr:
            linkedliststring+=str(itr.data) + "-->"
            itr=itr.next
        print(linkedliststring)

    


ll=LinkedList()

ll.insert_at_begining(89)
ll.insert_at_begining(5)
ll.insert_at_end(71)
ll.insert_at_end(795)
ll.insert_at_end(19887)
ll.print()

ll.insert_values(["apple orange,mango"])

ll.print()