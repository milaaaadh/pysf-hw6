import tkinter as tk
from MatchGame import *
mg = tk.Tk()


def update_btn_text(value):
    btn_text.set(str(value))


primary_table = MatchGame.creat_primary_table(4,5)
random_table = MatchGame.creat_random_table(1,6,4,5)

mg = tk.Tk()
btn_text = tk.StringVar()

mg.title ( "MatchGame" )
operator = ""
text_input = StringVar( )
r = 1
for i in primary_table :
    c = 1
    for j in i :
        btnname = str ( r ) + str ( c )
        btn_text = tk.StringVar()
        btn_text_value = str(primary_table [ r - 1 ] [ c - 1 ])

        locals ( ) [ btnname ] = tk.Button ( mg , padx=16 , pady=16 , bd=8 , fg='black' ,
                                              font=('arial' , 20 , 'bold') ,
                                              textvariable=btn_text, command=update_btn_text(random_table [ r - 1 ] [ c - 1 ]) ).grid ( row=r , column=c )
        btn_text.set ( btn_text_value )
        c = c + 1
    r = r + 1

mg.mainloop ( )

