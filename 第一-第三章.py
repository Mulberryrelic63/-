Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello,world')
hello,world
>>> print("hello,world")
hello,world
>>> type(*1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(*1)
TypeError: type object argument after * must be an iterable, not int
>>> type(1.2)
<class 'float'>
>>> type(1.1211212121212121211)
<class 'float'>
>>> type(-1)
<class 'int'>
>>> 1+0.1
1.1
>>> 
KeyboardInterrupt
>>> type(1+0.1)
<class 'float'>
>>> clear
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> type(1/1.0)
<class 'float'>
>>> type(2//2)
<class 'int'>
>>> type(1//2)
<class 'int'>
>>> 0b10
2
>>> 0b01
1
>>> 0b11
3
>>> 0b110
6
>>> 0b111
7
>>> bin(50)
'0b110010'
>>> int(8)
8
>>> int(0xf)
15
>>> oct(10)
'0o12'
>>> hex(0xf)
'0xf'
>>> hex(0b1111)
'0xf'
>>> true
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> False
False
>>> type
<class 'type'>
>>> type(bool)
<class 'type'>
>>> type(True)
<class 'bool'>
>>> int(True)
1
>>> int(False)
0
>>> bool(1)
True
>>> bool(0)
False
>>> bool(0.1)
True
>>> bool(-1)
True
>>> bool(*)
SyntaxError: invalid syntax
>>> bool(\)
	
SyntaxError: unexpected character after line continuation character
>>> bool(!)
SyntaxError: invalid syntax
>>> bool(0)
False
>>> bool(0b0)
False
>>> bool(abc)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    bool(abc)
NameError: name 'abc' is not defined
>>> bool("abc")
True
>>> bool(")
	 
SyntaxError: EOL while scanning string literal
>>> bool("")
	 
False
>>> bool([])
	 
False
>>> bool({})
	 
False
>>> 36j
	 
36j
>>> "hello world"
	 
'hello world'
>>> type("1\")
	 
SyntaxError: EOL while scanning string literal
>>> type("1")
	 
<class 'str'>
>>> """
hello world
justing bieber
"""
	 
'\nhello world\njusting bieber\n'
>>> '''just do
it
dodododo'''
	 
'just do\nit\ndodododo'
>>> 'hello world \nhello world'
	 
'hello world \nhello world'
>>> print("\na\nb\nc")
	 

a
b
c
>>> "hello\
world"
	 
'helloworld'
>>> print("hello '\n'world
	  ")
	  
SyntaxError: EOL while scanning string literal
>>> print("hello world")
	  
hello world
>>> print("hello \ n world")
	  
hello \ n world
>>> print("""hello "\n" world""")
	  
hello "
" world
>>> print("helllo \\n world")
	  
helllo \n world
>>> print("c:\$360Section\360.3948C8AEB4308220A35F626A2D721399.q3q")
	  
c:\$360Sectionð.3948C8AEB4308220A35F626A2D721399.q3q
>>> print(r"D:\360安全浏览器下载\LOL_V4.1.2.2_FULL_0_tgod_signed.exe)
	  
SyntaxError: EOL while scanning string literal
>>> print(r"D:\360安全浏览器下载\LOL_V4.1.2.2_FULL_0_tgod_signed.exe")
	  
D:\360安全浏览器下载\LOL_V4.1.2.2_FULL_0_tgod_signed.exe
>>> "hello"+"world"
	  
'helloworld'
>>> "hello"-"e"
	  
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    "hello"-"e"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> hello + world
	  
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    hello + world
NameError: name 'hello' is not defined
>>> "hello"*3
	  
'hellohellohello'
>>> "hello"[0]
	  
'h'
>>> "hello"[5]
	  
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    "hello"[5]
IndexError: string index out of range
>>> "hello"[2]
	  
'l'
>>> "hello"[4]
	  
'o'
>>> "hello"[0]
	  
'h'
>>> "hello world"[6]
	  
'w'
>>> "hello world"[-5]
	  
'w'
>>> "hello world"[0:5
		  ]
	  
'hello'
>>> "hello world"[0:0]
	  
''
>>> w
	  
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> "hello world"[6:11]
	  
'world'
>>> "hello world"[-6:-1]
	  
' worl'
>>> "hello world"[-6:0]
	  
''
>>> "hello world"[-6:11]
	  
' world'
>>> "hello world"[6:]
	  
'world'
>>>"hello"
          
