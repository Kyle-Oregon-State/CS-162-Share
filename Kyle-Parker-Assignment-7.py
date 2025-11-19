# Author: Kyle Parker
# GitHub username: Kyle-Oregon-State
# Date: 11/12/2025
# Description: Defines a LinkedList class with recursive add and remove methods. Also has recursive contains, insert, and reverse methods.
# Also a recursive method "to_plain_list" that returns a regular python list with the same value as the LinkedList.

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Represents a linked list, a discontiguous implementation of the list ADT.
    """
    def __init__(self):
        """
        creates a new linked list
        """
        self._head = None

    def get_head(self):
        """
        returns the head of the linked list
        """
        return self._head

    def add(self, data, current=None):
        """
        Creates a new node with the given data value and adds it to the end of the linked list
        current must = None
        """
        if self._head is None:
            self._head = Node(data)
            return None

        if current is None: # Sets current = head but only if current is empty, to prevent it from rewriting every recursion and looping until we run out of memory.
            current = self._head

        if current.next is not None:
            return self.add(data,current.next)
        else:
            current.next = Node(data)
            return None

    def remove(self, val, current=None, previous=None):
        """
        Removes the first node containing val from the linked list
        current must = None
        """
        if self._head is None:  # If the list is empty
            return None

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
            return None

        if current is None: # Sets current = head but only if current is empty, to prevent it from rewriting every recursion and looping until we run out of memory.
            current = self._head

        if current.data != val and current.next is not None:
            return self.remove(val,current.next,current)
        elif current.data != val:
            return None
        else:
            previous.next = current.next
            return None

    def contains(self, key, current=None):
        """
        Returns true if the given key exists in the linked list
        Otherwise returns false
        current must = None
        """
        if self._head is None:
            return False

        if self._head == key:
            return True

        if current is None: # Sets current = head but only if current is empty, to prevent it from rewriting every recursion and looping until we run out of memory.
            current = self._head

        if current.data == key:
            return True

        if current.next is not None:
            return self.contains(key,current.next)
        else:
            return False

    def insert(self, data, pos, current=None, current_pos=0):
        """
        Inserts the given data value into the linked list at index pos
        current must = None and current_pos must = 0
        """
        if self._head is None:
            self.add(data)
            return None

        if pos == 0:
            temp = self._head
            self._head = Node(data)
            self._head.next = temp
            return None

        if current_pos == pos -1:
            temp = current.next
            current.next = Node(data)
            current.next.next = temp
            return None

        if current is None:
            current = self._head

        if current.next is not None:
            return self.insert(data,pos, current.next, current_pos + 1)
        else:
            current.next = Node(data)
            return None

    def reverse(self, current=None, previous=None):
        """
        Reverses the linked list
        current must = None and previous must = None
        """

        if current is None and previous is None:
            current = self._head

        if current is not None:
            following = current.next
            current.next = previous
            return self.reverse(following, current)
        else:
            self._head = previous
            return None

    def to_plain_list(self, resulting_list=None,current=None):
        """
        Returns a regular Python list containing the same values, in the same order, as the linked list
        resulting_list must = None and current must = None
        """
        if self._head is None:
            return None

        if current is None:
            current = self._head

        if resulting_list is None:
            resulting_list = []

        resulting_list.append(current.data)

        if current.next is None:
            return resulting_list
        else:
            return self.to_plain_list(resulting_list, current.next)


