

import random
import time


def merge_sort(arr):
    """Implement the Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left
    
    merged = []
    i = j = 0
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def shell_sort(arr):
    """Implement the Shell Sort algorithm."""
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr
def generate_random_numbers(n):
    """Generate a list of n random numbers between 1 and 1000."""
    return [random.randint(1, 1000) for _ in range(n)]


def main():
    # Generate a list of 100,000 random numbers
    numbers = generate_random_numbers(100000)

    # Merge Sort Algorithm
    merge_start_time = time.time()
    sorted_numbers_merge = merge_sort(numbers)
    merge_end_time = time.time()

    merge_execution_time = (merge_end_time - merge_start_time) * 1000

    # Shell Sort Algorithm
    shell_start_time = time.time()
    sorted_numbers_shell = shell_sort(numbers)
    shell_end_time = time.time()

    shell_execution_time = (shell_end_time - shell_start_time) * 1000

    # Print the execution times
    print("\n")
    print("\033[1;31;40mMerge Sort Execution Time:", merge_execution_time, "ms\033[0m")

    print("\033[1;31;40mShell Sort Execution Time:", shell_execution_time, "ms\033[0m")
    # Condition to check what excution time is faster and print out Best algorithm selection rationale
    if merge_execution_time < shell_execution_time:
      print("\033[32m\nFrom the Above experiment we able to denote Merge sort  has an Execution time of ", merge_execution_time, "ms", " \nAnd hence is the Best Agorithm since it has  a faster Execution time\033[0m")    
    else:
          print("\033[32m\nFrom the Above experiment we able to denote Shell sort  has an Execution time of ", shell_execution_time, "ms", " \nAnd hence is the Best Agorithm since it has  a faster Execution time\033[0m") 
    print("\n")
if __name__ == '__main__':
    main()