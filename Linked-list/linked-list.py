class linkedList:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def insert_value_from_start(self, data: int):
        new_node = linkedList(data)
        if self.next == None:
            self.next = new_node
        
    def insert_value(self, data: int):
        new_node = linkedList(data)
        if self.next == None:
            self.insert_value_from_start(data)
        else:
            current_node = self
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def count_length(self):
        total = 1
        current_node = self
        while current_node.next != None:
            current_node = current_node.next
            total += 1
        return total
    
    def insert_at_idx(self, data, idx):
        if idx < 1:
            raise Exception("below zero is not allowed")
        new_node = linkedList(data)
        total_node = self.count_length()
        if idx > total_node:
            self.insert_value(data)
        else:
            pos = 1
            current_node = self
            while pos < idx:
                current_node = current_node.next
                pos += 1
            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
    
    def print_itterate(self):
        current_node = self
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def get_val_index(self, idx):
        if idx > self.count_length() - 1 or idx < 0:
            raise Exception("index out of range")
        pos = 0
        current_node = self
        while pos != idx:
            current_node = current_node.next
            pos += 1
        return current_node.data





head = linkedList(0)

head.insert_value(2)

head.insert_value(3)

head.insert_value(4)

head.insert_at_idx(5, 2)

head.insert_at_idx(6,4)

head.insert_at_idx(7,2)

# print(head.count_length())

print(head.get_val_index(3))

