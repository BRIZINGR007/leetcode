from operator import ne


class Node:
    def __init__(self,val=None,next=None) -> None:
        self.val=val
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
   def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        length,tail=1,head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        curr=head
        for i in range(length-k-1):
            curr=curr.next
        newHead=curr.next
        curr.next=None
        tail.next=head
        return newHead

        
       
if __name__=="__main__":
    call=LinkedList()
    ll1=call.insert_at_end([1,2,3,4,5])
    zx=Solution()
    rl=zx.rotateRight(ll1,2)
    print("JJJJ")
