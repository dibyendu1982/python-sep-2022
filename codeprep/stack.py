class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        self.stack.pop()
        
test = Stack()

test.push(1)
test.push(3)
test.push(5)
test.push(6)
test.pop()
test.pop()
print(test)