from collections import deque

class Stack:

    def __init__(self):
        self.stack = list()
        self.mid: int = len(self.stack) // 2

    def pop(self):

        if len(self.stack) > 0:
            return self.stack.pop()

    def extend(self, list_):
        if len(list_) > 0:
            for i in list_:
                self.push(i)


    def push(self, data):
        self.stack.append(data)


    def __len__(self) -> int: return len(self.stack)

    def __repr__(self) -> str: return repr(self.stack)

    def peek(self):
        
        if len(self.stack) > 0:
            return self.stack[-1]
        
        return None

    @property
    def last(self) -> int: return len(self.stack) - 1

    def __str__(self) -> str: return str(self.stack)

    def __getitem__(self, item) -> int: return self.stack.index(item)

    def __copy__(self) -> list: 
        cp = Stack()
        cp.extend(self.stack)
        return cp

    def __sizeof__(self) -> int: return self.stack.__sizeof__()

    def find(self, data: int) -> int or None:
        
        low = 0
        high = len(self.stack)
        
        while low < high:
            mid = (low + high) // 2
            if self.stack[mid] < data:
                low = mid + 1
            else:
                high = mid
        if low < len(self.stack):
            if self.stack[low] == data:
                return low
            else:
                return False
        else:
            return False

    def sortStack(self) -> bool:
        self.stack.sort()
        return True


class Queue(object):

    def __init__(self):
        self.queue = deque()

    def pushLeft(self, item) -> None:

        if isinstance(item, list):
            for i in item:
                self.queue.appendleft(i)
        elif isinstance(item, int or str or bool):
            self.queue.appendleft(item)

    def pushRight(self, item) -> None:
        if isinstance(item, list):
            for i in item:
                self.queue.append(i)
        
        elif isinstance(item, int or str or bool):
            self.queue.append(item)

    def __copy__(self) -> deque:
        return self.queue

    def __repr__(self) -> str:
        return repr(self.queue)

    def __getitem__(self, item) -> int:
        return self.queue.index(item)

    def __str__(self) -> str:
        return str(self.queue)

    def __len__(self) -> int:
        return len(self.queue)

    def peek(self):
       if len(self.queue) > 0:
            return self.queue[-1]

    def popLeft(self) -> None:
       self.queue.popleft()

    def popRight(self) -> None:
       self.queue.pop()

