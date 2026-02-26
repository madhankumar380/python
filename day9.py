# priority queue
# remove element based on elements/priority intead of order of insertion

# highest priority element is removed first
# not normal fifo
# smallest number has highest priority

# task-1
# task-3
# task-2

# real time example
# hospital emergency room
# cpu task scheduling
# printer task prority
# network packet routing

# normal_queue vs priority_queue

# heap
# smallest number=highest priority
# automatic sorting
# uses heap moduls

# pseudocode

# insert
# import heapq
# create empty priority queue- create empty list
# insert element with priority
# heap arranges automaticallay 

# remove
# remove smallest priority element

# import heapq

# pq = []

# heapq.heappush(pq,3)
# heapq.heappush(pq,2)
# heapq.heappush(pq,1)

# print("Priority Queue:", pq)

# print("Removed element:", heapq.heappop(pq))
# print("Removed element:", heapq.heappop(pq))
# print("Removed element:", heapq.heappop(pq))

# 83) remove duplicates from sorted list

# def removeDuplicates(nums):
#     if not nums:
#         return[]
#     result=[nums[0]]
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]:
#             result.append(nums[i])
#     return result
# print(removeDuplicates([1, 1, 2, 3, 3, 4]))

# 557) reverse words in a string

def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
s = "Hello World"
print(reverseWords(s))


