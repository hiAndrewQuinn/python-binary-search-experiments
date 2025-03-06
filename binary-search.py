import random

# ANSI color codes for visualizing in the terminal
COLOR_START = "\033[92m"
COLOR_END = "\033[0m"


def visualize_search(L, l, r):
    visual = []
    for i, num in enumerate(L):
        if l <= i < r:
            visual.append(f"{COLOR_START}{num}{COLOR_END}")
        else:
            visual.append(str(num))
    print("List: [" + " ".join(visual) + "]")


def binary_search(L, T, verbose=False):
    """
    Standard binary search. Given an element T, return the index of L which contains T, or -1 if T is not found in L.
    If verbose is True, prints step-by-step details of the search visually.
    """

    l, r = 0, len(L)
    while l < r:
        if verbose:
            visualize_search(L, l, r)
        assert T in L[l:r]
        mid = l + (r - l) // 2
        if verbose:
            print(f"Middle element at index {mid} is {L[mid]}")
        if L[mid] == T:
            if verbose:
                print(f"Element {T} found at index {mid}")
            return mid
        elif L[mid] > T:
            assert T in L[l:mid]
            r = mid
        elif L[mid] < T:
            assert T in L[mid + 1 : r]
            l = mid + 1

        if verbose:
            print()
            visualize_search(L, l, r)

    if verbose:
        print(f"Element {T} not found")
    return -1


def test_binary_search():
    # General randomized testing
    for size in [12, 50, 100]:
        L = sorted(random.sample(range(-100, 100), size))

        for _ in range(20):
            T = random.choice(L)
            assert binary_search(L, T) != -1, f"Failed to find existing element {T}"

    print("All randomized tests passed.")


def detailed_test():
    size = 20
    L = sorted(random.sample(range(-100, 100), size))
    print(f"Testing detailed binary search on list: {L}")

    T = random.choice(L)
    print(f"\nDetailed visual search for existing element {T}:")
    binary_search(L, T, verbose=True)

    T = 101  # Guaranteed not present
    print(f"\nDetailed search for non-existing element {T}:")
    try:
        binary_search(L, T, verbose=True)
    except AssertionError:
        print(f"Element {T} correctly identified as not present.")


if __name__ == "__main__":
    test_binary_search()
    detailed_test()
