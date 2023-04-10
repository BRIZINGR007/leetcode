class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert_at_end(self,data):
        if self.ahead is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(data,None)
    def insert_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
        return self.head
class Solution:
    def removeNthFromEnd(self, head, n):
        itr=head
        length=self.get_length(head)
        if length==1:
            head=None
            return
        if length==n:
            head=head.next
        count=1
        while itr:
            if count==(length-n):
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
        return head
    def get_length(self,head):
        count=1
        itr=head
        while itr.next:
            count+=1
            itr=itr.next
        return count        

if __name__=="__main__":
    call=LinkedList()
    ll=call.insert_value([1,2])
    zx=Solution()
    dl=zx.removeNthFromEnd(ll,2)
    print("Hello")

