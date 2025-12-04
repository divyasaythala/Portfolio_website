def validparanthesis(a):
    stack=[]
    left="([{"
    right=")]}"
    for char in a:
        if char in left:
            stack.append(char)
        if char in right:
            if right.index(char)!=left.index(stack.pop()):
                return False
    return True
a=input("")
print(validparanthesis(a))
