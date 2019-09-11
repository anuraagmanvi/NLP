# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:33:20 2019

@author: Anuraag Manvi

i/p
5
12345
12134
2
1345
1325
o/p
4
4
"""

n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = int(input())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

for i in range(q):
    print(i)
    a1 = a[l1[i]-1:l1[++1]]
    a1.extend(b[l1[++i]-1:l1[++i]])

#-5 -4 2 6 -3 7 2 8
#-5 -8 2 7 1 -2 6 3 

a = list(map(int, input().split()))
n=list()
p=list()
for i in range(len(a)):
    if a[i]<0:
        n.append(a[i])
    else:
        p.append(a[i])

a = n+p
print(*a, sep=', ')


def rev(n):
    if n<10:
      print(n)
    else:
        print(n%10, end='')
        rev(n//10)
    
print(rev(1234))