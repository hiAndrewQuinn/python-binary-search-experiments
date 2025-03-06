import random

COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"
COLOR_REVERSE = "\033[7m"


def visualize_search(L, l, r, mid=None):
    visual_list = ""

    # Highlight range [l, r) in green, r in red
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
    print(f"{visual_list}    {markers}")


def binary_search(L, T, verbose=False):
    l, r = 0, len(L)
    while l < r:
        mid = l + (r - l) // 2

        if verbose:
            visualize_search(L, l, r, mid)

        if L[mid] == T:
            if verbose:
                print(f"Element {T} found at index {mid}\n")
            return mid
        elif L[mid] > T:
            r = mid
        else:
            l = mid + 1

    if verbose:
        visualize_search(L, l, r)
        print(f"Element {T} not found\n")
    return -1


def test_binary_search():
    for _ in range(20):
        L = sorted(random.sample(range(0, 999), 12))
        T = random.choice(L)
        assert binary_search(L, T) != -1, f"Failed on element {T}"

    print("All randomized tests passed.")


def detailed_test():
    size = 12
    L = sorted(random.sample(range(-100, 101), size))
    print(f"Detailed binary search on list:\n{L}\n")

    T = random.choice(L)
    print(f"Visual search for existing element {T}:")
    binary_search(L, T, verbose=True)

    T = 101  # guaranteed outside range
    print(f"Visual search for non-existing element {T}:")
    binary_search(L, T, verbose=True)


if __name__ == "__main__":
    test_binary_search()
    detailed_test()

