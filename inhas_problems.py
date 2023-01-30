"""
      All of these logics have been created as for te solution to homeworks from python.
      Course Intro to It.


      Solved by @Davlatbek_Kobiljonov.  -> Telegram Username.
      Student of Inha University in Tashkent.

      26.01.23
"""

# 1. Given a string type AAAAAAABBBBCCCCCCCCDDD
# And we should convert it into this form 7A4B8C3D
# print('Given decompressed string type: AAAAAAABBBBCCCCCCCCDDD')
# s = 'AAAAAAABBBBCCCCCCCCDDD'
# x = []
# al = ['A', 'B', 'C', 'D']
# for i in al:
#     if i in s:
#         x.append(str(s.count(f'{i}')) + i)
# print("Compressed string: ", ''.join(x))
#
# # 2. Given a string type  7A4B8C3D
# # And we should convert it into this form AAAAAAABBBBCCCCCCCCDDD
# s = "7A4B8C3D"
# alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' and so on...']
# b = 0
# a = 2
# alph = ['A', 'B', 'C', 'D', 'E', 'F', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'N', 'O', 'P', 'Q', 'r', 'S', 'T', 'U', 'V', 'w', 'X', 'Y', 'z']
# decompressed = []
# print(f'Provided RLE String: {s}')
# print('Decompressed RLE: ', end='')
# for i in range(len(s) // 2):
#     for j in range(int(str(s[b:a])[0])):
#         print(alph[i].title(), end='')
#     b += 2
#     a += 2
# print()
#
# # 3. Counting the number of frequencies of each letter in a given string
# word = input('Enter your sentence to check the frequencies of each letter: ')
# print('Letter  times')
# dis = []
# for letter in alph:
#     if word.lower().count(f'{letter.lower()}') != 0:
#         print(f" {letter.upper()}-{letter.lower()}  -  {word.lower().count(f'{letter.lower()}')}")
#     else:
#         dis.append(letter.lower())
# print("Letters that were not in a string: ", ', '.join(dis))
#
# # 4. Palindrome
# word = input('Enter your word ')
# isPalindrome = True
# for i in range(len(word)//2):
#     if word[i] != word[-(1+i)]:
#         isPalindrome = False
# print('isPalindrome: ', isPalindrome)


# Program that checks whether inputted number is perfect or nut
# 6 -> 1, 2, 3, 6 -> sum: 12 / 2 = 6 is perfect number
# num = int(input("Enter any number: "))
# s = 0
# for i in range(1, num):
#     if num % i == 0:
#         s += i
# if s == num:
#     print(num, " is a perfect number")
# else:
#     print(num, " is a not perfect number")


# Python function that takes a list and returns a new list with unique elements of the first list.
# lst = []
# lst1 = []
# length = int(input("Type the length of list: "))
# for i in range(length):
#     x = lst.append(input(f'lst[{i}]: '))
# for i in range(len(lst)):
#     if lst[i] not in lst1:
#         lst1.append(lst[i])#
# print(f"input = [{', '.join(lst)}]")
# print(f"output = [{', '.join(lst1)}]")


# # Program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'd': 400, 'b': 200}
# d3 = {}
# try:
#     for key in d1:
#         for key1 in d2:
#             if key == key1:
#                 d3[key] = d1[key] + d2[key1]
#             elif key != key1:
#                 if key not in d3:
#                     d3[key] = d1[key]
#                 if key1 not in d3:
#                     d3[key1] = d2[key1]
#
#     print(f"d1 = {d1}\n"
#           f"d2 = {d2}\n"
#           f"output = {d3}")
# except Exception as ex:
#     print("Error name: ", ex)
# finally:
#     print('Process finished')


# def find_index(word: str, letter: str):
#     return word.index(letter)
#
#
# word = input("Enter any word: ")
# letter = input("to find the index position of a letter enter that letter! ")
# print(f"The index position of {letter} in your word is {find_index(word, letter)}")


# # Program w to find the Max of numbers given in the list.
# def max_num(lst):
#     greatest = int(lst[0])
#     for num in lst[1:]:
#         if int(num) > greatest:
#             greatest = int(num)
#     return greatest
#
#
# lst = ['1', '-3', '4', '3', '9', '13']
# print(f"The greatest number in list is {max_num(lst)}")


# Python function which takes as an argument a list, and returns a dictionary which gives the
# frequency of the elements in a list. For example, if the list is [2,1,2,3,1,9], the result should be
# {0:0, 1:2, 2:2, 3:1, 4:0, 5:0, 6:0, 7:0, 8:0, 9:1}.
# def count_elem(list1, dict1):
#     for i in range(0, 10):
#         dict1[i] = list1.count(f"{i}")
#     return dict1
#
#
# list1 = ['2', '1', '2', '3', '1', '9']
# dict1 = {}
# print(f"input = {list1}\n"
#       f"output = {count_elem(list1, dict1)}")

# function which takes as an argument a list, and returns its reverse as a result.
# list2 = ['1', '2', '3', '4', '5']
# vertual_list = []
# print(list2.reverse())
# Another approach.
# x = len(list2) - 1
# while 0 <= x:
#     vertual_list.append(list2[x])
#     x -= 1
# To return the list2 itself throwing away unnecessary vertural_list
# list2.clear()
# for i in vertual_list:
#     list2.append(i)
# vertual_list.clear()
# print(', '.join(list2))


# list3 = ['2', '1', '2', '3', '1', '9']
# print(list3)
# n_of_rot = int(input("Enter number of rotations: "))
# print(list3[len(list3) - n_of_rot:len(list3)]+list3[0:len(list3)-n_of_rot])

# Another approach with built-in methods.
# from collections import deque
#
# deq = deque(list3)
# deq.rotate(n_of_rot)
# list3 = list(deq)
# print(list3)

# Python function that mutates L such that it reverses its elements and also reverses the order
# of the int elements in every element of L. It does not return anything.
# def reversing(L: list):
#     for i in range(len(L)):
#         L.reverse()
#         L[i].reverse()
#     return L
#
#
# L = [[1, 2], [3, 4], [5, 6, 7]]
# print('input = ', L)
# print("output = ", reversing(L))


# Function to flatten a list.
new_lst = []


def flatten(L: list):
    for n in range(len(L)):
        if type(L[n]) is list:
            flatten(L[n])
        else:
            new_lst.append(L[n])
    return new_lst


L = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print('fluttered list: ', flatten(L))
