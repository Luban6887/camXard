#coded by Luban Mahfuz
#using version of all modules are
#1 mediapipe = 0.9.0.1

import sys
sys.path.append("C:/Users/Luban Mahfuz/Desktop/pyapp")
sys.path.append("C:/Users/Luban Mahfuz/AppData/Local/Programs/Python/Python38/Lib/site-packages/mediapipe")
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import *
import FingerCount as FC

root = Tk()
root.geometry("333x301+310+154")
root.resizable(False, False)
root.title("camXard")
root.iconbitmap('logo.ico')
root.configure(background="#57b7ea")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")

          
Label3 = Label(root)
Label3.place(relx=0.22, rely=0.063, height=46, width=174)
Label3.configure(activebackground="#f9f9f9")
Label3.configure(anchor='w')
Label3.configure(background="#57b7ea")
Label3.configure(compound='left')
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(font="-family {Segoe UI Black} -size 30 -weight bold")
Label3.configure(foreground="#ffffff")
Label3.configure(highlightbackground="#d9d9d9")
Label3.configure(highlightcolor="black")
Label3.configure(text='''camXard''')

Button1 = Button(root)
Button1.place(relx=0.601, rely=0.748, height=44, width=117)
Button1.configure(background="#cff3f5")
Button1.configure(font="-family {Segoe UI} -size 11 -weight bold")
Button1.configure(foreground="#145f63")
Button1.configure(text='''Apply''')

TCombobox0 = Combobox(root,state="readonly")
TCombobox0.place(relx=0.0, rely=0.332, relheight=0.08, relwidth=0.73)
TCombobox0.configure(takefocus="")
TCombobox0['value'] = ["FingerCount"]
TCombobox0.current(0)

TCombobox1 = Combobox(root,state="readonly")
TCombobox1.configure(takefocus="")
TCombobox1.place(relx=0.0, rely=0.432, relheight=0.08, relwidth=0.73)
TCombobox1['value'] = [0, 1, 2, 3, 4, 5]
TCombobox1.current(0)

TCombobox2 = Combobox(root,state="readonly")
TCombobox2.configure(takefocus="")
TCombobox2.configure(cursor="")
TCombobox2.place(relx=0.0, rely=0.532, relheight=0.08, relwidth=0.73)
TCombobox2['value'] = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10"]
TCombobox2.current(3)    

#TCombobox3 = Combobox(root,state="readonly")
#TCombobox3.configure(takefocus="")
#TCombobox3.place(relx=0.0, rely=0.632, relheight=0.08, relwidth=0.73)
#TCombobox3['value'] = [ 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 31250, 38400, 57600, 115200]
#TCombobox3.current(5)

Label0 = Label(root)
Label0.place(relx=0.751, rely=0.332, height=21, width=74)
Label0.configure(anchor='w')
Label0.configure(background="#d9d9d9")
Label0.configure(compound='left')
Label0.configure(disabledforeground="#a3a3a3")
Label0.configure(foreground="#000000")
Label0.configure(text='''MOD''')

Label1 = Label(root)
Label1.place(relx=0.751, rely=0.432, height=21, width=74)
Label1.configure(anchor='w')
Label1.configure(background="#d9d9d9")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(text='''Camera''')

Label2 = Label(root)
Label2.place(relx=0.751, rely=0.532, height=21, width=74)
Label2.configure(anchor='w')
Label2.configure(background="#d9d9d9")
Label2.configure(compound='left')
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(foreground="#000000")
Label2.configure(text='''PORT''')

#Label3 = Label(root)
#Label3.place(relx=0.751, rely=0.632, height=21, width=74)
#Label3.configure(anchor='w')
#Label3.configure(background="#d9d9d9")
#Label3.configure(compound='left')
#Label3.configure(disabledforeground="#a3a3a3")
#Label3.configure(foreground="#000000")
#Label3.configure(text='''Baud Rate''')



Label6 = Label(root)
Label6.place(relx=0.03, rely=0.93, height=21, width=114)
Label6.configure(anchor='w')
Label6.configure(background="#57b7ea")
Label6.configure(compound='left')
Label6.configure(cursor="fleur")
Label6.configure(disabledforeground="#a3a3a3")
Label6.configure(font="-family {Txt_IV50} -size 9")
Label6.configure(foreground="#000000")
Label6.configure(text='''Luban Mahfuz''')

def KeyP():
    Buton1()
def Buton1():
    Cam = TCombobox1.get()
    port = TCombobox2.get()
    Cam = int(Cam)
    FC.Fcnt(Cam,port)

root.bind('<Return>', KeyP)
Button1.configure(command=Buton1)  

root.mainloop()
