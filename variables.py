Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = input('something:')
something:'10'
>>> x
"'10'"
>>> something:10
>>> x
"'10'"
>>> x= input('something:')
something:10
>>> x
'10'
>>> x = input(someting)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = input(someting)
NameError: name 'someting' is not defined
>>> x = input("something:")
something:10
>>> x
'10'
>>> x = raw_input("something:")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x = raw_input("something:")
NameError: name 'raw_input' is not defined
>>> raise IOError, "file error" #This is accepted in Python 2
SyntaxError: invalid syntax
>>> raise IOError("file error") #This is accepted in Python 3
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    raise IOError("file error") #This is accepted in Python 3
OSError: file error
>>> raise IOError("file error")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    raise IOError("file error")
OSError: file error
>>> except Myerror as err: #In Python 3
	
SyntaxError: invalid syntax
>>> except Myerror, err: # In Python2
	
SyntaxError: invalid syntax
>>> abc
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x = 9
>>> x+10
19
>>> _ + x
28
>>>  name = 'youtube'
SyntaxError: unexpected indent
>>> name='youtube'
>>> name
'youtube'
>>> name + 'rock'
'youtuberock'
>>> name + ' best'
'youtube best'
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-3]
'u'
>>> name[-1:-2:-3:-4:-5:-6]
SyntaxError: invalid syntax
>>> name[-1:]
'e'
>>> name[:-1]
'youtub'
>>> name[:-0]
''
>>> name[:-1:6]
'y'
>>> name[6:-1]
''
>>> name[:-6]
'y'
>>> name[:-1]
'youtub'
>>> name[:1]
'y'
>>> 'my '+name[3:]
'my tube'
>>> myname = 'Md Anowar Hossain'
>>> len(myname)
17
>>> 
