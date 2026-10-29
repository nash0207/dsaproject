class StackModule:
    def __init__(self):
        self.stack = []

    def run(self):
        while True:
            print("\n--- [3] STACK (LIFO) OPERATIONS ---")
            print("Current Stack (Top -> Bottom):", list(reversed(self.stack)))
            print("1. Push")
            print("2. Pop")
            print("3. Peek / Top")
            print("4. Check Empty / Size")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                val = input("Enter element to push: ").strip()
                self.stack.append(val)
                print(f"-> Pushed '{val}' onto stack.")
            elif choice == '2':
                if not self.stack:
                    print("-> Underflow Error: Cannot pop from an empty stack.")
                else:
                    popped = self.stack.pop()
                    print(f"-> Popped '{popped}' from stack.")
            elif choice == '3':
                if not self.stack:
                    print("-> Stack is currently empty.")
                else:
                    print(f"-> Top Element: '{self.stack[-1]}'")
            elif choice == '4':
                print(f"-> Is Empty: {len(self.stack) == 0} | Total Elements: {len(self.stack)}")
            elif choice == '0':
                break
            else:
                print("-> Invalid option.")