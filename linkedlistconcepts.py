class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)
    def get_length(self):
        count=0
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_begining(data)
            self.head=node
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                
                break
            itr.next
            count+=1
    def print(self):
        if self.head is None:
            print("LinKED List is Empty")
            return
        itr= self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
    def insert_value(self,data_list):

        for data in data_list:
            self.insert_at_end(data)

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_value([1,2,3,4,5])
    ll.insert_at(1,26)
    print(ll.get_length())
    ll.print()

