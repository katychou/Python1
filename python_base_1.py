"""list1=[1,2,3,4,5,6,7,8,10]
#print(
a=1
for i in list1:
      
      print(i)
      print('out of'+ str(i))
     
print ("end1")

for i in range (1,7,2):
      print(float(i))  """
      
"""while a<10:
      print(a)
      a=a+1
      
'''print(a,c,b) """

#===================================================
#python基础 14 模块安装  numpy sourceforge.net
#https://sourceforge.net/projects/numpy/files/
# $sudo pip3 install numpy
# $sudo pip3 install numpy-1.9.2
# $sudo pip3 install -U numpy       //upgrade
# $sudo pip3 uninstall numpy


#python BASIC 15 file1
'''
text='This is my first test.\nThis is 2 line.\nThis is 3 line.'
print(text)

file1=open('myfile1.txt','w')
file1.write(text)
file1.close()
'''

#python BASIC 16 file2
"""
appendtext='\nThis is append line.'
file1=open('myfile1.txt','a')  #append
file1.write(appendtext)
file1.close()
"""

#python BASIC 17 file3
"""
file1=open('myfile1.txt','r')
#content=file1.read()
#print(content)
content=file1.readlines()
#list1=[1,2,3,4,5,'aaa','bbb']
print(content)
"""

#python BASIC 18 class
"""
class Calculator:
      name ='Good cal'
      price=20
      
      def add(self,x,y):
            print(self.name)
            result=x+y
            print(result)
      def minus(self,x,y):
            result=x-y
            print(result)
      def times(self,x,y):
            print(x*y)
      def divide(self,x,y):
            print(x/y)


calcul = Calculator()
calcul.add(10,20)
"""

#python BASIC 19 class init
"""
class Calculator:
      name ='Good cal'
      price=20
      def __init__(self,name,price=30,hight=31,width=32,weight=33):
            self.name=name
            self.price=price
            self.h=hight
            self.wi=width
            self.we=weight
            self.add(10,20)
      
      def add(self,x,y):
            print(self.name)
            result=x+y
            print(result)
      def minus(self,x,y):
            result=x-y
            print(result)
      def times(self,x,y):
            print(x*y)
      def divide(self,x,y):
            print(x/y)

c = Calculator('Bad cal',21,22,weight=23)
print(c.name,c.wi,c.we)
"""

#python BASIC 20 input
"""
a_input=input("Please give a number:")
#a_input=int(input("Please give a number:"))
if a_input=='1':
      print("This input number is:",a_input)
elif a_input==str(2):
      print("see you next time")
else:
      print("Goodbye")
"""


#python BASIC 21 tupieList
'''
a_tuple=(1,2,3,5,16,20)
b_tuple=3,4,6,7,9

a_list=[12,3,45,9]

for content in a_tuple:
      print(content)

for index in range(len(a_list)):
      print('index=',index,'number in list=',a_list[index])
'''

#python BASIC 22 List
'''
a=[1,2,3,4,2,3,1,1]
a.append(0)
a.insert(1,9)
a.remove(3)
print(a)
print(a[0] , a[-2], a[3:5])
print(a[:3])
print(a.index(4))
print(a.count(2))
a.sort(reverse=True)
print(a)
'''

#python BASIC 23 List
#numpy pandas
'''
a=[1,2,3,4,5]
multi_a=[[1,2,3],
         [2,3,4],
         [3,4,5]]
print(a[2])
print(multi_a[2][2])
'''

#python BASIC 24 dictionary
'''
a_list=[1,2,3,9,10]
d={'apple':1,'pear':2,'orange':3}

e={'book':[1,2,3],'pool':{1:4,4:'a'},'name':2}
d2={1:'a','c':'b'}
print(d['apple'])
print(a_list[0])

del d['pear']
print(d)
d['b']=20
print(d)
print(e)
print(e['pool'][4])
'''

#python BASIC 25 import
#import time
#import time as t
#print(t.localtime())
'''
from time import time,localtime
from time import *

print(localtime())
print(time())
'''

#python BASIC 26 self_class
'''
import m1
m1.printdata('I am python1')
# \Library\Frameworks\Python.framework\Versions\3.5\site-packages\m1.py
'''
#python BASIC 27 continue & break
'''way1
a=True
while a:
      b=input('type something')
      if b=='1':
            a=False

      else:
            pass
print('finish run')
#end way1 '''
'''way2
while True:
      b=input('type something')
      if b=='1':
            continue  #break
      else:
            pass
      print('still in while')
print('finish run')
#end way2
'''

#python BASIC 28 try--error
'''
try:
      file1=open('ddd.txt','r+')
except Exception as e:
      print('There is no file named as ddd.txt')
      response= input('Do you want to create a new file')
      if response=='y':
            file1=open('ddd.txt','w')
            print('Create a new file:eee')
      else:
            pass
else:
      file1.write('sss')
      file1.close()
finally:
      file1.close()
      print ('try End')      
'''   
      
#python BASIC 29 zip lambda map
'''
a=[1,2,3]
b=[4,5,6]
#print(zip(a,b))
print(list(zip(a,b)))
print(list(zip(a,a,b)))
for i,j in zip(a,b):
      print(i/2,j*2)      
#=========================
def fun1(x,y):
      return (x+y)
print(fun1(2,3))
#========================
fun2 = lambda x,y:x+y
print(fun2(2,3))
#========================
print(map(fun1,[1],[2]))
print(list(map(fun1,[1,3],[2,5])))
'''

#python BASIC 30 copy & deepcopy
'''
import copy
a=[1,2,3]
b=a                    #copy
print(id(a),id(b))
print(a)
a[1]=22
print(b)
print(id(a)==id(b))
c=copy.copy(a)         #shallow copy
print(id(a)==id(c))
c[1]=2222
print(a)
print(c)

a=[1,2,[3,4]]
d=copy.copy(a)
print(id(a)==id(d))
print(id(a[2])==id(d[2]))
a[2][0]=333             #copy.copy
print(d)

e=copy.deepcopy(a)      #deepcopy
print(id(e[2])==id(a[2]))
'''   

#python BASIC 31 threading
#python BASIC 32 multiprocessing
#python BASIC 33 tkinter

#python BASIC 34 pickle
#import pickle
#a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}
'''
file=open('pickle_example.pickle','wb')  #wb:write_binary
pickle.dump(a_dict,file)      #a_dict tmep save to file
file.close()
'''
#way1
'''
file=open('pickle_example.pickle','rb')  #wb:read_binary
a_dict1=pickle.load(file)  #file save to a_dict1
file.close()
'''
#way2 file_auto_close
'''
with open('pickle_example.pickle','rb') as file:
      a_dict1=pickle.load(file)
'''
#print(a_dict1)


#python BASIC 35 set
char_list=['a','b','c','c','d','d']
sentence='Welcome Back to this Turorial'
print(type(set(char_list)))
print(type({1:[2,3]}))
print(set(sentence))
unique_char=set(char_list)
unique_char.add('x')
#unique_char.clear()
#print(unique_char)
print(unique_char.remove('x'))
print(unique_char.discard('c'))  #remove,if none then not show error message
print(unique_char)

char_list=['a','b','c','c','d','d']
unique_char=set(char_list)
unique_char.add('x')
set1=unique_char
set2={'a','e','i'}
print(set1.difference(set2))
print(set1.intersection(set2))


#==========================================
