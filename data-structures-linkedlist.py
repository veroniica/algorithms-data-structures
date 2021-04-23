
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self,data):
        new_node = Node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def prepend(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def insert(self,index,data):

        if index == 0:
            self.prepend(data)
            return
        
        if index > self.length:
            index = self.length
            self.append(data)
            return
        
        newNode = Node(data)
        current = self.head

        i = 0
        while i < index-1:
            current = current.next
            i += 1

        leader = current
        follower = current.next

        leader.next = newNode
        newNode.next = follower

        self.length += 1
    
    def remove(self,index):
        
        i = 0
        if index == 0 and self.length > 1:  
           self.head = self.head.next

        elif index >= self.length-1:
            current = self.head
            while i < self.length-2:
                current = current.next
                i += 1
            current.next = None
            self.tail = current

        else:
            current = self.head
            while i < index-1:
                current = current.next
                i += 1
            
            leader = current
            target = leader.next
            follower = target.next

            leader.next = follower
        self.length -= 1

    
    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data , end = ' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))


if __name__ == '__main__':

    my_linked_list = LinkedList()
    my_linked_list.append(0)
    my_linked_list.append(10)
    my_linked_list.append(20)
    my_linked_list.append(30)
    my_linked_list.append(40)
    my_linked_list.append(50)
    my_linked_list.append(60)
    my_linked_list.printl()
    my_linked_list.remove(73)
    my_linked_list.printl()
