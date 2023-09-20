Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  1 2023, 18:18:15) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
heros=['spider man','thor','hulk','iron man','captain america']
length(heros)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    length(heros)
NameError: name 'length' is not defined
len(heros)
5
heros.append("black panther")
heros
['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']
heros.remove("black panther")
heros
['spider man', 'thor', 'hulk', 'iron man', 'captain america']
heros.insert(3,'black panther')
heros
['spider man', 'thor', 'hulk', 'black panther', 'iron man', 'captain america']
heros.remove("thor","hulk").insert(1,"doctor strange")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    heros.remove("thor","hulk").insert(1,"doctor strange")
TypeError: list.remove() takes exactly one argument (2 given)
heros.remove("thor,hulk").insert(1,"doctor strange")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    heros.remove("thor,hulk").insert(1,"doctor strange")
ValueError: list.remove(x): x not in list
heros[1:3] = "doctor strange"
print(heros)
['spider man', 'd', 'o', 'c', 't', 'o', 'r', ' ', 's', 't', 'r', 'a', 'n', 'g', 'e', 'black panther', 'iron man', 'captain america']
heros[1:3] = ['doctor strange']
print(heros)
['spider man', 'doctor strange', 'c', 't', 'o', 'r', ' ', 's', 't', 'r', 'a', 'n', 'g', 'e', 'black panther', 'iron man', 'captain america']
heros
['spider man', 'doctor strange', 'c', 't', 'o', 'r', ' ', 's', 't', 'r', 'a', 'n', 'g', 'e', 'black panther', 'iron man', 'captain america']
heros.remove('doctor strange')
heros
['spider man', 'c', 't', 'o', 'r', ' ', 's', 't', 'r', 'a', 'n', 'g', 'e', 'black panther', 'iron man', 'captain america']
heros.sort
<built-in method sort of list object at 0x000001FA4A2AF540>
heros.sort()
heros
[' ', 'a', 'black panther', 'c', 'captain america', 'e', 'g', 'iron man', 'n', 'o', 'r', 'r', 's', 'spider man', 't', 't']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> exp = (2200,2350,2600,2130,2190)
>>> exp = (2200,2350,2600,2130,2190)
>>> exp = (2200,2350,2600,2130,2190)
>>> exp = [2200,2350,2600,2130,2190]
>>> print("In feb this much extra was spent compared to jan:",exp[1]-exp[0])
In feb this much extra was spent compared to jan: 150
>>> print("Expense for first quarter:",exp[0]+exp[1]+exp[2])
Expense for first quarter: 7150
>>> print("Did I spent 2000$ in any month? ", 2000 in exp)
Did I spent 2000$ in any month?  False
>>> exp.append(1980)
... print("Expenses at the end of June:",exp)
SyntaxError: multiple statements found while compiling a single statement
>>> exp/append(1980)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    exp/append(1980)
NameError: name 'append' is not defined
>>> exp.append(1980)
>>> print("Expenses at the end of June : ", exp)
Expenses at the end of June :  [2200, 2350, 2600, 2130, 2190, 1980]
>>> exp[3] = exp[3] - 200
>>> print("Expenses after 200$ return in April:",exp)
Expenses after 200$ return in April: [2200, 2350, 2600, 1930, 2190, 1980]
