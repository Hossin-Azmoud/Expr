from collections import deque

class Stack:

    def __init__(self):
        self.base = list()
        self.mid: int = len(self.base) // 2
    
    def reverse(self):
        tmp = list()
        while len(self.base) > 0:
            tmp.append(self.base.pop())
        
        self.base = tmp


    def pop(self):
        if len(self.base) > 0: 
            return self.base.pop()

    def extend(self, list_):
        if len(list_) > 0:
            for i in list_:
                self.push(i)


    def push(self, data):
        self.base.append(data)

    def __len__(self) -> int: return len(self.base)

    def __repr__(self) -> str: return repr(self.base)
    
    def at(self, index) -> any:
        
        size = self.__len__()        
        if index >= 0 and index < size:
            return self.base[index]
        
        return None
            

    def peek(self):
        
        if len(self.base) > 0:
            return self.base[-1]
        
        return None

    @property
    def last(self) -> int: return len(self.base) - 1

    def __str__(self) -> str: return str(self.base)

    def __getitem__(self, item) -> int: return self.base.index(item)

    def __copy__(self) -> list: 
        cp = Stack()
        cp.extend(self.base)
        return cp

    def __sizeof__(self) -> int: return self.base.__sizeof__()

    def find(self, data: int) -> int or None:
        
        low = 0
        high = len(self.base)
        
        while low < high:
            mid = (low + high) // 2
            if self.base[mid] < data:
                low = mid + 1
            else:
                high = mid
        if low < len(self.base):
            if self.base[low] == data:
                return low
            else:
                return False
        else:
            return False

    def sortStack(self) -> bool:
        self.base.sort()
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

