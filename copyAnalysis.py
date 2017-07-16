#coding=utf-8
import copy
a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
a.append(5)
print(" a list append 5:")
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
a[4].append('c')
print("a sublist append 'c':")
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
