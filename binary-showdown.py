import random
import math
from rich import print as rprint  # Using rich for colored output

def binary_search(L, T):
    l, r = 0, len(L)
    iterations = 0
    comparisons = 0

    while l < r:
        iterations += 1
        mid = l + (r - l) // 2
        comparisons += 1  # Comparison for equality

        if L[mid] == T:
            return mid, iterations, comparisons
        comparisons += 1  # Comparison for greater
        if L[mid] > T:
            r = mid
        else:
            l = mid + 1

    return -1, iterations, comparisons

def binary_search_wikipedia(L, T):
    l, r = 0, len(L) - 1
    iterations = 0
    comparisons = 0

    while l <= r:
        iterations += 1
        mid = (l + r) // 2
        comparisons += 1  # Comparison for equality

        if L[mid] == T:
            return mid, iterations, comparisons
        comparisons += 1  # Comparison for greater
        if L[mid] > T:
            r = mid - 1
        else:
            l = mid + 1

    return -1, iterations, comparisons

def binary_search_bottenbruch(L, T):
    l, r = 0, len(L) - 1
    iterations = 0
    comparisons = 0

    while l != r:
        iterations += 1
        mid = math.ceil((l + r) / 2)
        comparisons += 1  # Comparison for greater

        if L[mid] > T:
            r = mid - 1
        else:
            l = mid
    
    comparisons += 1  # Final comparison
    if L[l] == T:
        return l, iterations, comparisons
    return -1, iterations, comparisons

def run_experiments():
    num_trials = 20
    array_size = 20
    max_value = 20

    print("Trial\tL\tT\tBinarySearch\tWikipedia\tBottenbruch")
    print("=" * 120)

    for trial in range(num_trials):
        L = sorted(random.choices(range(10, max_value + 1), k=array_size))  # Allow duplicates
        T = random.choice(L + [max_value + 1])  # Ensure some misses

        result1, _, _ = binary_search(L, T)
        result2, _, _ = binary_search_wikipedia(L, T)
        result3, _, _ = binary_search_bottenbruch(L, T)

        row = f"{trial:<5}\t{L}\t{T:<2}\t{result1:<12}\t{result2:<12}\t{result3:<12}"

        results = {result1, result2, result3}
        
        if len(results) == 1:
            rprint(f"[green]{row}[/green]")  # All same
        elif -1 in results or len(results) > 1 and any(L[r] != L[next(iter(results - {-1}))] for r in results if r != -1):
            rprint(f"[red]{row}[/red]")  # Different indices mapping to different elements or one result is -1
        else:
            rprint(f"[yellow]{row}[/yellow]")  # Indices are different but point to the same value

if __name__ == "__main__":
    run_experiments()

