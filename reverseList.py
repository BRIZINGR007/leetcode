class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
 
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        node=Node(data,self.head) # creating a node and the self.head connects to the previous nodes
        self.head=node #it is storing the current node so that it connects to the self.next when the previous line is called
    def display(self):
        print_val=self.head
        llstr=''
        while print_val:
            llstr+=(str(print_val.data)+' ')
            print_val=print_val.next
        print(llstr)
    def reverse(self):
        prev = None
        current=self.head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
a_llist.reverse()
print('The Linked list: ')
a_llist.display()