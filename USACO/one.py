# 1. What is the probability of rolling 3 dice and getting the sum of the numbers on the 3 dices
# be 11 or 12?
# def sum3dice():
#     dice1 = [1,2,3,4,5,6]
#     dice2 = [1,2,3,4,5,6]
#     dice3 = [1,2,3,4,5,6]
#     all_outcomes = 0
#     wanted_outcomes = 0
#     for i in dice1:
#         for j in dice2:
#             for k in dice3:
#                 if i + j + k == 12 or i + j + k == 11:
#                     wanted_outcomes += 1
#                 all_outcomes += 1
#     return f"{wanted_outcomes / 4}/{all_outcomes / 4}"
# print(sum3dice())

# 2. There is a list that contains the letters "A", "B", "C" and "D". Print all possible 4-character
# combinations that can be formed using these 4 letters such that all the 4 letters exist in the line.
# Example: ABCD, BACD, CDAB... 
# def all4charcombos(l):
#     combos = []
#     for a in l:
#         for b in l:
#             for c in l:
#                 for d in l:
#                     if len(set([a,b,c,d])) == len([a,b,c,d]):
#                         combos.append([a,b,c,d])
#     return combos
# print(all4charcombos(["A","B","C","D"]))

# 3. In Binary, 4 is represented as 100. Because, the conversion to decimal is made by multiplying
#  from the left, each number with increasing powers of 2. For example, in case of 4.
#  =(0*2^0) + (0*2^1) + (1*2^2)
#  = 4 + 0 + 0
#  = 4.
# Write a Python program which can do the same for a user inputted number.
# def binary2num(n):
#     int_n = 0
#     reversed_n = [int(a) for a in str(n)]
#     reversed_n.reverse()
#     for i in range(len(reversed_n)):
#         int_n = int_n + (reversed_n[i] * 2**i)
#     return int_n
# print(binary2num(1001))

# 4. Print the pattern entered below using nested for loops.
# ****_
# ***__
# **___
# *____
# **___
# ***__
# ****_
# def pattern():
#     star_pattern = ['*','*','*','*','*']
#     for i in range(4, 0, -1):
#         star_pattern[i] = '_'
#         print(''.join(star_pattern))
#     for i in range(1,4):
#         star_pattern[i] = '*'
#         print(''.join(star_pattern))
# pattern()

# 5. Find the sum of all prime numbers below 200.
# def allprimesunder200():
#     primes = []
#     prime = True
#     for i in range(200):
#         prime = True
#         for j in range(2, int(i/2)+1):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             primes.append(i)
#     print(primes)
#     return sum(primes)
# print(allprimesunder200())

# 6. Write a program that puts 10 random integers between 1 and 10 into a list such that there
# are no repeating numbers.
# import random
# def randomdiff10num():
#     l = []
#     while len(l) != 10:
#         n = random.randint(1,10)
#         if n not in l:
#             l.append(n)
#     return l
# print(randomdiff10num())

# 7. Assume a = [[[1,2], [3,4]]]
#  b = [[[5,6], [7,8]]]
#  Add the corresponding elements in each matrix.
# import numpy as np
# def addElementsInMatrix():
#     a = [[[1,2], [3,4]]]
#     b = [[[5,6], [7,8]]]
#     return np.sum([a + b], axis=1)
# print(addElementsInMatrix())

# 8. A koala wants to climb a ladder of 100 steps. In every try, it can go up 3 steps and comes down either
#  1 step or 2 steps. What is the most and the least number of tries it might need to touch the top?
# def koala():
#     most = 0
#     least = 0
#     i = 0
#     while i != 100:
#         most += 3
#         most -= 2
#         i += 1
#     i = 0
#     while i != 100 and least != 100:
#         least += 3
#         least -= 1
#         i += 1
#     return most, i
# print(koala())

# 9. Write a program that finds all the factors of a user given number that are odd.
# def oddFactors(n):
#     l = []
#     for i in range(1, n-1):
#         if n % i == 0:
#             if i % 2 != 0:
#                 l.append(i)
#     return l
# print(oddFactors(18))

# 10. Generate a 16-digit product key containing both letters as well as numbers. There should be at least
#  4 numbers in the key but they should all be at least 2 spaces away from each other. 
# import random
# def productKey():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
#     key = ''
#     for i in range(16):
#         if i % 3 == 0:
#             key += alphabet[random.randint(25,35)]
#         else:
#             key += alphabet[random.randint(0,25)]
#     return key
# print(productKey())
