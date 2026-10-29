class SortingModule:
    @staticmethod
    def bubble_sort(arr):
        a = list(arr)
        n = len(a)
        comparisons = 0
        swaps = 0
        print("\n--- BUBBLE SORT TRACE ---")
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparisons += 1
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1
                    swapped = True
            print(f"Pass {i + 1}: {a}")
            if not swapped:
                print("-> Array is sorted early. Terminating passes.")
                break
        print(f"Summary: Total Comparisons = {comparisons}, Total Swaps = {swaps}")
        return a

    @staticmethod
    def quicksort_trace(arr):
        a = list(arr)
        steps = []
        comparisons = [0]
        swaps = [0]

        def partition(low, high):
            pivot = a[high]
            i = low - 1
            for j in range(low, high):
                comparisons[0] += 1
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
                    swaps[0] += 1
            a[i + 1], a[high] = a[high], a[i + 1]
            swaps[0] += 1
            return i + 1

        def qs(low, high):
            if low < high:
                pi = partition(low, high)
                steps.append(f"Sub-partition (Pivot {a[pi]} placed at index {pi}): {list(a)}")
                qs(low, pi - 1)
                qs(pi + 1, high)

        print("\n--- QUICKSORT TRACE ---")
        qs(0, len(a) - 1)
        for s in steps:
            print(s)
        print(f"Summary: Total Comparisons = {comparisons[0]}, Total Swaps = {swaps[0]}")
        return a

    def run(self):
        while True:
            print("\n--- [7] SORTING ALGORITHMS (BUBBLE SORT & QUICKSORT) ---")
            raw = input("Enter numbers separated by spaces (e.g., 64 34 25 12 22 11 90) or '0' to back: ").strip()
            if raw == '0':
                break
            try:
                numbers = [int(x) for x in raw.split()]
                if not numbers:
                    print("-> Error: No numbers entered.")
                    continue
            except ValueError:
                print("-> Error: All elements must be valid integers.")
                continue

            print("\nOriginal Array:", numbers)
            b_res = self.bubble_sort(numbers)
            q_res = self.quicksort_trace(numbers)
            print("\nVerification:")
            print("Bubble Sort Result:", b_res)
            print("Quicksort Result:  ", q_res)
            print(f"Identical Outputs: {b_res == q_res}")
            input("\nPress Enter to continue...")
            break