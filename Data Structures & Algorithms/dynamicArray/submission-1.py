class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        old_capacity = self.capacity
        self.capacity *= 2
        self.arr.extend([0] * old_capacity)

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
