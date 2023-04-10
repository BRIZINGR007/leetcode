class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert_value_at_end(self,data_list):
        dummy=Node()
        curr=dummy
        for data in data_list:
            curr.next=Node(data)
            curr=curr.next
        return dummy.next
        
if __name__=="__main__":
    call=LinkedList()
    call2=LinkedList()
    ll1=call.insert_value([2,4,3])
    ll2=call2.insert_value([5,6,4])
    print("h")