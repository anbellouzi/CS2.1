#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    minimum = min(numbers)
    maximum = max(numbers)
        
    # TODO: Create list of counts with a slot for each number in input range
    counts = [[x, 0] for x in set(numbers)]
    
    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
        for i in range(0, len(counts)):
            if num == counts[i][0]:
                counts[i][1] += 1
    
    # TODO: Loop over counts and append that many numbers into output list
    output = []
    for count in counts:
        for _ in range(count[1]):
            output.append(count[0])
    # FIXME: Improve this to mutate input instead of creating new output list
    return output

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    minimum = min(numbers)
    maximum = max(numbers) 
    num_range = maximum - minimum
    # print(num_range)
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = []
    for i in range(num_buckets+1):
        buckets.append([])
    
    # print(len(buckets))
    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        # print(buckets)
        # print("{} is {}".format(((num - minimum) * 100) / num_range, num))
        index = int((int((num - minimum) * 100) / num_range) / num_buckets)
        # print(num, index)
        # print(buckets[index])
        buckets[index].append(num)
        # print(buckets)
        
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for bucket in buckets:
        for i in range(1, len(bucket)):
            j = i - 1
            num = bucket[i]
            while j >= 0:
                if bucket[i] < bucket[j]:
                    bucket[j+1] = bucket[j]
                    bucket[j] = num
                    j -= 1
                else:
                    break
        
    output = []
    # TODO: Loop over buckets and append each bucket's numbers into output list
    for bucket in buckets:
        for num in bucket:
            output.append(num)
    # FIXME: Improve this to mutate input instead of creating new output list
    return output
    
    
nums = [10, 22, 2, 1, 5, 15, 18, 6, 4, 18, 17, 19]
print("Bucket sort: ", bucket_sort(nums))

nums = [10, 22, 2, 1, 5, 15, 18, 6, 4, 18, 17, 19]
print("Counting sort: ", counting_sort(nums))