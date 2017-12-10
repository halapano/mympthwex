class DoubleLinkedListNode(object):

    def __init__(self,value,nxt,prev):

        self.value = value
        self.nxt = nxt
        self.prev = prev

    def __repr__(self):

        nval = self.nxt and self.nxt.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value},{repr(nval)},{repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):

        self.begin = None
        self.end = None

    def push(self,obj):
        """Append a new value on the end of the list"""
        node = DoubleLinkedListNode(obj,None,None)
        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            self.end.nxt = node
            node.prev = self.end
            self.end = node

    def pop(self):
        """Removes the last item and returns it."""
        node = self.end
        if node == None:
            return None
        elif self.begin == self.end:
            self.begin = self.end =None
            return node.value
        else:
            self.end = node.prev
            self.nxt = None
            return node.value

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        cnt = 0
        while node:
            cnt +=1
            node = node.nxt
        return cnt


