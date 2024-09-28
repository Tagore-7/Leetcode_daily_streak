#Design your implementation of the circular double-ended queue (deque).
#
#Implement the MyCircularDeque class:
#
#MyCircularDeque(int k) Initializes the deque with a maximum size of k.
#boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
#boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
#boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
#int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
#int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
#boolean isEmpty() Returns true if the deque is empty, or false otherwise.
#boolean isFull() Returns true if the deque is full, or false otherwise.
# 
#
#Example 1:
#
#Input
#["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
#[[3], [1], [2], [3], [4], [], [], [], [4], []]
#Output
#[null, true, true, true, false, 2, true, true, true, 4]
#
#Explanation
#MyCircularDeque myCircularDeque = new MyCircularDeque(3);
#myCircularDeque.insertLast(1);  // return True
#myCircularDeque.insertLast(2);  // return True
#myCircularDeque.insertFront(3); // return True
#myCircularDeque.insertFront(4); // return False, the queue is full.
#myCircularDeque.getRear();      // return 2
#myCircularDeque.isFull();       // return True
#myCircularDeque.deleteLast();   // return True
#myCircularDeque.insertFront(4); // return True
#myCircularDeque.getFront();     // return 4
# 
#
#Constraints:
#
#1 <= k <= 1000
#0 <= value <= 1000
#At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull. 

# my solution 
class MyCircularDeque:

    def __init__(self, k: int):
        self.cdeque = deque(maxlen = k)
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.cdeque) > self.k - 1:
            return False
        self.cdeque.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.cdeque) > self.k - 1:
            return False
        self.cdeque.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.cdeque) == 0:
            return False
        self.cdeque.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.cdeque) == 0:
            return False
        self.cdeque.pop()
        return True

    def getFront(self) -> int:
        if len(self.cdeque) == 0:
            return -1
        value = self.cdeque[0]
        return value

    def getRear(self) -> int:
        if len(self.cdeque) == 0:
            return -1
        value = self.cdeque[-1]
        return value

    def isEmpty(self) -> bool:
        return len(self.cdeque) == 0
            
    def isFull(self) -> bool:
        return len(self.cdeque) == self.k 
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull(



# leet code


class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val 
        self.prev = prev 
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head 
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head 
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()






















