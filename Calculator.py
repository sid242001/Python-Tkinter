from tkinter import *
root=Tk()
root.title("©alculator by Siddhesh™")
root.geometry("240x300+600+300")
def click(event):
    global exp
    val=event.widget.cget("text")
    if val== "=":
        e=eval(exp.get())
        exp.set(e)
    elif val=="C":
        ent.delete(0,END)
    elif val=="<":
        ent.delete(len(ent.get())-1,END)
    else:
        ent.insert(END,val)
exp=StringVar()
ent=Entry(root,textvariable=exp,font="Ariel 25 bold")
ent.pack(fill=X)
butt=[["7","8","9","+"],["4","5","6","-"],["1","2","3","*"],["=","<","C","/"]]
fr=["f1","f2","f3","f4"]
for i,k in zip(butt,fr):
    k=Frame(root)
    k.pack(fill=X)
    for j in i:
        b=Button(k,text=f"{j}",padx=20,pady=20)
        b.pack(side="left")
        b.bind("<Button-1>",click)
root.mainloop()
