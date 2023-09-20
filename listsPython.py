Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mithai = ['halva','kheer','jalebi','gulabjamun']
>>> mithai
['halva', 'kheer', 'jalebi', 'gulabjamun']
>>> type(mithai)
<class 'list'>
>>> mithai[0]
'halva'
>>> mithai[1]
'kheer'
>>> mithai[-1]
'gulabjamun'
>>> mithai[1:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> mithai[1:3]
['kheer', 'jalebi']
>>> mithai[:2]
['halva', 'kheer']
>>> mithai[:]
['halva', 'kheer', 'jalebi', 'gulabjamun']
>>> mithai[-3:]
['kheer', 'jalebi', 'gulabjamun']
>>> len(mithai)
4
>>> 'samosa' in mithai
False
>>> 'samosa' not in mithai
True
>>> 'halva' in mithai
True
>>> mithai.append['laddu']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    mithai.append['laddu']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> mithai.append["laddu"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    mithai.append["laddu"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> mithai.append('laddu')
>>> mithai
['halva', 'kheer', 'jalebi', 'gulabjamun', 'laddu']
>>> mithai.insert(2,'khulfi')
>>> mithai
['halva', 'kheer', 'khulfi', 'jalebi', 'gulabjamun', 'laddu']
>>> tikha = ['samosa','sev']
>>> food = mithai+ tikha
>>> food
['halva', 'kheer', 'khulfi', 'jalebi', 'gulabjamun', 'laddu', 'samosa', 'sev']
>>> mithai[0] = 'peda'
>>> mithai
['peda', 'kheer', 'khulfi', 'jalebi', 'gulabjamun', 'laddu']
>>> mithai[0:2]
['peda', 'kheer']
>>> mithai[0:2]='samosa'
>>> mithai
['s', 'a', 'm', 'o', 's', 'a', 'khulfi', 'jalebi', 'gulabjamun', 'laddu']
>>> mithai[0:6] = ['samosa']
>>> mithai
['samosa', 'khulfi', 'jalebi', 'gulabjamun', 'laddu']
>>> dir(mithai)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> mithai.reverse()
>>> mithai
['laddu', 'gulabjamun', 'jalebi', 'khulfi', 'samosa']
>>> 