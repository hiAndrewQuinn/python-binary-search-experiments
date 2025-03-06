import random
from typing import List, Optional, Any

COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"
COLOR_REVERSE = "\033[7m"


def visualize_search(
    L: List[Any], l: int, r: int, mid: Optional[int] = None, label: str = ""
) -> None:
    """
    Visualizes the current state of the binary search algorithm.

    Parameters:
        L (list): The list being searched.
        l (int): The left boundary index of the current search space.
        r (int): The right boundary index of the current search space.
        mid (int, optional): The middle index being evaluated. Default is None.
        label (str): Label describing the type of binary search.
    """
    visual_list = ""

    for i, num in enumerate(L):
        if i == r:
            visual_list += f"{COLOR_RED}{num:3}{COLOR_RESET} "
        elif l <= i < r:
            if i == mid:
                visual_list += f"{COLOR_GREEN}{COLOR_REVERSE}{num:3}{COLOR_RESET} "
            else:
                visual_list += f"{COLOR_GREEN}{num:3}{COLOR_RESET} "
        else:
            visual_list += f"{num:3} "

    markers = f"l = {l}, m = {mid}, r = {r}"
    print(f"{label:<12} {visual_list}    {markers}")


def binary_search(L: List[Any], T: Any, verbose: bool = False) -> int:
    """
    Performs standard binary search to find any occurrence of target T in sorted list L.

    Preconditions:
        - L must be sorted in ascending order.

    Parameters:
        L (list): Sorted list in which to search.
        T (comparable): Target element to find.
        verbose (bool): If True, visualizes each search step.

    Returns:
        int: Index of the target element if found, otherwise -1.
    """
    l, r = 0, len(L)
    while l < r:
        mid = l + (r - l) // 2

        if verbose:
            visualize_search(L, l, r, mid, "Binary")

        if L[mid] == T:
            return mid
        elif L[mid] < T:
            l = mid + 1
        else:
            r = mid

    return -1


def binary_search_leftmost(L: List[Any], T: Any, verbose: bool = False) -> int:
    """
    Finds the leftmost (first) occurrence of target T in sorted list L using binary search.

    Preconditions:
        - L must be sorted in ascending order.

    Parameters:
        L (list): Sorted list in which to search.
        T (comparable): Target element to find.
        verbose (bool): If True, visualizes each search step.

    Returns:
        int: Index of the leftmost occurrence of T, or the index where it would be inserted.
    """
    l, r = 0, len(L)
    while l < r:
        mid = l + (r - l) // 2

        if verbose:
            visualize_search(L, l, r, mid, "Leftmost")

        if L[mid] < T:
            l = mid + 1
        else:
            r = mid

    if verbose:
        visualize_search(L, l, r, label="Leftmost")

    return l


def binary_search_rightmost(L: List[Any], T: Any, verbose: bool = False) -> int:
    """
    Finds the rightmost (last) occurrence of target T in sorted list L using binary search.

    Preconditions:
        - L must be sorted in ascending order.

    Parameters:
        L (list): Sorted list in which to search.
        T (comparable): Target element to find.
        verbose (bool): If True, visualizes each search step.

    Returns:
        int: Index of the rightmost occurrence of T, or the index just before where it would be inserted.
    """
    l, r = 0, len(L)
    while l < r:
        mid = l + (r - l) // 2

        if verbose:
            visualize_search(L, l, r, mid, "Rightmost")

        if L[mid] <= T:
            l = mid + 1
        else:
            r = mid

    if verbose:
        visualize_search(L, l, r, label="Rightmost")

    return l - 1


def detailed_tests() -> None:
    """
    Runs example tests for standard, leftmost, and rightmost binary searches on a randomly generated sorted list.
    """
    L = sorted(random.choices(range(0, 20), k=20))
    print(f"Testing leftmost, rightmost, and ordinary binary search on list:\n{L}\n")

    T = random.choice(L)

    print(f"Ordinary binary search for element {T}:")
    idx = binary_search(L, T, verbose=True)
    if idx != -1:
        print(f"Element {T} found at index {idx}\n")
    else:
        print(f"Element {T} not found\n")

    print(f"Searching leftmost occurrence of {T}:")
    left_idx = binary_search_leftmost(L, T, verbose=True)
    if left_idx < len(L) and L[left_idx] == T:
        print(f"Leftmost occurrence of {T} found at index {left_idx}\n")
    else:
        print(f"Element {T} not found\n")

    print(f"Searching rightmost occurrence of {T}:")
    right_idx = binary_search_rightmost(L, T, verbose=True)
    if right_idx >= 0 and L[right_idx] == T:
        print(f"Rightmost occurrence of {T} found at index {right_idx}\n")
    else:
        print(f"Element {T} not found\n")


if __name__ == "__main__":
    detailed_tests()
