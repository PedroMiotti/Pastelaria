#Importing modules===========================================================
from tkinter import *
import sqlite3
from tkinter import messagebox

#connecting to the DB===========================================================
conn = sqlite3.connect("Login.db")
c = conn.cursor()

#Creating the Login Window===========================================================
login_root = Tk()
login_root.geometry("400x200+600+300")
login_root.title("Di Pastel Login")
login_root.resizable(False, False)

#Creating the widgets=================================================================
title_frame = Frame(login_root, width = 900 , height = 40,background = "gold2")
title_frame.place(x= 0, y=0)

#Labels__________________
title_label = Label(login_root, text = "Login", font = ('courier new', 20), foreground = "black", bg = "gold2")
title_label.place(x= 170, y=1)

cod_label = Label(login_root, text = "Cód :",font = ('courier new', 18))
cod_label.place(x = 40, y = 40)

psw_label = Label(login_root, text = "Senha :",font = ('courier new', 18))
psw_label.place(x = 40, y = 110)

#StringVars___________________
cod_str = StringVar()
psw_str = StringVar()

#Entrys___________________
cod_entry = Entry(login_root, font = ('courier new', 13) ,insertwidth = 4, relief = 'flat', textvariable = cod_str )
cod_entry.place(x = 60, y = 80)

psw_entry = Entry(login_root, font = ('courier new', 13) ,insertwidth = 4, relief = 'flat', show = '*' , textvariable = psw_str)
psw_entry.place(x = 60, y = 150)

#Funçao para verificar se o codigo e a senha estão corretos
def log():
    find_user = ("SELECT * FROM login WHERE cod = ? AND senha = ?")
    c.execute(find_user,[(cod_str.get()) , (psw_str.get())])
    resultado = c.fetchall()
    #Se o codigo e a senha estao corretos abra o sistema
    if resultado:
        login_root.destroy()
        import DiPastel
    #Se não mostre essa mensagem
    else:
        messagebox.showerror('Di Pastel', "Usuário não encontrado " , parent= entrar_btt)

#Button____________________
entrar_btt = Button(login_root , text = "Entrar", font = ('arial', 13), bg = "gold2" ,fg = "black", command = log)
entrar_btt.place(x = 290 , y = 150)



login_root.mainloop()
