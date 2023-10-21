class Node:
    def __init__(self, v, p, n):
        """
        constructor - declare variables
        :param v: value of Node
        :param p: link on previous Node
        :param n: link on next Node
        """
        self.value = v
        self.previous = p
        self.next = n

    def set_value(self, v):
        """
        Checking and setting param _value
        :param v: value of Node
        """
        if (not isinstance(v, int) and
                not isinstance(v, float) and
                not type(v) == bool and
                not type(v) == str and
                v is not None):
            raise Exception("Variable \"value\" can be only boolean, int, float, string or None!")
        else:
            self._value = v

    def get_value(self):
        """
        Returning value of param value
        :return: value of node
        """
        return self._value

    def set_previous(self, p):
        """
        Checking and setting _previous
        :param p: node
        """
        if p is not None and not isinstance(p, Node):
            raise Exception("Variable \"previous\" can be only None or Node!")
        else:
            self._previous = p

    def get_previous(self):
        """
        Returning previous node
        :return: previous node
        """
        return self._previous

    def set_next(self, n):
        """
        Checking and setting node _next
        :param n: node
        """
        if n is not None and not isinstance(n, Node):
            raise Exception("Variable \"next\" can be only None or Node!")
        else:
            self._next = n

    def get_next(self):
        """
        Returning next node
        :return: next node
        """
        return self._next

    value = property(get_value, set_value)
    previous = property(get_previous, set_previous)
    next = property(get_next, set_next)


class My_Queue:
    def __init__(self):
        """
        constructor - declare variables
        """
        self.head = None
        self.tail = None
        self.size = 0

    def set_head(self, h):
        """
        Checking and setting _head
        :param h: head node
        """
        if h is not None and not isinstance(h, Node):
            raise Exception("Variable \"head\" can be only None or Node!")
        else:
            self._head = h

    def get_head(self):
        """
        Returning head node
        :return: head
        """
        return self._head

    def set_tail(self, t):
        """
        Checking and setting _tail
        :param t: tail
        """
        if t is not None and not isinstance(t, Node):
            raise Exception("Variable \"tail\" can be only None or Node!")
        else:
            self._tail = t

    def get_tail(self):
        """
        Returning node tail
        :return: node tail
        """
        return self._tail

    head = property(get_head, set_head)
    tail = property(get_tail, set_tail)

    def count(self):
        """
        Counting number of nodes in queue (For this method it can only return variable "size")
        :return: number of nodes
        """
        num_of_nodes = 0
        tmp_node = self.head
        if tmp_node is not None:
            num_of_nodes += 1
            while tmp_node.next is not None:
                tmp_node = tmp_node.next
                num_of_nodes += 1
        return "In queue is " + str(num_of_nodes) + " elements (nodes)"

    def add(self, num):
        """
        Adds new node with value of num into queue
        :param num: value of new node
        """
        if self.size == 0:
            self.head = Node(num, None, None)
            self.tail = Node(num, None, None)
        elif self.size == 1:
            self.tail = Node(num, self.head, None)
            self.head.next = self.tail
        elif self.size >= 2:
            self.tail.next = Node(num, self.tail, None)
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        """
        Deletes node from head
        :return: deleted node
        """
        if self.size == 0:
            return "Queue is empty, nothing to delete"
        elif self.size == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return str(tmp.value) + " was deleted"
        elif self.size >= 2:
            tmp = self.head
            self.head = self.head.next
            self.size -= 1
            return str(tmp.value) + " was deleted"

    def clear(self):
        """
        Deletes all nodes from whole queue (clears it - is empty)
        """
        self.head = None
        self.tail = None
        self.size = 0

    def popAll(self):
        """
        Deletes all nodes from whole queue (clears it - is empty)
        :return: list of all deleted nodes
        """
        list_of_Nodes = []
        while True:
            text = self.pop()
            if text != "Queue is empty, nothing to delete":
                list_of_Nodes.append(text[0:len(text) - 12])
            else:
                break
        return str(list_of_Nodes) + " was deleted"

    def printf(self):
        """
        Returns string of values of nodes
        :return: all values of all nodes in queue (current state of queue)
        """
        text = ""
        if self.size != 0:
            element = self.head
            while element.next is not None:
                text += str(element.value) + ", "
                element = element.next
            text += str(element.value)
        else:
            text += "Linked List is empty."
        return text


try:
    q = My_Queue()
    print(q.printf())
    q.add(4)
    q.add(8)
    q.add(6)
    q.add(38)
    q.add(39)
    q.add(95)
    print(q.count())
    print(q.printf())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    q.add(1)
    q.add(93)
    q.add(47)
    print(q.printf())
    q.clear()
    q.add(13)
    q.add(85)
    q.add(63)
    q.add(44)
    q.add(671)
    print(q.printf())
    print(q.count())
    print(q.popAll())
    print(q.count())
    print(q.printf())
except Exception as e:
    print(e)
