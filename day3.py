# # fibonacci series
# a, b = 0, 1
# while a < 10:
#     print(a, end=' ')
#     a, b = b, a + b


# # for leet
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
        
#         return b

# # tribonacci series 
# a, b, c = 0, 1, 1
# while a < 30:
#     print(a, end=' ')
#     a, b, c = b, c, a + b + c

# # for leet
# # for leeet
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
        
#         a, b, c = 0, 1, 1
        
#         for _ in range(3, n + 1):
#             a, b, c = b, c, a + b + c
        
#         return c
    
# # list([1, 2, 3, 4, 5])
# # list indices (positive and negative)
# # list slicing (start, end, step)
# # list methods (append, insert, remove, pop, clear, index, count, sort, reverse)
# # list operations (concatenation, repetition, membership)
# # mapping (map, filter, reduce)

# # list
# list=[11, 21, 39, 43, 52]
# print(list[2])
# # o/p: 39

# # list slicing makes a new data structure
# # syntax [start index : end index]

# print(list[1:4])
# print(list[:4])
# # o/p: [21, 39, 43]
# # o/p: [11, 21, 39, 43]

# # list operators (concatenation +, repetition *)
 
# a=[1, 2, 3]
# b=[4, 5, 6]
# print(a+b)
# print(a*3)
# # o/p: [1, 2, 3, 4, 5, 6]
# # o/p: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# # list membership operators (in, not in)

# fruits=['apple', 'banana', 'cherry']
# print('banana' in fruits)
# print('grape' not in fruits)
# print('orange' in fruits)
# # o/p: True
# # o/p: True
# # o/p: False

# # comparison operators (==, !=, >, <, >=, <=)
# one=[1, 2, 3]
# two=[1, 3, 4]
# print(one==two)
# print(one<two)

# # repetation operators (*, **)
# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# # index
# print(a[2])
# # slice
# print(a[1:4])
# # repetation
# print(a*3,b*2)
# # membership
# print(3 in a)
# print(5 in b)
# # comparison
# print(a==b)
# print(a<b)
# print(a>b)

# # list methods (append, insert, extend, remove, pop, clear, index, count, sort, reverse, copy)

# # append is to add an element at the end of the list
# num=[1, 2, 3, 4, 5]
# num.append(6)
# print(num)

# # insert is to add an element at a specific index
# num.insert(2, 10)
# print(num)

# # extend is to add multiple elements at the end of the list
# a=[1, 2, 3]
# b=[4, 5, 6]
# a.extend(b)
# print(a)

# # remove is to remove an element from the list
# a=[1, 2, 3, 4, 5]
# a.remove(4)
# print(a)

# # pop is to remove an element from the list and return it
# num=[1, 2, 3, 4, 5]
# num.pop(2)
# print(num) 

# # clear is to remove all elements from the list
# num.clear()
# print(num)

# # index is to find the index of an element in the list
# num=[1, 2, 3, 4, 5]
# print(num.index(3))

# # count is to count the number of occurrences of an element in the list
# num=[1, 2, 3, 4, 5, 3, 3]
# print(num.count(1))

# # sort is to sort the elements of the list in ascending order
# num=[5, 2, 3, 1, 4]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)

# # reverse is to reverse the order of the elements in the list
# num=[1, 2, 3, 4, 5]
# num.reverse()
# print(num)

# # copy is to create a copy of the list
# num=[1, 2, 3, 4, 5]
# b=num.copy()
# print(b)
 

# # lambda function (anonymous function)
# # map(), filter() and list()--->funtional programming--->iterates

# # should use it on list

# num=[1, 2, 3, 4, 5]
# result = list(map(lambda x: x**2, num))
# print(result)
# def fun(x):
#     return x*2
# result = list(map(fun, num))
# print(result)

# num1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# resultone=list(filter(lambda x: x%2==0, num1))
# print(resultone)

# # convert into a single value --->functional module
# from functools import reduce
# num=[1, 2, 3, 4, 5]
# result=reduce(lambda x, y: x+y, num)
# print(result)
    
# # seperate odd and even
# num1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# even=list(filter(lambda x: x%2==0, num1))
# odd=list(filter(lambda x: x%2!=0, num1))
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# # palindrome
# word=input("Enter a word: ")
# if word==word[::-1]:
#     print("The word is a palindrome.") 
# else:
#     print("The word is not a palindrome.")

# method 2
word=input("Enter a word: ")
rev=""
for ch in word:
    rev=ch+rev
if word==word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
