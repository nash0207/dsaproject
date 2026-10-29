class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BSTModule:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(str(root.val))
            self.inorder(root.right, res)

    def preorder(self, root, res):
        if root:
            res.append(str(root.val))
            self.preorder(root.left, res)
            self.preorder(root.right, res)

    def postorder(self, root, res):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(str(root.val))

    def print_tree(self, node, prefix="", is_left=True):
        if node is not None:
            print(prefix + ("|-- " if is_left else "\\-- ") + str(node.val))
            self.print_tree(node.left, prefix + ("|   " if is_left else "    "), True)
            self.print_tree(node.right, prefix + ("|   " if is_left else "    "), False)

    def run(self):
        while True:
            print("\n--- [5] BINARY SEARCH TREE & TRAVERSALS ---")
            print("Current Tree Structure:")
            if not self.root:
                print("   (Tree is empty)")
            else:
                self.print_tree(self.root)

            print("\n1. Insert Value (Integers)")
            print("2. Display All Traversals (Inorder, Preorder, Postorder)")
            print("3. Reset Tree")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                raw = input("Enter an integer key (or multiple space-separated integers): ").strip()
                tokens = raw.split()
                for t in tokens:
                    try:
                        val = int(t)
                        self.root = self.insert(self.root, val)
                        print(f"-> Inserted {val}")
                    except ValueError:
                        print(f"-> Error: '{t}' is not a valid integer. Skipped.")
            elif choice == '2':
                if not self.root:
                    print("-> Tree is empty.")
                    continue
                ino, pre, post = [], [], []
                self.inorder(self.root, ino)
                self.preorder(self.root, pre)
                self.postorder(self.root, post)
                print("\nTraversals Output:")
                print("  Preorder  (Root, L, R) : " + " -> ".join(pre))
                print("  Inorder   (L, Root, R) : " + " -> ".join(ino) + "  (Sorted order for BST)")
                print("  Postorder (L, R, Root) : " + " -> ".join(post))
            elif choice == '3':
                self.root = None
                print("-> Tree reset to empty.")
            elif choice == '0':
                break
            else:
                print("-> Invalid option.")