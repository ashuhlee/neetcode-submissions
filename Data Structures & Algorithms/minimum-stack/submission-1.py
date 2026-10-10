class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val <= self.min_st[-1]:
            self.min_st.append(val)
        else:
            self.min_st.append(self.min_st[-1])

    def pop(self) -> None:
        if not self.st:
            return -1
        self.st.pop()
        self.min_st.pop()
        
    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]
        
    def getMin(self) -> int:
        if not self.min_st:
            return -1
        return self.min_st[-1]
        
