#!/bin/python3
# Dutch national flag problem


# def solve_pivot(arr, pivot):
#     pivot_element = arr[pivot]
#     smaller = []
#     equal = []
#     larger = []
#     for el in arr:
#         if el < pivot_element:
#             smaller.append(el)
#         elif el == pivot_element:
#             equal.append(el)
#         else:
#             larger.append(el)
#     return smaller + equal + larger

def solve_pivot(A, pivot):
    pivot_element = A[pivot]
    smaller = 0
    equal = 0
    larger = len(A)
    while equal < larger:
        print(A)
        if A[equal] < pivot_element:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot_element:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A


if __name__ == '__main__':
    arr = [0, 1, 2, 0, 3, 2, 1, 1]
    pivot = 1
    result = solve_pivot(arr, pivot)
    print(result)
