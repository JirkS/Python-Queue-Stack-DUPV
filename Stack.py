class Node:
    def __init__(self, v, n):
        """
        constructor - declare variables
        :param v: value of Node
        :param n: link to next Node
        """
        self.value = v
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
    next = property(get_next, set_next)


class Stack:
    def __init__(self):
        """
        constructor - declare variables
        """
        self.top = None
        self.size = 0

    def set_top(self, t):
        """
        Checking and setting node _top
        :param t: top node
        """
        if t is not None and not isinstance(t, Node):
            raise Exception("Variable \"top\" can be only None or Node!")
        else:
            self._top = t

    def get_top(self):
        """
        Returning top node
        :return: top node
        """
        return self._top

    top = property(get_top, set_top)

    def count(self):
        """
        Counting number of nodes in stack (For this method it can only return variable "size")
        :return: number of nodes
        """
        num_of_nodes = 0
        tmp_node = self.top
        if tmp_node is not None:
            num_of_nodes += 1
            while tmp_node.next is not None:
                tmp_node = tmp_node.next
                num_of_nodes += 1
        return "In stack is " + str(num_of_nodes) + " elements (nodes)"

    def add(self, num):
        """
        Adds new node with value of num into stack (on top)
        :param num: value of new node
        """
        if self.size == 0:
            self.top = Node(num, None)
        else:
            n = Node(num, self.top)
            self.top = n
        self.size += 1

    def pop(self):
        """
        Deletes node from top
        :return: deleted node
        """
        if self.size == 0:
            return "Stack is empty, nothing to delete"
        else:
            n = self.top
            self.top = self.top.next
            self.size -= 1
            return str(n.value) + " was deleted"

    def clear(self):
        """
        Deletes all nodes from whole stack (clears it - is empty)
        """
        self.top = None
        self.size = 0

    def popAll(self):
        """
        Deletes all nodes from whole stack (clears it - is empty)
        :return: list of all deleted nodes
        """
        list_of_Nodes = []
        while True:
            text = self.pop()
            if text != "Stack is empty, nothing to delete":
                list_of_Nodes.append(text[0:len(text) - 12])
            else:
                break
        return str(list_of_Nodes) + " was deleted"

    def printf(self):
        """
        Returns string of values of nodes
        :return: all values of all nodes in stack (current state of stack)
        """
        text = ""
        if self.size != 0:
            element = self.top
            while element.next is not None:
                text += str(element.value) + ", "
                element = element.next
            text += str(element.value)
        else:
            text += "Stack is empty."
        return text

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        if self.size != 0 and key < self.size:
            element = self.top
            for i in range(key+1):
                if i == key:
                    return element.value
                else:
                    element = element.next
        else:
            return "Stack is empty or key is too big!"
        return "error"

    def __setitem__(self, key, value):
        if self.size != 0 and key < self.size:
            element = self.top
            for i in range(key+1):
                if i == key:
                    element.value = value
                else:
                    element = element.next
        else:
            return "Stack is empty or key is too big!"
        return "error"


try:
    s = Stack()
    s.add(8)
    s.add(1)
    s.add(5)
    s.add(7)
    s.add(-6)
    print(s.count())
    print(s.printf())
    print(s.pop())
    print(s.printf())
    print(s.pop())
    print(s.printf())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.printf())
    s.add(1)
    s.add(-36)
    s.add(62)
    s.add(93)
    print(s.printf())
    print(s.count())
    s.clear()
    print(s.printf())
    print(s.pop())
    s.add(13)
    s.add(85)
    s.add(63)
    s.add(44)
    s.add(671)
    print(len(s))
    print(s.printf())
    print(s[4])
    s[10] = "Pepa"
    print(s[4])
    print(s.popAll())
    print(s.count())
    print(s.printf())
except Exception as e:
    print(e)
