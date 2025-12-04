class stack:
    def __init__(self):
        self.st=[]
    def push(self,x):
        self.st.append(x)
    def pop(self):
        if self.st is None:
            return "underflow"
        return self.st.pop()
    def peek(self):
        if len(self.st)==0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.st)
    def isEmpty(self):
        return len(self.st)==0
    def display(self):
        if len(self.st)==0:
            return "stack is empty"
        for i in range(len(self.st)-1):
            print(self.st[i],end=" ")
    def minstack(self):
        return min(self.st)
   
        
if __name__=="__main__":
    s=stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print(s.pop())
    print(s.peek())
    print(s.isEmpty())
    print(s.size())
    print("minimum element in the stack",s.minstack())
    
#valid paramthesis,next greater, daily temperature, min stack
