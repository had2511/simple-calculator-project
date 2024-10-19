from tkinter import *

window=Tk()
window.title("caculator")
window.geometry("400x500+100+200")
window.configure(bg='black')

equation =""
def show(value):
    global equation
    equation+=value
    label.config(text=equation)
    
def clear():
    global equation
    equation =""
    label.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label.config(text=result)

label=Label(window,width=25,height=2,text="",font=('times newroman',30))
label.pack()

Button(window,text="C", width=4,height=1, font=('times newroman',20), bg="red", command=lambda: clear()).place(x=10,y=100)
Button(window,text="/", width=4,height=1, font=('times newroman',20),command=lambda: show("/")).place(x=100,y=100)
Button(window,text="%", width=4,height=1, font=('times newroman',20),command=lambda: show("%")).place(x=200,y=100)
Button(window,text="*", width=4,height=1, font=('times newroman',20),command=lambda: show("*")).place(x=300,y=100)

Button(window,text="7", width=4,height=1, font=('times newroman',20),command=lambda: show("7")).place(x=10,y=175)
Button(window,text="8", width=4,height=1, font=('times newroman',20),command=lambda: show("8")).place(x=100,y=175)
Button(window,text="9", width=4,height=1, font=('times newroman',20),command=lambda: show("9")).place(x=200,y=175)
Button(window,text="-", width=4,height=1, font=('times newroman',20),command=lambda: show("-")).place(x=300,y=175)

Button(window,text="4", width=4,height=1, font=('times newroman',20),command=lambda: show("4")).place(x=10,y=250)
Button(window,text="5", width=4,height=1, font=('times newroman',20),command=lambda: show("5")).place(x=100,y=250)
Button(window,text="6", width=4,height=1, font=('times newroman',20),command=lambda: show("6")).place(x=200,y=250)
Button(window,text="+", width=4,height=1, font=('times newroman',20),command=lambda: show("+")).place(x=300,y=250)

Button(window,text="1", width=4,height=1, font=('times newroman',20),command=lambda: show("1")).place(x=10,y=325)
Button(window,text="2", width=4,height=1, font=('times newroman',20),command=lambda: show("2")).place(x=100,y=325)
Button(window,text="3", width=4,height=1, font=('times newroman',20),command=lambda: show("3")).place(x=200,y=325)
Button(window,text="0", width=9,height=1, font=('times newroman',20),command=lambda: show("0")).place(x=10,y=400)
Button(window,text=".", width=4,height=1, font=('times newroman',20),command=lambda: show(".")).place(x=200,y=400)
Button(window,text="=", width=4,height=3, font=('times newroman',20),bg="royal blue",command=lambda: calculate()).place(x=300,y=325)



window.mainloop()
