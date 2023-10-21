# Given on a 10-point scale for the biology assessments of three students. Write a program that prints the set of scores that are not found in any of the three students.

a, b, c = set(int(i) for i in input().split()), set(int(i) for i in input().split()), set(int(i) for i in input().split())
x = a | b | c
s = [int(i) for i in range(11)]

for i in x:
    for j in s:
        if j == i:
            s.remove(i)

for i in sorted(s):
    print(i, end = ' ')
