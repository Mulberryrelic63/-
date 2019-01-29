Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> {1,2,2,3,3}
{1, 2, 3}
>>> 1 in {1,2,3}
True
>>> 2 not in {3,4,5}
True
>>> {1,2,3,4,5} - {5,6}
{1, 2, 3, 4}
>>> {1,2,3,4,5} & {6,7}
set()
>>> {1,2,3,4,5} & {1,4}
{1, 4}
>>> {1,2,3,4,5} | {6,7}
{1, 2, 3, 4, 5, 6, 7}
>>> type ({})
<class 'dict'>
>>> type (set())
<class 'set'>
>>> len(set()）
	
SyntaxError: invalid character in identifier
>>> len(set()）
	
SyntaxError: invalid character in identifier
>>> len（set()）
	
SyntaxError: invalid character in identifier
>>> len(set())
	
0
>>> ["q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"]
	
SyntaxError: invalid syntax
>>>  ["q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"]
	
SyntaxError: unexpected indent
>>> ["q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"]
	
SyntaxError: invalid syntax
>>> ["q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"]
	
SyntaxError: invalid syntax
>>> {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}
	
{'q': '新月打击', 'w': '苍白之瀑', 'e': '月之降临', 'r': '月神冲刺'}
>>> {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}[q]
	
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}[q]
NameError: name 'q' is not defined
>>> {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}["q"]
	
'新月打击'
>>> {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}["q","w"]
	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}["q","w"]
KeyError: ('q', 'w')
>>> {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}["q""w"]
	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    {"q":"新月打击","w":"苍白之瀑","e":"月之降临","r":"月神冲刺"}["q""w"]
KeyError: 'qw'
>>> 
