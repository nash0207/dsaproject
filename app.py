import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="CC 104 - Data Structures and Algorithms System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Academic Stylesheet (No emojis, clean corporate/academic UI)
st.markdown("""
<style>
    /* Main Layout & Typography */
    .reportview-container, .main {
        background-color: #f8fafc;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    }
    
    /* Institutional Header Banner */
    .inst-header {
        background-color: #0f2a4a;
        color: #ffffff;
        padding: 20px 24px;
        border-radius: 4px;
        margin-bottom: 24px;
        border-left: 6px solid #2563eb;
    }
    .inst-header h1 {
        margin: 0;
        font-size: 20px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-weight: 700;
        color: #ffffff;
    }
    .inst-header p {
        margin: 4px 0 0 0;
        font-size: 13px;
        color: #94a3b8;
    }

    /* Section Cards */
    .module-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .module-title {
        font-size: 16px;
        font-weight: 700;
        color: #0f2a4a;
        margin-bottom: 12px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Visual Memory Cell Containers */
    .mem-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 15px 0;
    }
    .mem-cell {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .mem-index {
        font-size: 11px;
        color: #64748b;
        font-family: monospace;
        margin-bottom: 4px;
    }
    .mem-val {
        background-color: #ffffff;
        border: 2px solid #0f2a4a;
        color: #0f2a4a;
        padding: 10px 18px;
        font-size: 14px;
        font-weight: 600;
        border-radius: 4px;
        min-width: 60px;
        text-align: center;
    }

    /* Pointer Node for Linked Lists */
    .node-wrapper {
        display: inline-flex;
        align-items: center;
        margin: 6px 0;
    }
    .ll-node {
        display: inline-flex;
        border: 1px solid #1e293b;
        border-radius: 4px;
        overflow: hidden;
        background-color: #ffffff;
    }
    .ll-data {
        padding: 8px 14px;
        font-weight: 600;
        font-size: 13px;
        color: #0f172a;
        border-right: 1px solid #cbd5e1;
    }
    .ll-ptr {
        padding: 8px 10px;
        background-color: #f1f5f9;
        font-size: 11px;
        color: #64748b;
        font-family: monospace;
    }
    .ptr-arrow {
        margin: 0 8px;
        font-weight: bold;
        color: #64748b;
    }

    /* Stack Visualization Box */
    .stack-tube {
        border-left: 3px solid #0f2a4a;
        border-right: 3px solid #0f2a4a;
        border-bottom: 3px solid #0f2a4a;
        padding: 8px;
        background-color: #f8fafc;
        max-width: 260px;
        display: flex;
        flex-direction: column;
        gap: 6px;
    }
    .stack-cell {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 8px 12px;
        text-align: center;
        font-weight: 600;
        font-size: 13px;
        color: #0f2a4a;
    }
    .stack-top-cell {
        background-color: #eff6ff;
        border: 1px solid #2563eb;
        color: #1e40af;
    }

    /* Console Logs */
    .log-box {
        background-color: #0f172a;
        color: #38bdf8;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 12px;
        padding: 12px;
        border-radius: 4px;
        margin-top: 10px;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("""
<div class="inst-header">
    <h1>Padre Garcia Polytechnic College</h1>
    <p>Department of Computer Studies | CC 104 - Data Structures and Algorithms Laboratory Interface</p>
</div>
""", unsafe_allow_html=True)

# Navigation Menu
st.sidebar.markdown("### System Navigation")
module = st.sidebar.selectbox(
    "Select Target Module:",
    [
        "Module 1: Array Operations",
        "Module 2: Singly Linked List",
        "Module 3: Stack (LIFO)",
        "Module 4: Queue (FIFO)",
        "Module 5: Binary Search Tree",
        "Module 6: Graph Traversals",
        "Module 7: Sorting Analysis"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Course Code:** CC 104")
st.sidebar.markdown("**Academic Year:** 2026-2027")

# ==============================================================================
# MODULE 1: ARRAY OPERATIONS
# ==============================================================================
if module == "Module 1: Array Operations":
    st.markdown('<div class="module-title">Linear Data Structure: One-Dimensional Array</div>', unsafe_allow_html=True)

    if "array_state" not in st.session_state:
        st.session_state.array_state = ["45", "12", "89", "33"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Array Controls**")
        input_val = st.text_input("Enter Element Value", key="arr_in")
        c1, c2 = st.columns(2)
        if c1.button("Insert Element", use_container_width=True):
            if input_val.strip():
                st.session_state.array_state.append(input_val.strip())
                st.rerun()

        if c2.button("Delete by Value", use_container_width=True):
            if input_val.strip() in st.session_state.array_state:
                st.session_state.array_state.remove(input_val.strip())
                st.rerun()
            else:
                st.error("Error: Element not found.")

        if st.button("Clear Entire Array", use_container_width=True):
            st.session_state.array_state = []
            st.rerun()

    with col2:
        st.markdown("**Contiguous Memory View**")
        if st.session_state.array_state:
            # Fixed: Combined into single-line strings so Markdown won't mistake indentation for code
            html_cells = '<div class="mem-grid">'
            for idx, val in enumerate(st.session_state.array_state):
                html_cells += f'<div class="mem-cell"><div class="mem-index">INDEX [{idx}]</div><div class="mem-val">{val}</div></div>'
            html_cells += '</div>'
            st.markdown(html_cells, unsafe_allow_html=True)
        else:
            st.info("Status: Array is empty (Length: 0)")

        st.markdown(f"""
        <div class="log-box">Total Elements (Length): {len(st.session_state.array_state)}
Status: Memory allocated contiguously
Operations supported: O(1) Append, O(n) Search/Delete</div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MODULE 2: SINGLY LINKED LIST
# ==============================================================================
elif module == "Module 2: Singly Linked List":
    st.markdown('<div class="module-title">Linear Data Structure: Singly Linked List</div>', unsafe_allow_html=True)

    if "ll_state" not in st.session_state:
        st.session_state.ll_state = ["100", "250", "400"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Node Controls**")
        node_val = st.text_input("Enter Node Data", key="ll_in")
        b1, b2 = st.columns(2)
        if b1.button("Insert Head", use_container_width=True):
            if node_val.strip():
                st.session_state.ll_state.insert(0, node_val.strip())
                st.rerun()
        if b2.button("Insert Tail", use_container_width=True):
            if node_val.strip():
                st.session_state.ll_state.append(node_val.strip())
                st.rerun()
        if st.button("Delete Specific Node", use_container_width=True):
            if node_val.strip() in st.session_state.ll_state:
                st.session_state.ll_state.remove(node_val.strip())
                st.rerun()
            else:
                st.error("Error: Value not present in list.")

    with col2:
        st.markdown("**Pointer Chain Architecture**")
        if st.session_state.ll_state:
            # Fixed: Compact single-line HTML prevents accidental Markdown code blocks
            ll_html = '<div><span style="font-weight:bold; color:#0f2a4a;">[HEAD]</span> <span class="ptr-arrow">&rarr;</span> '
            for val in st.session_state.ll_state:
                ll_html += f'<div class="node-wrapper"><div class="ll-node"><span class="ll-data">{val}</span><span class="ll-ptr">next</span></div><span class="ptr-arrow">&rarr;</span></div>'
            ll_html += '<span style="font-weight:bold; color:#64748b;">NULL</span></div>'
            st.markdown(ll_html, unsafe_allow_html=True)
        else:
            st.info("[HEAD] -> NULL (List is empty)")

        st.markdown(f"""
        <div class="log-box">Total Node Count: {len(st.session_state.ll_state)}
Dynamic Memory: Heap allocated non-contiguously
Head Node: {st.session_state.ll_state[0] if st.session_state.ll_state else 'None'}
Tail Node: {st.session_state.ll_state[-1] if st.session_state.ll_state else 'None'}</div>
        """, unsafe_allow_html=True)
        
# ==============================================================================
# MODULE 3: STACK (LIFO)
# ==============================================================================
elif module == "Module 3: Stack (LIFO)":
    st.markdown('<div class="module-title">Abstract Data Type: Stack (Last-In, First-Out)</div>', unsafe_allow_html=True)

    if "stack_state" not in st.session_state:
        st.session_state.stack_state = ["Frame 0", "Frame 1", "Frame 2"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Stack Operations**")
        item = st.text_input("Element Value", key="stk_in")
        s1, s2, s3 = st.columns(3)
        if s1.button("Push", use_container_width=True):
            if item.strip():
                st.session_state.stack_state.append(item.strip())
                st.rerun()
        if s2.button("Pop", use_container_width=True):
            if st.session_state.stack_state:
                popped = st.session_state.stack_state.pop()
                st.rerun()
            else:
                st.error("Underflow Error: Stack is empty.")
        if s3.button("Peek", use_container_width=True):
            if st.session_state.stack_state:
                st.info(f"Top Element: {st.session_state.stack_state[-1]}")
            else:
                st.warning("Stack is currently empty.")

    with col2:
        st.markdown("**Stack Register Representation**")
        if st.session_state.stack_state:
            tube_html = '<div class="stack-tube">'
            for i in range(len(st.session_state.stack_state) - 1, -1, -1):
                val = st.session_state.stack_state[i]
                if i == len(st.session_state.stack_state) - 1:
                    tube_html += f'<div class="stack-cell stack-top-cell">{val} &nbsp;&nbsp;[TOP POINTER]</div>'
                else:
                    tube_html += f'<div class="stack-cell">{val}</div>'
            tube_html += '</div>'
            st.markdown(tube_html, unsafe_allow_html=True)
        else:
            st.info("Stack Underflow State: 0 Elements")

# ==============================================================================
# MODULE 4: QUEUE (FIFO)
# ==============================================================================
elif module == "Module 4: Queue (FIFO)":
    st.markdown('<div class="module-title">Abstract Data Type: Queue (First-In, First-Out)</div>', unsafe_allow_html=True)

    if "queue_state" not in st.session_state:
        st.session_state.queue_state = ["Task A", "Task B", "Task C"]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Queue Operations**")
        q_item = st.text_input("Element Value", key="q_in")
        q1, q2 = st.columns(2)
        if q1.button("Enqueue", use_container_width=True):
            if q_item.strip():
                st.session_state.queue_state.append(q_item.strip())
                st.rerun()
        if q2.button("Dequeue", use_container_width=True):
            if st.session_state.queue_state:
                st.session_state.queue_state.pop(0)
                st.rerun()
            else:
                st.error("Underflow Error: Queue is empty.")

    with col2:
        st.markdown("**Queue Pipe Visualization**")
        if st.session_state.queue_state:
            q_html = '<div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">'
            q_html += '<span style="font-size:12px; font-weight:bold; color:#2563eb;">[FRONT]</span> '
            for idx, val in enumerate(st.session_state.queue_state):
                q_html += f'<div style="background:#ffffff; border:1px solid #0f2a4a; padding:8px 14px; font-size:13px; font-weight:bold;">{val}</div>'
                if idx < len(st.session_state.queue_state) - 1:
                    q_html += '<span style="color:#94a3b8;">&larr;</span>'
            q_html += ' <span style="font-size:12px; font-weight:bold; color:#0f2a4a;">[REAR]</span></div>'
            st.markdown(q_html, unsafe_allow_html=True)
        else:
            st.info("Queue Underflow State: 0 Elements")

# ==============================================================================
# MODULE 5: BINARY SEARCH TREE & TRAVERSALS
# ==============================================================================
elif module == "Module 5: Binary Search Tree":
    st.markdown('<div class="module-title">Non-Linear Hierarchical Structure: Binary Search Tree</div>', unsafe_allow_html=True)

    class TreeNode:
        def __init__(self, key):
            self.val = key
            self.left = None
            self.right = None

    def insert(root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = insert(root.left, key)
        elif key > root.val:
            root.right = insert(root.right, key)
        return root

    def inorder(root, res):
        if root:
            inorder(root.left, res)
            res.append(str(root.val))
            inorder(root.right, res)

    def preorder(root, res):
        if root:
            res.append(str(root.val))
            preorder(root.left, res)
            preorder(root.right, res)

    def postorder(root, res):
        if root:
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(str(root.val))

    raw_input = st.text_input("Enter Integer Keys (Space-Delimited):", "50 30 70 20 40 60 80")
    try:
        keys = [int(x) for x in raw_input.split()]
        root = None
        for k in keys:
            root = insert(root, k)

        pre, ino, post = [], [], []
        preorder(root, pre)
        inorder(root, ino)
        postorder(root, post)

        st.markdown("**Deterministic Traversal Outputs**")
        df_trav = pd.DataFrame({
            "Traversal Type": ["Preorder", "Inorder", "Postorder"],
            "Visit Order Formula": ["Root -> Left -> Right", "Left -> Root -> Right", "Left -> Right -> Root"],
            "Sequence Result": [" -> ".join(pre), " -> ".join(ino), " -> ".join(post)]
        })
        st.table(df_trav)

        st.markdown("""
        <div class="log-box">BST Verification Note:
Inorder Traversal produces a strictly sorted sequence, confirming correct Binary Search Tree insertion and traversal properties.</div>
        """, unsafe_allow_html=True)

    except ValueError:
        st.error("Validation Error: Please enter valid integer numbers only.")

# ==============================================================================
# MODULE 6: GRAPH TRAVERSALS
# ==============================================================================
elif module == "Module 6: Graph Traversals":
    st.markdown('<div class="module-title">Non-Linear Network Structure: Graph Traversals</div>', unsafe_allow_html=True)

    graph_db = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**Graph Representation (Adjacency List)**")
        for k, v in graph_db.items():
            st.text(f"Vertex {k} -> {v}")
        start_node = st.selectbox("Select Start Vertex:", list(graph_db.keys()))

    with col2:
        def bfs(start):
            visited, queue, order = set([start]), [start], []
            while queue:
                curr = queue.pop(0)
                order.append(curr)
                for nbr in sorted(graph_db[curr]):
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
            return order

        def dfs(start):
            visited, order = set(), []
            def dfs_rec(curr):
                visited.add(curr)
                order.append(curr)
                for nbr in sorted(graph_db[curr]):
                    if nbr not in visited:
                        dfs_rec(nbr)
            dfs_rec(start)
            return order

        st.markdown("**Traversal Execution Analysis**")
        bfs_res = " -> ".join(bfs(start_node))
        dfs_res = " -> ".join(dfs(start_node))

        st.markdown(f"""
        <div class="log-box">Breadth-First Search (Queue-Driven / Level Order):
Order: {bfs_res}

Depth-First Search (Stack-Driven / Recursive Backtracking):
Order: {dfs_res}</div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MODULE 7: SORTING ANALYSIS (BUBBLE SORT VS QUICKSORT)
# ==============================================================================
elif module == "Module 7: Sorting Analysis":
    st.markdown('<div class="module-title">Algorithm Performance: Bubble Sort vs. Quicksort</div>', unsafe_allow_html=True)

    data_input = st.text_input("Enter Numeric Sequence to Sort (Space-Delimited):", "64 34 25 12 22 11 90")
    try:
        elements = [int(x) for x in data_input.split()]
        
        # Bubble Sort Trace
        b_arr = list(elements)
        b_comparisons = 0
        b_swaps = 0
        b_passes = []
        n = len(b_arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                b_comparisons += 1
                if b_arr[j] > b_arr[j + 1]:
                    b_arr[j], b_arr[j + 1] = b_arr[j + 1], b_arr[j]
                    b_swaps += 1
                    swapped = True
            b_passes.append(f"Pass {i+1}: {list(b_arr)}")
            if not swapped:
                break

        # Quicksort Trace
        q_arr = list(elements)
        q_comp = [0]
        q_swaps = [0]
        q_traces = []

        def partition(low, high):
            pivot = q_arr[high]
            i = low - 1
            for j in range(low, high):
                q_comp[0] += 1
                if q_arr[j] <= pivot:
                    i += 1
                    q_arr[i], q_arr[j] = q_arr[j], q_arr[i]
                    q_swaps[0] += 1
            q_arr[i + 1], q_arr[high] = q_arr[high], q_arr[i + 1]
            q_swaps[0] += 1
            return i + 1

        def quicksort(low, high):
            if low < high:
                pi = partition(low, high)
                q_traces.append(f"Pivot placed at [{pi}] (Value: {q_arr[pi]}): {list(q_arr)}")
                quicksort(low, pi - 1)
                quicksort(pi + 1, high)

        quicksort(0, len(q_arr) - 1)

        colA, colB = st.columns(2)
        with colA:
            st.markdown("**Bubble Sort Analysis (O(n²))**")
            st.markdown(f"""
            <div class="log-box">Total Comparisons: {b_comparisons}
Total Swaps: {b_swaps}
Pass History:
""" + "\n".join(b_passes) + "</div>", unsafe_allow_html=True)

        with colB:
            st.markdown("**Quicksort Analysis (O(n log n))**")
            st.markdown(f"""
            <div class="log-box">Total Comparisons: {q_comp[0]}
Total Swaps: {q_swaps[0]}
Partition History:
""" + "\n".join(q_traces) + "</div>", unsafe_allow_html=True)

        st.markdown("**Performance Comparison Summary**")
        df_perf = pd.DataFrame({
            "Algorithm": ["Bubble Sort", "Quicksort"],
            "Average Complexity": ["O(n²)", "O(n log n)"],
            "Space Complexity": ["O(1) Auxiliary", "O(log n) Call Stack"],
            "Comparisons Count": [b_comparisons, q_comp[0]],
            "Swaps Count": [b_swaps, q_swaps[0]],
            "Deterministic Verification": [str(b_arr == sorted(elements)), str(q_arr == sorted(elements))]
        })
        st.table(df_perf)

    except ValueError:
        st.error("Validation Error: Please enter valid integer sequences.")