class ListNode: 
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None  


class MyLinkedList:

    def __init__(self):
        self.head : ListNode = None         
        self.tail : ListNode = None
        

    def get(self, index: int) -> int:
        current_node = self.head 
        i = 0
        if index == 0: 
            return current_node.value
        while current_node: 
            if i == index:
                return current_node.value
            current_node = current_node.next 

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head == None: 
            self.head = new_node
            return
        current = self.head
        
        if self.head.next == None: 
            new_node.next = current
            current.prev = new_node
            self.head = new_node
        else:
            new_node.next = current
            next_node = current.next.
            
            
                    
        
        return

    def addAtTail(self, val: int) -> None:
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        pass

    def deleteAtIndex(self, index: int) -> None:
        pass


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(5)
obj.addAtHead(10)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)