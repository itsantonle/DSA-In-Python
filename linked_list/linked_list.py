class Node: 
    data = None
    next_node = None
    
    def __repr__(self) -> str:
        return f" Node: {self.data}"
    
    def __init__(self, data) -> None:
        self.data = data 


n1 = Node("Data One")
n2 = Node("Data One")
n1.next_node = n2
print(n1)

class LinkedList: 

    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        listings = []
        current = self.head
        while(current != None):
            listings.append(current)
            current = current.next_node
        return f"Linked List({listings})"
    
    @property
    def isEmpty(self): 
        return self.head == None
    
    @property
    def size(self):
        count = 0
        current = self.head
        
        while( current != None):
            count += 1
            current = current.next_node
            
        return count 
    # i could write this recursively in FP
    
    def append(self,data):
        new_node = Node(data)
        current = self.head
        if (self.head == None): 
            self.head = new_node
        
        while(current.next_node != None):
            current = current.next_node
            
        current.next_node = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        if(self.head == None): 
            self.head = new_node
            
        new_node.next_node = self.head
        self.head = new_node
        
    def insert(self, data, target_index):
        new_node = Node(data)
        cur_index = 0
        current = self.head
        
        if(self.size < target_index or target_index < 0): 
            raise Exception("Target index out of bounds")
        
        if(target_index == 0):
            self.prepend(data)
        else: 
        
            while(cur_index != (target_index -1)): 
                cur_index += 1
                current = current.next_node
            
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def delete(self, target_index): 
        current = self.head
        previous = None
        cur_in = 0
        
        while(cur_in != target_index):
            previous = current
            current = current.next_node
            cur_in += 1
        
        previous.next_node = current.next_node
        
        
            
                
                
        
        
    

linked = LinkedList()
node_one = Node("1")
node_two = Node("2")
linked.head = node_one
node_one.next_node = node_two
linkedagain = LinkedList()


linked.append("3")
linked.prepend("0")
linked.insert("20", 1)
linked.insert("1", 0)
linked.insert("1", linked.size)
linked.delete(1)

print(linked.size)
print(linked)