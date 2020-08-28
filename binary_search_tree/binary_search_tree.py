"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left:  BSTNode = None    #bst either a BSTNnde or None
        self.right:  BSTNode  =None

    # Insert the given value into the tree
    def insert(self, value):
        #if single element
        # compare target value to node.value
        if value >= self.value:
            #go right for greater than

        #first node is root
        #if value > node.value

            if self.right is None:
            # if node.right is None:
            #create the new node there
                new_node = BSTNode(value)
                self.right = new_node
        #else
        #do the same thing
        #insert value into node right
            else: #self.right is bstNode\
                right_child = self.right
                right_child.insert(value)
        #else if target < node.value
        if value < self.value:

        #go left
            if self.left is None:
        #if left is None
        #create node
                self.left = BSTNode(value)
                #else:
            #       insert target in node.left
            else:
                left_child = self.left
                left_child.insert(value)





    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is None:
            return None
        #if target == node.value
            #return True
        if target == self.value:
            return True
        #if target > node.value
        #go right
        if target > self.value:
            #return self.contains(target.self.right)
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            #return self.contains(target.self.left)
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        #go right

       #contains = searching

    # Return the maximum value found in the tree
    def get_max(self):
        #will be right most node
        if self.right is None: #if no right side
            return self.value

        elif self.value == self.right:#if the right side is the same as the value
            return self.value
        else:
            max_value = self.right.get_max()
            return max_value #for the max value




    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is None and self.left is None:
            return None #if empty
        if self.right is not None:#for right side
            self.right.for_each(fn)
        if self.left is not None:#for left side
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    #queue first in last out
    def bft_print(self):
        node = self

        queue = Queue()
        queue.enqueue(node)#enqueue adds
        while queue.storage.length > 0:

            current = queue.dequeue() #takes off
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal


    def dft_print(self):
        node = self
        stack = Stack()
        stack.push(node)#pushs the node in
        while stack.storage.length > 0:
            current = stack.storage.head.value#stay aware of spacing
            stack.pop()#takes off
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            print(current.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)  # This is our de facto "root"

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# # print("pre order")
# # bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# # print("post order")
# # bst.post_order_dft()