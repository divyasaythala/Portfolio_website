class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False
def getNode():
    return TrieNode()
def insert(root,key):
    curr=root
    for c in key:
        index=ord(c)-ord('a')
        if curr.children[index] is None:
            newNode=TrieNode()
            curr.children[index]=getNode()#as we are inserting new key, we are assigning the index to the new key
        curr=curr.children[index]#iterating
    curr.isEndOfWord=True#after successfully inserting we mark end as true
def search(root,key):
    curr=root
    for c in key:
        index=ord(c)-ord('a')
        if curr.children[index] is None:#base case for all
            return False
        curr=curr.children[index]#iterates until the condition fails 
    return curr.isEndOfWord
def prefixsearch(root,search):
    curr=root
    for c in key:
        index=ord(c)-ord('a')
        if curr.children[index] is None:
            return False
        curr=curr.children[index]
    return True
def remove(root,key,depth=0):
    if root is None:
        return None

    if depth == len(key):
        if root.isEndOfWord:
            root.isEndOfWord = False
        if all(child is None for child in root.children):
            return None
        return root

    index = ord(key[depth]) - ord('a')
    root.children[index] = remove(root.children[index], key, depth + 1)

    if all(child is None for child in root.children) and not root.isEndOfWord:
        return None

    return root
if __name__=='__main__':
    root=getNode()
    keys=["the","a","there","answer","any","by","bye","their","hero","heroplane"]
    for key in keys:
        insert(root,key)
    if search(root,"the"):
        print("Yes")
    else:
        print("No")
    root=remove(root,"heroplane")
    if search(root,"hero"):
        print("yes")
    print("no")
