class GraphModule:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, bidirectional=True):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if bidirectional and u not in self.adj[v]:
            self.adj[v].append(u)

    def bfs(self, start):
        if start not in self.adj:
            return []
        visited = set([start])
        queue = [start]
        order = []
        while queue:
            curr = queue.pop(0)
            order.append(curr)
            for neighbor in sorted(self.adj[curr]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        if start not in self.adj:
            return []
        visited = set()
        order = []

        def dfs_recursive(v):
            visited.add(v)
            order.append(v)
            for neighbor in sorted(self.adj[v]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return order

    def run(self):
        while True:
            print("\n--- [6] GRAPH OPERATIONS ---")
            print("Adjacency List:")
            if not self.adj:
                print("   (Graph has no vertices)")
            else:
                for k in sorted(self.adj.keys()):
                    print(f"   {k} -> {self.adj[k]}")

            print("\n1. Add Vertex")
            print("2. Add Edge (u - v)")
            print("3. BFS Traversal (Breadth-First Search)")
            print("4. DFS Traversal (Depth-First Search)")
            print("5. Reset Graph")
            print("0. Back to Main Menu")
            choice = input("Select an option: ").strip()

            if choice == '1':
                v = input("Enter vertex identifier: ").strip()
                if v and v not in self.adj:
                    self.adj[v] = []
                    print(f"-> Added vertex '{v}'.")
            elif choice == '2':
                u = input("Enter source vertex (u): ").strip()
                v = input("Enter destination vertex (v): ").strip()
                if u and v:
                    self.add_edge(u, v)
                    print(f"-> Added undirected edge between '{u}' and '{v}'.")
            elif choice == '3':
                start = input("Enter start vertex for BFS: ").strip()
                if start not in self.adj:
                    print("-> Error: Vertex does not exist.")
                else:
                    path = self.bfs(start)
                    print("-> BFS Order: " + " -> ".join(path))
            elif choice == '4':
                start = input("Enter start vertex for DFS: ").strip()
                if start not in self.adj:
                    print("-> Error: Vertex does not exist.")
                else:
                    path = self.dfs(start)
                    print("-> DFS Order: " + " -> ".join(path))
            elif choice == '5':
                self.adj.clear()
                print("-> Graph cleared.")
            elif choice == '0':
                break
            else:
                print("-> Invalid option.")