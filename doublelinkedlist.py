class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DLinkedList:
    def __init__(self) -> None:
        self.head = None
    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None,itr)
    def get_length(self):
        count=0
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index ==0:
            self.insert_at_begining(data)
            return
        itr = self.head
        count=0
        while itr:
            if count == index-1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr=itr.next
            count=count+1

        
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            self.head.prev = None
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                break
            itr=itr.next
            count+=1

    def print_forward(self):
        itr = self.head
        dllstr=""
        while itr:
            dllstr+=str(itr.data)+"-->"
            itr = itr.next
        print(dllstr)
    def insert_value(self,list):
        for data in list:
            self.insert_at_end(data)
if __name__=="__main__":
    ll=DLinkedList()
    ll.insert_value([1,2,3,4,5])
    ll.insert_at(2,24)

    ll.print_forward()s