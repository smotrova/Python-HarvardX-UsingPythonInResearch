# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:39:34 2018

Python for Research

Week 1, Python 3 Basics

"""

import numpy as np

x = np.array([1,2,3])

x[1]

# mean is a function 
print (x.mean())

# shape is a data attribute
print(x.shape)

#=========================================

import math
print(math.pi)

# to have just value of pi
from math import pi

# to get available functions on the object
dir(x)

name = "Any"
dir(name)

dir(str)

# random sampling
import random
random.choice(x)
random.choice(["aa", "bb", "cc"])

#--------------------------------------------------------------------
# lists
numbers = [1,2,3, 8]
numbers[0]

# iverse the stringe

stroka1 = "abcde"

def inverse (stroka):
    
    newstroka = str()
    n = len(stroka)

    for i in range(0, n, 1):
        newstroka = newstroka + stroka[n-i-1]
    return newstroka

inverse(stroka1)

#---------------------------------------------------------------
# Lists

numbers = [1,2,3,4,5,6]
x = [10,11,12]

numbers+x

# reverse exisiting list
numbers.reverse()
numbers

# sort existing list
numbers.sort()
numbers

# create a new list with sorted elements

sorted_list = sorted(numbers)
sorted_list

# number of elements
len(numbers)

#------------------------------------
# Tuples, immutable

T = (1,3,6,8,)

len(T)

T + (9,11)

# acces an object in a tupple
T[1]

x = 23.17
y = 12.23

coordinate = x, y
coordinate = (x, y)

# unpack tuple
(c1, c2) = coordinate
c1
c2

# list of tuples

coordinates = [(1,2), (3,4), (5,6), (7,8), (9,10) ]

for (x,y) in coordinates:
    print(x,y)

# construct a tuple with just a one object
T1 = (2,)

# add oject to a tuple
coordinate = coordinate + (c2, c1)

# count the number 3 in a tuple
T2 = (1,2,3)
T2.count(3)

# to sum the numbers in T2
sum(T2)

# ranges
# ranges are immutable sequences of integer
range(5) 

# to see content of range object
list(range(5))

list(range(1,7))

list(range(1,7,3))

# use range objects as it is
# do not convert it in a list before to safe memory and computational time
# range keep only 3 numbers, while list contains all range of numbers

#---------------------------------------------------------------------
# Strings
# immutable seq od charakters

S = "Immutable"
len(S)

# access the element
S[-1]

# slicing
# 3 first letters
S[0:3]

# 3 last letters
S[-3:]

# is element in a string
"a" in S

max(S)

S.count("a")

# reverse a string
LS = list(S)
LS.reverse()
"".join(LS)

#------------------------------------------------------------------
# sets
# sets are unordered collection of distinct hashable objects

# tow types: set and frozen set (not mutable)
# sets cannot be indexed

set([1,2,3,4,5])

ids = set(range(5))

ids.add(5)

# nothing happens, we have 2 yet in the set
ids.add(2)

# operations on sets
male = set([1,3,5])
female = ids-male

# union
male | female

# intersection
female & male

set1={1,2,3} 
set2={2,3,4}

(set2 | set1) - (set1&set2)

# dictionaries
# Dictionaries are mapping from key objects to value objects
# consist of key:value pairs
# keys must be immutable
# dictionaries themselfs are mutable

age = {}
age = {"Tim": 25, "Jim": 39, "Tom": 42}

age["Tom"]

# to add one to Tom's year
age["Tom"] += 1

# keys is a view object
names = age.keys()
ages = age.values()

age["Pam"] = 27

# after adding new key:values
# names and ages objects are redifined automaticaly
# we do not need recalculating
names
ages

# to check membership in a dictionart

"Tom" in age

#------------------------------------------------------
# Notes 

# Variable names always link to object, NEVER to the other varaible
# A variable is a reference to the given object
# A variable can not reference the other variable
# A variable can only reference an object

# x = 3 reffer to object 3
# y = x reffer to object 3

# numbers are immutable
 
# y = y-1  in oder to make substractions a new object has been created
# new object is 2
# then Python create new reference to the object 2, so y=2

#--------
# mutable objects, the same logic, different results
# L1 = [2,3,4]
# L2 = L1
# l1[0] = 24

# as a result we have that L2[0] = 24
# in this case we have only one list and two names reference to the list

# L2 = list(L1) makes a copy of yhe list L1

#----------------------------------------------------------------------------

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}

for bear in bears:
    if bears[bear] == "friendly": 
        print("Hello, "+bear+" bear!")
    else:
        print("odd")

#=========================================

is_prime = True
for i in range(2,n):
    if n%i == 0:
        pass
print(is_prime)        


n=100
number_of_times = 0
while n >= 1:
   n //= 2
   number_of_times += 1
print(number_of_times)

# List comprehensions

numbers = list(range(9))
squares = []

for number in numbers:
    square = number**2
    squares.append(square)

squres2 = [number**2 for number in numbers]    

squres3 = sum([number**2 for number in numbers if number%2 !=0 ])    

#-------------------------------------------

def is_vowel(letter):
    if type(letter) == int: 
        letter = str(letter) 
    if letter in "aeiouy": 
        return(True) 
    else: 
        return(False) 
     
is_vowel(4)


# --------------------------------------------

def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N = i*N
     return(N)
     
factorial(3)     


#-----------------------------------------------

    