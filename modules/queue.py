class QueueModule:
    def __init__(self):
        self.queue = []

    def run(self):
        while True:
            print("\n--- [4] QUEUE (FIFO) OPERATIONS ---")
            print("Current Queue (Front -> Rear):", self.queue)
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek / Front")
            print("4. Check Empty / Size")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                val = input("Enter element to enqueue: ").strip()
                self.queue.append(val)
                print(f"-> Enqueued '{val}'.")
            elif choice == '2':
                if not self.queue:
                    print("-> Underflow Error: Cannot dequeue from an empty queue.")
                else:
                    removed = self.queue.pop(0)
                    print(f"-> Dequeued '{removed}'.")
            elif choice == '3':
                if not self.queue:
                    print("-> Queue is currently empty.")
                else:
                    print(f"-> Front Element: '{self.queue[0]}'")
            elif choice == '4':
                print(f"-> Is Empty: {len(self.queue) == 0} | Total Elements: {len(self.queue)}")
            elif choice == '0':
                break
            else:
                print("-> Invalid option.")