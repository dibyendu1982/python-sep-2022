class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None 

class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertTail(self, val: int):
        self.tail.next = ListNode(val) 
        self.tail = self.tail
        
    def insertHead(self, val: int):
        current = self.head
        self.head = ListNode(val)
        self.head.next = current
        
    