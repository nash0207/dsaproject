class ArrayModule:
    def __init__(self):
        self.data = []

    def run(self):
        while True:
            print("\n--- [1] ARRAY OPERATIONS ---")
            print("Current Array:", self.data)
            print("1. Insert Element")
            print("2. Delete Element by Value")
            print("3. Search Element")
            print("4. Clear Array")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                val = input("Enter value to insert: ").strip()
                if val:
                    self.data.append(val)
                    print(f"-> Inserted '{val}' successfully.")
            elif choice == '2':
                if not self.data:
                    print("-> Error: Array is empty.")
                    continue
                val = input("Enter value to delete: ").strip()
                if val in self.data:
                    self.data.remove(val)
                    print(f"-> Deleted '{val}' from array.")
                else:
                    print(f"-> Error: Value '{val}' not found.")
            elif choice == '3':
                if not self.data:
                    print("-> Error: Array is empty.")
                    continue
                val = input("Enter value to search: ").strip()
                indices = [i for i, x in enumerate(self.data) if x == val]
                if indices:
                    print(f"-> Value '{val}' found at index/indices: {indices}")
                else:
                    print(f"-> Value '{val}' not found.")
            elif choice == '4':
                self.data.clear()
                print("-> Array cleared.")
            elif choice == '0':
                break
            else:
                print("-> Invalid option. Please try again.")