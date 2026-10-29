class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListModule:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Linked List: [HEAD] -> None")
            return
        curr = self.head
        chain = []
        while curr:
            chain.append(str(curr.data))
            curr = curr.next
        print("Linked List: [HEAD] -> " + " -> ".join(chain) + " -> None")

    def run(self):
        while True:
            print("\n--- [2] LINKED LIST OPERATIONS ---")
            self.display()
            print("1. Insert at Beginning")
            print("2. Insert at End")
            print("3. Delete by Value")
            print("4. Search Value")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                val = input("Enter value: ").strip()
                new_node = Node(val)
                new_node.next = self.head
                self.head = new_node
                print(f"-> Inserted '{val}' at the beginning.")
            elif choice == '2':
                val = input("Enter value: ").strip()
                new_node = Node(val)
                if not self.head:
                    self.head = new_node
                else:
                    curr = self.head
                    while curr.next:
                        curr = curr.next
                    curr.next = new_node
                print(f"-> Inserted '{val}' at the end.")
            elif choice == '3':
                if not self.head:
                    print("-> Error: List is empty.")
                    continue
                val = input("Enter value to delete: ").strip()
                if self.head.data == val:
                    self.head = self.head.next
                    print(f"-> Deleted '{val}' from head.")
                    continue
                curr = self.head
                found = False
                while curr.next:
                    if curr.next.data == val:
                        curr.next = curr.next.next
                        found = True
                        print(f"-> Deleted '{val}'.")
                        break
                    curr = curr.next
                if not found:
                    print(f"-> Error: Value '{val}' not found.")
            elif choice == '4':
                if not self.head:
                    print("-> Error: List is empty.")
                    continue
                val = input("Enter value to search: ").strip()
                curr = self.head
                pos = 0
                found = False
                while curr:
                    if curr.data == val:
                        print(f"-> Found '{val}' at position {pos}.")
                        found = True
                        break
                    curr = curr.next
                    pos += 1
                if not found:
                    print(f"-> Value '{val}' not found.")
            elif choice == '0':
                break
            else:
                print("-> Invalid option.")