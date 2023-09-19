Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  1 2023, 18:18:15) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
street = rewa
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    street = rewa
NameError: name 'rewa' is not defined
street = rewa
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    street = rewa
NameError: name 'rewa' is not defined
street "rewa "
SyntaxError: invalid syntax
street = "rewa"
city = "Rewa"
Country = "India"
adress = street +'\n'+ city +'\n'+ Country
print("Address using + operatot " , adress)
Address using + operatot  rewa
Rewa
India
adress = f'{street}\n{city}\n{country}'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    adress = f'{street}\n{city}\n{country}'
NameError: name 'country' is not defined. Did you mean: 'Country'?
adress = f'{street}\n{city}\n{Country}'
print("Addres using f string", adress)
Addres using f string rewa
Rewa
India
# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

s = "Earth revolves around the sun"
print(s[6:14])
revolves
print([sun[-3:])
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(s[-3:])
      
sun
>>> 
>>> 
>>> 
>>> # 3. Create two variables to store how many fruits and vegetables you eat in a day.
... # Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
... # Use python f string for this.
...       
>>> fruits = 13
...       
>>> num_fruits = 12
...       
>>> num_vegetables = 12
...       
>>> print(f'I eat {num_vegetables } veggies and {num_fruits} fruits daily')
...       
I eat 12 veggies and 12 fruits daily
>>> 
>>> # 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
... # wrong statement, the correct statement is 'maine 10 samosa khaye'.
... # Replace incorrect words in original strong with new ones and print the new string.
... # Also try to do this in one line.
...       
>>> s = "maine 200 banana khaye"
...       
>>> s = s.replace("banana","samosa")
...       
>>> s
...       
'maine 200 samosa khaye'
>>> s= s.replace("200","10")
...       
>>> s
...       
'maine 10 samosa khaye'
>>> print("using two line replaces ", s)
...       
using two line replaces  maine 10 samosa khaye
>>> s=s.replace('banana','samosa').replace('200','10')
... print("Using single line:",s)
...       
SyntaxError: multiple statements found while compiling a single statement
