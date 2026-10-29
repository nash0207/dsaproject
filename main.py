from modules.array_ops import ArrayModule
from modules.linked_list import LinkedListModule
from modules.stack import StackModule
from modules.queue import QueueModule
from modules.tree import BSTModule
from modules.graph import GraphModule
from modules.sorting import SortingModule
import sys

def main():
    array_mod = ArrayModule()
    ll_mod = LinkedListModule()
    stack_mod = StackModule()
    queue_mod = QueueModule()
    bst_mod = BSTModule()
    graph_mod = GraphModule()
    sort_mod = SortingModule()

    while True:
        print("\n=======================================================")
        print("  PADRE GARCIA POLYTECHNIC COLLEGE - CC 104 TOOLKIT    ")
        print("     DATA STRUCTURES AND ALGORITHMS FINAL PROJECT      ")
        print("=======================================================")
        print("  1. Array Operations")
        print("  2. Singly Linked List Operations")
        print("  3. Stack (LIFO) Operations")
        print("  4. Queue (FIFO) Operations")
        print("  5. Binary Search Tree & Traversals (In/Pre/Post)")
        print("  6. Graph Operations (Adjacency List, BFS, DFS)")
        print("  7. Sorting Demonstrations (Bubble Sort vs Quicksort)")
        print("  0. Exit")
        print("=======================================================")
        ch = input("Enter choice [0-7]: ").strip()

        if ch == '1':
            array_mod.run()
        elif ch == '2':
            ll_mod.run()
        elif ch == '3':
            stack_mod.run()
        elif ch == '4':
            queue_mod.run()
        elif ch == '5':
            bst_mod.run()
        elif ch == '6':
            graph_mod.run()
        elif ch == '7':
            sort_mod.run()
        elif ch == '0':
            print("\nExiting DSA Toolkit. Good luck on your defense!")
            sys.exit(0)
        else:
            print("-> Invalid input! Please enter a number between 0 and 7.")

if __name__ == "__main__":
    main()