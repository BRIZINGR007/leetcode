class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def insert_at_end(self,data_list):
        dummy=Node()
        curr=dummy
        for data in data_list:
            curr.next=Node(data)
            curr=curr.next
        return dummy.next
class Solution:
    def middleNode(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        


if __name__=="__main__":
    call=LinkedList()
    call2=LinkedList()
    ll1=call.insert_at_end([1,2,3,4,5])
    zx=Solution()
    zx.middleNode(ll1)
    print("Hello")

