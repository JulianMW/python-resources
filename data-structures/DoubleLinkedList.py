# DoublyLinkedLists

class Node(object):

    def __init__(self, prev = None, data=None, next = None):
        self._prev = prev
        self._data = data
        self._next = next

    def __str__(self):
        return str(self._data)
    def __repr__(self):
        return "Node(%s,%s,%s)" % (repr(self._prev), repr(self._data), repr (self._next))

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self._prev == other._prev and self._data == other._data and self._next == other._next`enter code here`

class DoublyLinkedList(object):

    def __init__(self):
        self._first = Node(None, None, None)
        self._length = 0
        self._last = Node(None, None, None)

    def __len__(self):
        return self._length

    def _insertItemAfterNode(self,item,aNode):
        newNode = Node(aNode._prev, item, aNode._next)
        aNode._next= newNode._prev
        aNode._prev=newNode._next
        self._length += 1

    def _nodeBeforeIndex(self, index):
        if 0 <= index <= self._length:
            aNode = self._first
            for i in range(index):
                aNode = aNode._next
            return aNode
        else:
            raise IndexError

    def _nodeAfterIndex(self, index):
        if 0<= index <= self.length:
            aNode = self._last
            for i in range(index):
                aNode = aNode._prev
            return aNode
        else:
            raise IndexError

    def __getitem__(self, index):
        return self._nodeBeforeIndex(index)._next._data

    def insertAtEnd(self, item):
        self._nodeAfterIndex(item)        

    def __iter__(self):
        return DoublyLinkedListIterator(self)

    def __setitem__(self, index, item):
        self._nodeBeforeIndex(index)._next._data = item

    def insertItemAtTheFront(self, item):
        self._insertItemAfterNode(item, self._nodeBeforeIndex(0))

    def insertItemAtTheEnd(self, item):
        self._insertItemAfterNode(item, self._nodeBeforeIndex(self._length))

    def insertItemAtIndex(self, index, item):
        '''Valid range 0 <= index <= length.'''
        self._insertItemAfterNode(item, self._nodeBeforeIndex(index))

    def __iter__(self):
        return DoublyLinkedListIterator(self)

    def __repr__(self):
        #used by print in abscence of __str__ .
        plist = []
        for item in self:
            plist.append(item)
        return "DoublyLinkedList(%s)" % str(plist)

class DoublyLinkedListIterator(object):

    def __init__(self, aList):
        self._list = aList
        self._currentIndex = -1
        self._currentNode = self._list._first

    def __iter__(self):
        return self

    def __next__(self):
        if self._currentIndex == self._list._length - 1:
            raise StopIteration
        else:
            self._currentIndex += 1
            self._currentNode = self._currentNode._next
            return self._currentNode._data
