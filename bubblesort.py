"""
Sorting algorithm => Bubble Sorts the list in order , pushes the higher value to last
?
Tranverse through list by comparing two elements adjacent until it is ordered
"""

unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    # holds val of highest index of the passed-in list by subtracting one from length
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            # pick out index 0,1 from list
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                # swapping the values
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)

            if list_changed == False:
                break


bubblesort(unsorted_list)
