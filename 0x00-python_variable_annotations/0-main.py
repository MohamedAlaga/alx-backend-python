#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

#{'a': <class 'float'>, 'b': <class 'float'>}
#{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}