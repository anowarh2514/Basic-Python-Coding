Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = 2.4
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+8i
SyntaxError: invalid syntax
>>> num = 6+8j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float b
SyntaxError: invalid syntax
>>> k = float(b)
>>> k
5.0
>>> k = 6
>>> c = complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool = b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> lst[25,35,33,45]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lst[25,35,33,45]
NameError: name 'lst' is not defined
>>> lst = [25,35,33,45]
>>> lst
[25, 35, 33, 45]
>>> type(lst)
<class 'list'>
>>> s = {22,33,44,55}
>>> type(s)
<class 'set'>
>>> t = (22,34,55,66)
>>> type(t)
<class 'tuple'>
>>> str = "anowar"
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,20))
[2]
>>> list(range(2,22,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> d = {'anowar':'samsung','monia':'lenevo','saif':'vivo'}
>>> d
{'anowar': 'samsung', 'monia': 'lenevo', 'saif': 'vivo'}
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys()
dict_keys(['anowar', 'monia', 'saif'])
>>> d.values()
dict_values(['samsung', 'lenevo', 'vivo'])
>>> d['anowar']
'samsung'
>>> d.get('monia')
'lenevo'
>>> 
