Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> food = 'samosa'
>>> food
'samosa'
>>> food[0]
's'
>>> fod[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fod[5]
NameError: name 'fod' is not defined
>>> food[5]
'a'
>>> food[-1]
'a'
>>> food[-1]
'a'
>>> food[-2]
's'
>>> food[0:2]
'sa'
>>> food[:2]
'sa'
>>> food[-3:]
'osa'
>>> len(food)
6
>>> myfood = 'samosa,jalebi'
>>> 'jalebi' in my food
SyntaxError: invalid syntax
>>> 'jalebi' in myfood
True
>>> 'biryani' in myfood
False
>>> 'biryani' not in myfood
True
>>> food
'samosa'
>>> food="samosa"
>>> food ='samosa'
>>> myfood.replace('samosa' , 'biryani')
'biryani,jalebi'
>>> myfood
'samosa,jalebi'
>>> myfood = myfood.replace('samosa' , 'biryani')
>>> myfood
'biryani,jalebi'
>>> dir(myfood)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> myfood.upper()
'BIRYANI,JALEBI'
>>> 'ABC'.lower()
'abc'
>>> s='420'
>>> s.isdigit
<built-in method isdigit of str object at 0x000001BF5F2830F0>
>>> s.isdigit = true
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.isdigit = true
NameError: name 'true' is not defined
>>> s.isdigit
<built-in method isdigit of str object at 0x000001BF5F2830F0>
>>> s='420chor'
>>> s.isdigit
<built-in method isdigit of str object at 0x000001BF5F274AB0>
>>> myfood
'biryani,jalebi'
>>> myfood.index('jalebi')
8
>>> states = 29
>>> text = 'states in india:'
>>> text+str(states)
'states in india:29'
>>> s="let's learn python "
>>> 
>>> 
>>> 
>>> 
>>> dialog = '''kitne aadmi the ?
kalia : sardar do '''
>>> dialog
'kitne aadmi the ?\nkalia : sardar do '
>>> print(dialog)
kitne aadmi the ?
kalia : sardar do 
>>> 
>>> 
>>> s = 'hey\tbro'
>>> s
'hey\tbro'
>>> print(s)
hey	bro
>>> s = 'hey\nbro'
>>> print(s)
hey
bro
>>> first = 'Sachin'
>>> last = 'tendulkar'
>>> print('best cricket player :' first+ ''+last)
SyntaxError: invalid syntax
>>> print('best cricket player :' ,first+ ''+last)
best cricket player : Sachintendulkar
>>> print(f'best cricket player : {first} {last})
      
SyntaxError: EOL while scanning string literal
>>> print(f'best cricket player : {first} {last}')
best cricket player : Sachin tendulkar
>>> 