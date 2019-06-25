Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nums = [25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[0]
25
>>> nums[4]
14
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names = ['anowar','monia','ayan']
>>> names
['anowar', 'monia', 'ayan']
>>> values = [9.5,'monia',25]
>>> values
[9.5, 'monia', 25]
>>> mil = [nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['anowar', 'monia', 'ayan']]
>>> nums.
SyntaxError: invalid syntax
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(12)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    nums.pop(12)
IndexError: pop index out of range
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 
