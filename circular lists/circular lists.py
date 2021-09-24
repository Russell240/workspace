
class Node(object):
    def __init__(self, data = None, next_node= None ):
        self.data= data 
        self.next_node= next_node
       

class CircularLinkedList(object): 
    def __init__(self, head= None, end=None) :
        self.head= head 
        self.end = end

    def traverse(self): 
        curr_node= self.head 
        while curr_node.next_node:
            print(curr_node.data)
            curr_node=curr_node.next_node
            if curr_node== self.head:
                break
    def insert_end(self, data): 
        new_node= Node(data)
        # if list is empty 
        if self.head == None :
            self.head= new_node
            self.head.next_node= new_node
            self.end= new_node
            return
        # if the list if not empty 
        if self.end!= None:
             self.end.next_node = new_node
             new_node.next_node= self.head
             self.end = new_node
             return   
    def insert_beg (self, data): 
            new_node= Node(data)
            new_node.next_node= self.head
            curr_node = self.head
            # handle the empty list case 
            if curr_node == None:
                self.head = new_node
                self.end = new_node
                self.head.next_node = new_node
                return
            # handle the none empty list case   
            if self.end!=  None:
                self.end.next_node = new_node
                new_node.next_node = self.head
                self.head = new_node
                return
    def insert_mid(self, ref_node, data):   
        # handle empty node 
        if ref_node == None: 
            raise ValueError("The reference node can't be none ")
    
        # otherwise its a true mid 
        new_node = Node(data) 
        ref_next = ref_node.next_node
        ref_node.next_node = new_node
        new_node.next_node = ref_next    
        # grad the node after the head 
    def delete_beg(self): 
        if self.head!= None: 
            after_head= self.head.next_node    
            # have the last node point to the last node after head 
            self.end.next = after_head      
            # set the head property 
            self.head = after_head
        else : 
            raise ValueError("The list is empty ")  
    def delete_end(self):
        if self.end!= None: 
           # grad the head 
           curr_node= self.head 
           # transverse until the end 
           while curr_node.next_node.next_node != self.head: 
                curr_node = curr_node.next_node
            # reassign the tail 
                self.end = curr_node
                curr_node.next_node = self.head   
        else : 
            raise ValueError("The list is empty ")  
    def delete_mid(self, position): 
        # if position if zero 
        if position ==0:
            self.delete_beg()
            return
        if position == self.list_size(): 
            self.delete_end
            return
        # if the position of the size of the  list minus one the delete 
        if position == self.list_size():
            self.delete_end()
            return
        curr_node = self.head.next_node    
        # initalise the count 
        count = 0 
        while count <= position : 
            count = count +1 
            curr_node= curr_node.next_node
        curr_node.next_node= curr_node.next_node.next_node    
    def list_size(self) : 
        curr_node = self.head
        count = 0 
        print(curr_node.data)
        while curr_node.next_node:
            count = count +1
            curr_node=curr_node.next_node
            if curr_node== self.head:
                break
            return count    

    def get_prev_node(self, ref_node):
        '''
            Return the node before a given reference node.
            Time Complexity: O(n)
        ''' 
        
        # handle empty list case
        if self.head is None:
            raise ValueError("The list is empty")
        
        # define the first node
        current = self.head
        
        # keep going until you reach the desired node.
        while current.next_node != ref_node:
            current = current.next_node
                   
        return current

            
    def reverse(self):
        '''
            Reverse the circular list, so that the tail is now the head.
            Time Complexity: O(n)
        ''' 
        
        # if the head is empty return
        if self.head is None:
            raise ValueError("The list is empty")
        
        # initalize a few of our variables
        last = self.head
        curr = self.head
        prev = self.end        
        next = curr.next_node
        
        # reassign the last node to the head's next node
        curr.next_node = prev 
        
        # the old previous now becomes the old current
        prev = curr
        
        # the old current now becomes the old next, the one after the head
        curr = next
        
        # keep going until you reach the last node
        while curr != last:
            
            # reassign next
            next=curr.next_node
            
            # do the same reassignment steps as upabove
            curr.next_node = prev
            prev = curr
            curr = next
        
        # one final reassignment, make sure the last node points to the head
        curr.next_node = prev
        
        # then redefine your head and tail.
        self.head = prev
        self.end = curr 
    def split_list(self, head1, head2):
        '''            
            Split the list into two separate circular linked list.
            Time Complexity: O(n)
            
            PARA: head1
            TYPE: CircularLinkedList
            
            PARA: head2
            TYPE: CircularLinkedList
        ''' 
        
        slow_ptr = self.head
        fast_ptr = self.head
        
        # handle empty list case
        if self.head is None:
            raise ValueError("The list is empty")
        
        # For ODD NODES: fast_ptr.next_node will become the head.
        # For EVEN NODES: fast_ptr.next_node.next_node will become the head.
        while (fast_ptr.next_node != self.head and fast_ptr.next_node.next_node != self.head):
            fast_ptr = fast_ptr.next_node.next_node
            slow_ptr = slow_ptr.next_node
        
        # if the fast pointer next next is the head, just stop one node before to get the last element of our list.
        if fast_ptr.next_node.next_node == self.head:
            fast_ptr = fast_ptr.next_node
        
        # Set the head pointer of first half 
        head1.head = self.head
        
        # Set the head pointer of second half 
        if self.head.next_node != self.head:
            head2.head = slow_ptr.next_node
        
        # Make second half circular 
        fast_ptr.next_node = slow_ptr.next_node
        
        # Make first half circular
        slow_ptr.next_node = self.head
        
    def split_list_2(self, head1, head2):
        '''            
            Split the list into two separate circular linked list.
            Time Complexity: O(n)
            
            PARA: head1
            TYPE: CircularLinkedList
            
            PARA: head2
            TYPE: CircularLinkedList
        ''' 
        # grab the list size
        list_size =self.list_size()

        if list_size==None: 
            raise ValueError("The list is empty")
      # grab the midpoint
        mid = list_size // 2
        # get the first node
        curr = self.head
        
        # go while the count is less than the list size
        count = 0        
        while count <= list_size - 1:
            
            # grab the data
            data = curr.data
            
            # if it's less than the mid, put in list one
            if count < mid:
                head1.insert_beg(data)
            
            # if it's greater than the mid, put it in list two
            if count >= mid:
                head2.insert_beg(data)
                
            # grab the next node.
            curr = curr.next_node
            
            # increment the counter
            count = count + 1    

circularList = CircularLinkedList()
circularList.insert_end(50)
circularList.insert_end(60)
circularList.insert_end(70)

circularList.insert_beg(90)
circularList.insert_beg(100)
print('After Insertion ')
print('-'*20)
first_node = circularList.end

circularList.insert_mid(first_node,20)

print('After Mid Insertion')
print('-'*20)

circularList.traverse()
circularList.delete_beg()
circularList.delete_end()

circularList.reverse
print('Before reversal ')
print('-'*20)
circularList.traverse()
print(circularList.list_size())
circularList.delete_mid(3)

print('After Mid Deletion ')
print('-'*20)
circularList.traverse()

second_node= circularList.head.next_node
circularList.get_prev_node(second_node)

head1= CircularLinkedList()
head2 = CircularLinkedList()

circularList.split_list_2(head1, head2)

print('List one ') 
print('-'*20)
head1.traverse()

print('List two ') 
print('-'*20)
head2.traverse()
