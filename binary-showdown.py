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
    max_value = 99

    print("Trial\tL\tT\tBinarySearch\tWikipedia\tBottenbruch")
    print("=" * 120)

    for trial in range(num_trials):
        L = sorted(random.choices(range(10, max_value + 1), k=array_size))  # Allow duplicates
        T = random.choice(L + [max_value + 1])  # Ensure some misses

        result1, iter1, comp1 = binary_search(L, T)
        result2, iter2, comp2 = binary_search_wikipedia(L, T)
        result3, iter3, comp3 = binary_search_bottenbruch(L, T)

        row = f"{trial:<5}\t{L}\t{T:<2}\t{result1:<12}\t{result2:<12}\t{result3:<12}"

        results = {result1, result2, result3}
        
        if len(results) == 1:
            rprint(f"[green]{row}[/green]")  # All same
        elif -1 in results or len(results) > 1 and any(L[r] != L[next(iter(results - {-1}))] for r in results if r != -1):
            rprint(f"[red]{row}[/red]")  # Different indices mapping to different elements or one result is -1
        else:
            rprint(f"[yellow]{row}[/yellow]")  # Indices are different but point to the same value

def run_large_experiment():
    num_trials = 1000
    array_size = 1000
    max_value = 2**32
    
    total_iterations = {"binary": 0, "wikipedia": 0, "bottenbruch": 0}
    total_comparisons = {"binary": 0, "wikipedia": 0, "bottenbruch": 0}
    
    for _ in range(num_trials):
        L = sorted(random.choices(range(max_value), k=array_size))
        T = random.choice(L + [max_value + 1])
        
        _, iter1, comp1 = binary_search(L, T)
        _, iter2, comp2 = binary_search_wikipedia(L, T)
        _, iter3, comp3 = binary_search_bottenbruch(L, T)
        
        total_iterations["binary"] += iter1
        total_iterations["wikipedia"] += iter2
        total_iterations["bottenbruch"] += iter3
        
        total_comparisons["binary"] += comp1
        total_comparisons["wikipedia"] += comp2
        total_comparisons["bottenbruch"] += comp3
    
    print("\nLarge-Scale Experiment Results")
    print("=" * 50)
    print("Algorithm      | Avg Iterations | Avg Comparisons")
    print("-" * 50)
    for key in total_iterations:
        avg_iter = total_iterations[key] / num_trials
        avg_comp = total_comparisons[key] / num_trials
        print(f"{key.capitalize():<14} | {avg_iter:<14.2f} | {avg_comp:<15.2f}")

if __name__ == "__main__":
    run_experiments()
    run_large_experiment()

