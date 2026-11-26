"""
Assessment 3.7: Sorting Algorithms
Sorts the letters of a full name using Bubble Sort.

Rules:
  - Two arrays: unsorted and sorted
  - Duplicate letters are discarded
  - Symbols (anything that is not a letter) are excluded
"""

def build_unsorted_array(full_name):
    """Keep letters only, discard symbols/spaces/digits and duplicate letters."""
    unsorted = []
    for ch in full_name:
        if not ch.isalpha():          # exclude symbols, spaces, numbers
            continue
        ch = ch.upper()               # so 'a' and 'A' count as the same letter
        if ch not in unsorted:        # discard duplicates
            unsorted.append(ch)
    return unsorted


def bubble_sort(arr):
    """Bubble Sort: repeatedly swap adjacent items that are out of order."""
    result = arr.copy()               # keep the unsorted array untouched
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:               # already sorted, stop early
            break
    return result


if __name__ == "__main__":
    FULL_NAME = input("Enter your full name: ")
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = bubble_sort(unsorted_array)

    print("Full Name :", FULL_NAME)
    print("Unsorted  :", unsorted_array)
    print("Sorted    :", sorted_array)
