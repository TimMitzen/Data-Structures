

#run time complexity constant time operation: doesnt depend on the size of the list always takes the same time



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list
    def __str__(self):
      pass

class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
        self.length = 0
    def __str__(self):
        pass
    def __len__(self):
        pass
    def add_to_tail(self, value):
        # Check if there's a tail
        # If there is no tail (empty list)
        if self.tail is None:
            # Create a new node
            new_tail = Node(value, None)
        #    Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1
    def remove_head(self):
        # If not head (empty list)
        if self.head is None:  # if self.head is None
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length = self.length - 1
            return current_head.value

    def add_to_head(self, value):
            new_node = Node(value)

            if self.head is None and self.tail is None:
                self.head = new_node
                self.tail = new_node
            else:

                new_node.next - self.head

                self.head = new_node
        # General case:
        # Start at head and iterate to the next-to-last node


        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        # Set current_node.next to None
        #
        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
    def remove_tail(self):

        # Remove Tail:
        # Check if it's there

        if self.tail is None:
            return None
        elif self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_tail = self.tail
            self.tail = current_node

            current_node.next = None
            self.length -= 1
            return current_tail.value

    def add_to_head(self,value):
        if self.head is None:
            new_node = None(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, self.head)
            self.head - new_node
            self.length += 1


    def remove_at_index(self, index):
        if index >= self.length:
            return None
        if self.length == 1 and index ==0:
            target = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return target.value
        prev_node = self.head
        for i in range(index -1):
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length -= 1

        return target.value