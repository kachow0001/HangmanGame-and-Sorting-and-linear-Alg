"""
linear search algorithm using List implmentation
"""


def linear_search(my_list, target):
    for x in range(len(my_list)):
        if my_list[x] == target:
            print("Found at index", x)
            return x

    print("Target not in list")
    return -1


my_list = [100, 5, 18, 12, 2, 0]
linear_search(my_list, 5)
linear_search(my_list, 14)
linear_search(my_list, 12)
