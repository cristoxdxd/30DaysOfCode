class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            out = ""
            while current:
                out += str(current) + " -> "
                current = current.next
            return out[:-4]
    
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def remove(self, data):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            if current.data == data:
                self.head = current.next
                return
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
            return "Not found"

def menu():
    print("\n1. Add")
    print("2. Remove")
    print("3. Print")
    print("4. Exit")
    return int(input("Enter an option: "))

if __name__ == "__main__":
    ll = LinkedList()
    try:
        while True:
            option = menu()
            if option == 1:
                ll.add(input("Enter data: "))
            elif option == 2:
                ll.remove(input("Enter data: "))
            elif option == 3:
                print(ll)
            elif option == 4:
                break
            else:
                print("Invalid option")    
    except KeyboardInterrupt:
        print('An error occurred')

'''
odes = LinkedList()
        evens = LinkedList()
        current = self.head
        while current:
            if current.data % 2 == 0:
                evens.add(current)
            else:
                odes.add(current)
            current = current.next
        return odes, evens
'''