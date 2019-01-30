Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,3,4,5,6][1,2,3]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    [1,2,3,4,5,6][1,2,3]
TypeError: list indices must be integers or slices, not tuple
>>> [1,2,3,4,5,6]*3
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> [1,2,3,4,5,6]*3+[1,2,3]
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3]
>>> [1,2,3,4,5,6]*3+[1,2,3]+[1,2,3,4,5,6]
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4, 5, 6]
>>> A=[1,2,3,4,5,6] B=[1,2,3] A*3+B+A
SyntaxError: invalid syntax
>>> A=[1,2,3,4,5,6]
>>> B=[1,2,3]
>>> A*3+B+A
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4, 5, 6]
>>> skill = ["新月打击","苍白之瀑"]
>>> action = ["引燃","闪现"]
>>> skill+action
['新月打击', '苍白之瀑', '引燃', '闪现']
>>> a1=[1,2,3]
>>> a_=[1,2,3,4]
>>> b_1="123"
>>> c1={1,2}
>>> d_=(2,3)
>>> a1+a_+b_1+c1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a1+a_+b_1+c1
TypeError: can only concatenate list (not "str") to list
>>> a=1
>>> b=a
>>> a=3
>>> b
1
>>> a=[1,2,3,4,5]
>>> b=a
>>> a[0]="1"
>>> print(a)
['1', 2, 3, 4, 5]
>>> b
['1', 2, 3, 4, 5]
>>> a
['1', 2, 3, 4, 5]
>>> 
>>> a=[1,2,3]
>>> b=a
>>> a[0]="5"
>>> a
['5', 2, 3]
>>> b
['5', 2, 3]
>>> a=[1,2,3]
>>> b=a
>>> a=[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3]
>>> 
>>> type = 1
>>> print(type)
1
>>> type(type)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    type(type)
TypeError: 'int' object is not callable
>>> type(type=1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    type(type=1)
TypeError: 'int' object is not callable
>>> a="hello
"
SyntaxError: EOL while scanning string literal
>>> a="hello"
>>> a=a+"python"
>>> a
'hellopython'
>>> id(a)
44276216
>>> b="hello"
>>> b=b+"python"
>>> b
'hellopython'
>>> id(d)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    id(d)
NameError: name 'd' is not defined
>>> id(b)
32793528
>>> "hello"[0]
'h'
>>> b="hello"
>>> id(b)
44174880
>>> b=b+"python"
>>> b
'hellopython'
>>> id(b)
44169920
>>> a=(1,2,3,[1,2,4])
>>> a[3[2]]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a[3[2]]
TypeError: 'int' object is not subscriptable
>>> a[3]
[1, 2, 4]
>>> 
KeyboardInterrupt
>>> a[3][2]
4
>>> a=(1,2,3,[1,2["a","b","c"]])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a=(1,2,3,[1,2["a","b","c"]])
TypeError: 'int' object is not subscriptable
>>> 
>>> a[1]
2
>>> a[3]
[1, 2, 4]
>>> a=(1,2,3,[1,2["a","b","c"]])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a=(1,2,3,[1,2["a","b","c"]])
TypeError: 'int' object is not subscriptable
>>> a = (1,2,3,[1,2["a","b","c"]])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a = (1,2,3,[1,2["a","b","c"]])
TypeError: 'int' object is not subscriptable
>>> b=(1,2,3,[1,2["a","b","c"]])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b=(1,2,3,[1,2["a","b","c"]])
TypeError: 'int' object is not subscriptable
>>> a=(1,2,3,[1,2,4])
>>> a[3][2]="4"
>>> a
(1, 2, 3, [1, 2, '4'])
>>> a=(1,2,3,[1,2[3,4,5]])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=(1,2,3,[1,2[3,4,5]])
TypeError: 'int' object is not subscriptable
>>> a=(1,2,3,[4,5,[3,4,5]])
>>> a = (1,2,3,[1,2,["a","b","c"]])
>>> a[3][2][1]
'b'
>>> 3-1
2
>>> 3/2
1.5
>>> 3//2
1
>>> 5%2
1
>>> b+=a
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    b+=a
TypeError: can only concatenate str (not "tuple") to str
>>> a=1
>>> b=2
>>> b+=a
>>> print(b)
3
>>> b
3
>>> a
1
>>> 
bool(1)
True
>>> bool(.)
SyntaxError: invalid syntax
>>> 
