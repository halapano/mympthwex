class SingleLinkedListNode(object):
    def __init__(self,value,nxt):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        nval = self.nxt and self.nxt.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.cnt = 0

    def push(self,obj):
        node = SingleLinkedListNode(obj,None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
            self.cnt +=1
        else:
            self.end.nxt = node
            self.end = node
            self.cnt += 1

    def pop(self):
        """remove the last item and return it"""
        if self.begin == None:
            return None
        elif self.begin == self.end:
            node = self.end
            self.begin = self.end = None
            return node.value
        else:
            node = self.begin
            while node.nxt != self.end:
                node = node.nxt
            self.end = node
            return self.end.nxt.value
            

    def shift(self,obj):
        """another name for push"""    

    def unshift(self):
        """remove the first item and return it"""
        
    def remove(self,obj):
        """find a matching item and remove it from the list"""

    def first(self):
        """return a reference to the first item,don't remvoe"""

    def last(self):
        """return a reference to the last item,does not remove"""

    def count(self):
        """count the number of elements in the list."""
        return self.cnt

    def get(self,index):
        """get the value at index."""

    def dump(self,mark):
        """debugging function that dumps the contents"""
