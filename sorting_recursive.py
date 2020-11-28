#!python
import time

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    newList = []
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    # if both lists empty return newList
    if not items1 and not items2:
        return newList
    # if list1 is not empty but list2 is 
    # append list1 to new list and return vice-versa
    if items1 and not items2:
        return newList + items1
    if not items1 and items2:
        return newList + items2
    # if boths lists are not empty
    if items1 and items2:
        # check if item at 0 in list1 is smaller than item at 0 in list2
        if items1[0] <= items2[0]:
            # add smallest item from list1 to newList
            newList.append(items1[0])
            # recursive call on the items1 from index 1 to lenght. 
            # item at 0 is now in newlist
            newList = newList + merge(items1[1:], items2)
            # add smallest item from list2 to newList
        if items1[0] > items2[0]:
            newList.append(items2[0])
            # recursive call on the items2 from index 1 to lenght. 
            # item at 0 is now in newlist
            newList = newList + merge(items1, items2[1:])
    return newList
    
      
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) > 1:
    
        # TODO: Split items list into approximately equal halves
        mid = len(items)//2
        right = items[mid:]
        left = items[:mid]
        
        # TODO: Sort each half by recursively calling merge sort
        merge_sort(right)
        merge_sort(left)
        
        # TODO: Merge sorted halves into one list in sorted order
        l = 0
        r = 0
        i = 0
 
        left_size = len(left)
        right_size = len(right)
        while l < left_size and r < right_size:
            if left[l] < right[r]:
              items[i] = left[l]
              l += 1
            else:
                items[i] = right[r]
                r += 1
             
            i += 1
 
        while l < left_size:
            items[i] = left[l]
            l += 1
            i += 1
 
        while r < right_size:
            items[i]=right[r]
            r += 1
            i += 1
            
    return items
# time complexity: O(n*Log n)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: high index) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    index = ( low-1 )
    pivot = items[high]
    
    # TODO: Loop through all items in range [low...high]
    for j in range(low, high):
        # TODO: Move items less than pivot into front of range [low...p-1] 
        if items[j] <= pivot:
            # increment index of smaller element 
            index += 1
            items[index],items[j] = items[j],items[index]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    items[index+1],items[high] = items[high],items[index+1] 
    
    # TODO: Move pivot item into final position [p] and return index p
    return index+1 

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low == None:
        low = 0
    if high == None: 
        high = len(items)-1
    
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) < 1:
        return items
    
    if low < high:
        # TODO: Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        
        # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot-1)   #before the pivot
        quick_sort(items, pivot+1, high)   #after the pivot
    
    return items
    
if __name__=="__main__":
    listA = [1, 2, 3, 4, 5]
    listB = [6, 7, 8, 9, 10]
    unsortedList = [2, 1, 10, 7, 100, 5, 8]
    # start = time.time()
    # print(merge(listA, listB))
    # end = time.time()
    # print("Time to run merge: {}".format(end-start))
    print(quick_sort(unsortedList))