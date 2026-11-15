class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        self.left.next = self.right
        self.right.prev = self.left

    def is_empty(self):
        return self.left.next == self.right

    def enqueue(self, val):
        node = ListNode(val)

        prev = self.right.prev
        next_node = self.right

        node.next = next_node
        node.prev = prev

        prev.next = node
        next_node.prev = node

    def dequeue(self):
        if self.is_empty():
            return None

        node = self.left.next
        val = node.val

        self.left.next = node.next
        node.next.prev = self.left

        return val

    def peek(self):
        if self.is_empty():
            return None

        return self.left.next.val


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1.enqueue(x)

        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()  


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()