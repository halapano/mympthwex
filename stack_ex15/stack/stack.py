class StackNode(object):

    def __init__(self,value,nxt):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        nval = self.nxt and self.nxt.value or None
        return f"[{self.value},{repr(nval)}]"


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self,obj):
        """push a new value to the top of the stack"""
        node  = StackNode(obj,None)
        node.nxt = self.top
        self.top = node

    def pop(self):
        """pop the value on the top and remove it"""
        if self.top  == None:
            return None
        else:
            node  = self.top
            self.top = self.top.nxt
            return node.value
            
    def top(self):
        """return a reference to the top item,does not remove"""

    def count(self):
        """count the number of elements"""
        tmpNode  = self.top
        cnt = 0
        while tmpNode:
            cnt += 1
            tmpNode = tmpNode.nxt
        return cnt
        
    def dump(self,mark="----"):
        """debug, dumps the contents of the stack"""
