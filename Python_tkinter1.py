#Python tkinter 
#2 tkinter Label & Button
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x100')          #size

var=tk.StringVar()
on_hit= False


#Label
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()                            #l.place()

#Button

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('You hit me')
    else:
        on_hit=False
        var.set('')  

b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
b.pack()

window.mainloop()            
'''

#3.tkinter Entry & Text
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

#Entry
e=tk.Entry(window,show=None)        #show='*'
e.pack()


#Button
def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    #t.insert('end',var)
    t.insert(2.1,var)               #1.1:row.column
    
b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2=tk.Button(window,text='insert end',command=insert_end)
b2.pack()

t=tk.Text(window,height=2)
t.pack()

window.mainloop()            
'''

#4.tkinter Listbox
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

#Label
var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)        #show='*'
l.pack()

#Button
def insert_selection():
    value=lb.get(lb.curselection())
    var1.set(value)   
    
b1=tk.Button(window,text='print selection',width=15,height=2,command=insert_selection)
b1.pack()

#Listbox
var2=tk.StringVar()
var2.set((11,22,33,44))
lb=tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()
'''

#5.tkinter Radiobutton
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

#Label
var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

#Radiobutton
def print_selection():
    l.config(text='you select:'+var.get())
    
r1= tk.Radiobutton(window,text='Option A',
                   variable=var,value='A',
                   command=print_selection)
r1.pack()
r2= tk.Radiobutton(window,text='Option B',
                   variable=var,value='B',
                   command=print_selection)
r2.pack()
r3= tk.Radiobutton(window,text='Option C',
                   variable=var,value='C',
                   command=print_selection)
r3.pack()

window.mainloop()
'''

#6.tkinter Scale
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

#Label
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

#Scale
def print_selection(v):                 #have default value:v
    l.config(text='you select:'+v)
    
s=tk.Scale(window,label='try me',from_=5,to_=11,
           orient=tk.HORIZONTAL,length=200,showvalue=0,             #showvalue=1
           tickinterval=3,resolution=0.01,command=print_selection)
s.pack()

window.mainloop()
'''

#7.tkinter Checkbutton
'''
import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

#Label
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

#Checkbutton
def print_selection():
    if (var1.get()==1) & (var2.get()==0):
        l.config(text='Only Python')
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text='Only C++')
    elif (var1.get()==0) & (var2.get()==0):
        l.config(text='Not either')
    else:
        l.config(text='Love Both')    

var1=tk.IntVar()        #type:int variable type
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                  command=print_selection)
c2=tk.Checkbutton(window,text=' C++  ',variable=var2,onvalue=1,offvalue=0,
                  command=print_selection)
c1.pack()
c2.pack()

window.mainloop()
'''

#8Canvas

import tkinter as tk

window=tk.Tk()                      #TK():object
window.title('my windows')          #name
window.geometry('200x200')          #size

def moveit():
    canvas.move(rect,0,2)
    

canvas=tk.Canvas(window,bg='blue',height=100,width=200)
image_file=tk.PhotoImage(file='C:\DATA\Python\P01.GIF')
image=canvas.create_image(10,10,anchor='nw',image=image_file)
#anchor= r1:NW,N,NE r2:W,CENTER,E r3:SW,S,SE
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=30,extent=150)
rect=canvas.create_rectangle(100,30,100+20,30+20)

canvas.pack()

b=tk.Button(window,text='move',command=moveit).pack()

window.mainloop()



