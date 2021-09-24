class node: 
    def __init__(self, data= None): 
        self.data = data
        self.next= None

class linked_list: 
    def __init__(self):
        self.head = node()
    def append(self, data) :  
        new_node= node(data)
        cur= self.head
        while cur.next != None: 
            cur= cur.next
        cur.next = new_node    
    def length(self ): 
        cur= self.head
        total= 0 
        while cur.next != None: 
            total +=1
        cur= cur.next

    def display(self): 
        elems= []
        cur_node= self.head  
        while cur_node.next != None: 
            cur_node= cur_node.next
            elems.append(cur_node.data)
        print(elems) 
    def get(self , index): 
        if index  >= self.length():   
            print("Error, get an index out of range ")
            return None
        current_index=0 
        current_node = self.head
        while True: 
            current_node= current_node.next
            if current_index==index: return current_node.data
            current_index+=1
 
my_list= linked_list()     
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display() 

print("element at 2nd index : %d " % my_list.get(1))