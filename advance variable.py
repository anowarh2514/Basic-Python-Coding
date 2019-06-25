Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
1770469696
>>> name = 'anowar'
>>> id(name)
47149632
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
1770469776
>>> id(b)
1770469776
>>> id(10)
1770469776
>>> data = 5
>>> id(data)
1770469696
>>> id(5)
1770469696
>>> k = 10
>>> id(k)
1770469776
>>> a = 9
>>> id(a)
1770469760
>>> id(b)
1770469776
>>> k = a
>>> id(k)
1770469760
>>> b = 8
>>> id(b)
1770469744
>>> id(10)
1770469776
>>> PI = 3.1416
>>> PI
3.1416
>>> PI = 3.15
>>> type(PI)
<class 'float'>
>>> 
