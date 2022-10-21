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

    def addFirst(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            self.head = Node(data)
            self.head.next = current
    
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
    print("2. Add at the beginning")
    print("3. Remove")
    print("4. Print")
    print("5. Split")
    print("6. Exit")
    return int(input("Enter an option: "))

if __name__ == "__main__":
    ll = LinkedList()
    try:
        while True:
            option = menu()
            if option == 1:
                ll.add(input("Enter data: "))
            elif option == 2:
                ll.addFirst(input("Enter data: "))
            elif option == 3:
                ll.remove(input("Enter data: "))
            elif option == 4:
                print(ll)
            elif option == 5:
                even = LinkedList()
                odd = LinkedList()
                current = ll.head
                while current:
                    if int(current.data) % 2 == 0:
                        even.add(int(current.data))
                    else:
                        odd.add(int(current.data))
                    current = current.next
                print('Odes: ', odd)
                print('Even: ', even)
            elif option == 6:
                break
            else:
                print("Invalid option")    
    except KeyboardInterrupt:
        print('An error occurred')