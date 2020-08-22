"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, data, prev_node=None, next_node=None):
        self.prev_node = prev_node
        self.data = data
        self.next_node = next_node

    def delete(self):
        if self.prev_node:
            self.prev_node.next_node = self.next_node
        if self.next_node:
            self.next_node.prev_node = self.prev_node

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length +=1  # adding to head
        if self.head is None:#if empty list

            self.head = new_node
            self.tail = new_node

        else:
            new_node.next_node = self.head #setting head to next node
            self.head.prev_node = new_node
            self.head = new_node




        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.data
        self.delete(self.head)
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value,None,None)
        self.length += 1
    #check to see if tail
        if self.tail is None:
            #set tail and head to new tail
            self.head = new_node
            self.tail = new_node
        else:
            #create a new tail
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node




            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.data#useing delete function
        self.delete(self.tail)
        return value


            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if node is head
        if node is self.head:
            return
        if self.head.next is None: #if its tail
            return None
        value = node.value
        self.delete(node)
        self.add_to_head(value)



"""
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.data
        self.delete(node)
        self.add_to_tail(value)




"""
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return  self.head.data
        current_max = self.head.data
        current_node= self.head
        while current_node is not None:
            if current_max < current_node.data:
                current_max = current_node.data

        current_max = current_node.next_value
        return current_max