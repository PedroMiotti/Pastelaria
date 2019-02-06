#Status:
#Building the fech window
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import time

#Janela========================
root = Tk()
root.title("Di pastel")
root.geometry('950x757+50+150')
root.resizable(False, False)


#Database=======================
conn = sqlite3.connect('dipastel.db')
c = conn.cursor()

#photoimage====================
image = PhotoImage(file = 'C:\\Users\Dinopc\Desktop\DiPastel\logotipo-Tio-Di.gif')
image= image.subsample(2, 2)

lb = Label(image=image)
lb.place(x= 20 , y = 100, height=500, width=500)

#JanelaPricipal=================

#Stringsvar---------------------
qtdstr = StringVar()
combostr= StringVar()
#Numero comanda-----------------

#Label
ncomanda = Label(root, font=('arial', 18), text='Comanda:')
ncomanda.grid(row=1, column= 2)
#Entry
ncomandaE = Entry(root, font=('arial',20, 'bold'), width = 15, insertwidth=4, justify= 'center', border=3, relief="flat")
ncomandaE.grid(row=2, column= 2)

#tabela prods add---------------
addprod = ttk.Treeview(root, show='headings', height=22)
addprod["columns"] = ("one", "two", "three")
addprod.column("one", width=50)
addprod.column("two", width=360)
addprod.column("three", width=65)

addprod.heading("one", text='Qtd', anchor='w')
addprod.heading("two", text="Produto", anchor='w')
addprod.heading("three", text="Preço", anchor='w')

addprod.place(x=450,y=100)

#DeleteAllTreviewFunction------
rst = StringVar()


def deleteall():
    searchcb.delete(0, END)
    rst.set(" 0 ")
    addprod.delete(*addprod.get_children())

#DeleteSelected----------------
def deletesel():
    selected_item = addprod.selection()
    addprod.delete(selected_item)

#Frames De separaçao============
#frame de separacao
fram1 = Frame(root, width = 120, height =0 )
fram1.grid(row=1, column=1)
#frame de separacao
fram2 = Frame(root, width = 50, height = 20)
fram2.grid(row=1, column=6)
#frame de separacao
fram3 = Frame(root, width = 100, height = 20)
fram3.grid(row=1, column=4)

#Quantidade produto------------
#qtd Entry
Quant = Entry(root,font=('arial', 20, 'bold'), width = 7, insertwidth=4, justify= 'center', border=3, textvariable = qtdstr, relief ="flat")
qtdstr.set(1)
Quant.grid(row= 2, column= 5)
#qtd Label
quantL = Label(root, text='Quantidade:', font=('arial', 15))
quantL.grid(row=1, column= 5)

#ComboBox dos prods-------------


#ComboLabel
cbLabel = Label(root, text='Selecionar produto:', font=('arial',14))
cbLabel.grid(row=1, column=7)

#AddtreeviewFunction
def addbtt():
    global precodb
    var4 = Quant.get()
    var5 = searchcb.get()
    var6 = ncomandaE.get()
    if var6 == '':
        messagebox.showerror("Di Pastel","Por favor selecione uma comanda", parent = searchcb)
    elif var5 == '' or var4 == '':
        messagebox.showerror("Di Pastel", "Por favor preencha todos os campos", parent= searchcb)
    else:
        global i
        global e
        i = int(qtdstr.get())
        e = combostr.get()
        c.execute('SELECT preco FROM PRODUTOS WHERE produtos = ?', (e,))
        precodb = c.fetchall()
        datta = (i, e, precodb)
        addprod.insert("", END, values = datta)


#Addbtt
img = PhotoImage(file = 'C:\\Users\Dinopc\Desktop\DiPastel\plussign.gif')
img = img.subsample(30,30)
addbtt= Button (root,image = img , width = 40, command = addbtt, bd = '0')
addbtt.grid(row=2, column= 8)
#FuncaoSOMAR------------------
def soma():

    global total

    total = 0.0

    for child in addprod.get_children():
        total += float(addprod.item(child, 'values' )[2])

        rst.set(format(total))


#BottomButtons------------------




deleteall = Button(root, text = 'Limpar', font=('arial', 12), width = 15, height = 4, command = deleteall, bg = 'NavajoWhite4', foreground = "white", relief = "flat")
deleteall.place(x = 620, y=650)

delete = Button(root, text = 'Deletar', font=('arial', 12), width = 15, height = 4, command = deletesel, bg = 'coral3', foreground = "white", relief = "flat")
delete.place(x = 450, y=650)




#Somatotal---------------------
#Frames
totalframe = Frame(root, width = 480, height =70, relief = GROOVE, bd= 2)
totalframe.place(x= 450, y= 574)
totalframe2 = Frame(root, width = 150, height =70, relief = GROOVE, bd= 2, bg = "white")
totalframe2.place(x= 780, y= 574)
#Labels
totalL= Button(root, text ='Total', font=('Arial', 25, 'bold'), borderwidth = 0, command = soma )
totalL.place(x= 470, y= 577)

##totalLR= Label(root, text ='R$', font=('Arial', 25), fg = 'black')
##totalLR.place(x= 715, y= 590)

result = Label(root,text = 'R$ 0', font=('arial', 25), bg= 'white', textvariable = rst)
rst.set(' 0')
result.place(x=845, y= 590)


r = Label(root, text = 'R$ ', font=('arial', 18), bg= 'white')
r.place(x= 785, y=580)

#Entry
##totalE = Entry(root,font=('arial', 40, 'bold'), width = 5, insertwidth=4, justify= 'left', border=2)
##totalE.place(x= 780, y= 574 )



#MenuProdutos===================

#Definindo Funçoes==============

#Definindo Funçao de Editar produtos
def viz_fun():

    global sch
    rand = StringVar()
    rootviz = Tk()
    rootviz.title('Vizualizar Produtos')
    rootviz.resizable(width=False, height=False)
    rootviz.geometry('616x274+50+150')

    searchL = Label(rootviz,text='Procurar \n Produto', font=('arial', 12))
    searchL.grid(row=0, column= 0)
    searchE = Entry(rootviz,font=('arial', 13),width=33)
    searchE.grid(row= 0, column=2)
    lbl = Label(rootviz, text='', font=('arial', 150))
    lbl.grid(row=1, column=2)

    sch = searchE.get()





    f1 = Frame(rootviz, width= 300, height = 400, bd= 2)
    f1.place(x= 0, y= 44)


#DefiningTreeviewWidgets================
    scrollbar = Scrollbar(f1)
    scrollbar.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(f1, show='headings', yscrollcommand = scrollbar.set)
    tree["columns"] = ("one", "two", "three")
    tree.column("one", width=342)
    tree.column("two", width=100)
    tree.column("three", width=150)
    tree.heading("one", text='Produtos', anchor='w')
    tree.heading("two", text="Preço", anchor='w')
    tree.heading("three", text="Observação", anchor='w')



    tree.pack(side = 'left', expand=True)
    scrollbar.config( command= tree.yview)
#InsertingValuesToTreeView=============

    sql2 = 'SELECT * FROM PRODUTOS ORDER BY observacao ASC'
    result = c.execute(sql2)
    row = c.fetchall()
    for row in row:
        tree.insert("", END, values = row)

    def showProds():

        find_produto = ("SELECT * FROM PRODUTOS WHERE produtos LIKE ? ")
        c.execute(find_produto, [(searchE.get())])
        row = c.fetchall()
        if row:
            tree.delete(*tree.get_children())
            for row in row:
                tree.insert("", END, values = row)
        else:
            pass


##        c.execute("SELECT * FROM PRODUTOS WHERE produtos LIKE ?"(%+sch+%))
##        row = c.fetchall()
##        for produtos in row:
##            tree.insert("", END, values = row)

    searchB = Button(rootviz, text='Procurar', width=10, height = 2, command=showProds )
    searchB.grid(row= 0, column=3)
#DefinindoDeletarBut====================

    def delete():

        selected_item = tree.selection()
        for selected_item in tree.selection():
            c.execute("DELETE FROM PRODUTOS WHERE produtos=?", (tree.set(selected_item, '#1'),))
            conn.commit()
            tree.delete(selected_item)

            messagebox.showinfo('Sucesso', "Excluido com sucesso " , parent= delbtt)



    delbtt= Button(rootviz, text='Deletar', command= delete, width=10, height= 2)
    delbtt.grid(row=0, column= 4)


#EditButton============================
    def edit_btt():
        ########################
        selectinput = tree.selection()
        for selectinput in tree.selection():
            sql = c.execute( "SELECT * FROM PRODUTOS WHERE produtos=? ", (tree.set(selectinput, '#1'),))
            for row in sql:
                produtos = row[0]
                precos = row[1]
                observacaos = row[2]


            conn.commit()

        if selectinput == '"':
            messagebox.showerror("!", "Por favor selecione um produto", parent= editbtt)

        else:
            rootedit = Tk()
            rootedit.geometry('310x160+100+150')
            rootedit.resizable(False, False)
            rootedit.title('Editar ')

            lbl1= Label(rootedit, text='')
            lbl1.grid(row=0, column=0)
            lbl2= Label(rootedit, text='')
            lbl2.grid(row=1, column=0)

            title_frame = Frame(rootedit, width = 400, height = 30, bg = "black")
            title_frame.place( x = 0 , y = 0)

            titleL = Label(rootedit,font=('courier new', 14), text='Editar Produto', bg = "black", fg = "white")
            titleL.place(x= 90, y=0)

            editqtl = Label(rootedit,font=('courier new', 13), text='Preco: ')
            editqtl.grid(row=4, column=0, sticky= W)


            editvld = Label(rootedit,font=('courier new', 13), text='Observacao: ')
            editvld.grid(row=3, column=0, sticky= W)

            editprodL = Label(rootedit, text=('Produtos: '), font=('courier new', 13))
            editprodL.grid(row=2, column= 0, sticky= W)

            editprodE = Entry(rootedit, width= 22, font=('courier new', 13))
            editprodE.grid(row=2, column= 1, sticky= W)
            editprodE.insert(END, str(produtos))


            editqtlE = Entry(rootedit, width=10, font=('courier new', 13))
            editqtlE.grid(row=4, column= 1, sticky= W)
            editqtlE.insert(END, str(precos))

            editvldE = Entry(rootedit, width = 15, font=('courier new', 13))
            editvldE.grid(row=3, column= 1, sticky= W)
            editvldE.insert(END, str(observacaos))
        #####################
        def update_btt():
            var1= editprodE.get()
            var2= editqtlE.get()
            var3= editvldE.get()

            txtupdate= tree.selection()
            for txtupdate in tree.selection():
                query = c.execute("UPDATE PRODUTOS SET produtos=?, preco=?, observacao=? WHERE produtos=?", (var1, var2, var3, tree.set(txtupdate, '#1'),))
                conn.commit()
            messagebox.showinfo('Sucesso', "Atualizado com sucesso " , parent= okbtt)

            tree.delete(*tree.get_children())

            sql2 = 'SELECT * FROM PRODUTOS'
            result = c.execute(sql2)
            row = c.fetchall()
            for row in row:
                tree.insert("", END, values = row)

            rootedit.destroy()


        okbtt= Button (rootedit, text='Salvar', width = 10, command=update_btt , bg = "SpringGreen4", fg = "white", relief = "flat" )
        okbtt.place(x = 120 , y = 130)


#####################
    editbtt = Button(rootviz, text = 'Editar', command= edit_btt, width=10, height= 2)
    editbtt.grid(row=0, column= 5)


#Definindo Funçao de add Produtos

def add_fun():
    global var1
    global var2
    global var3
    rootadd = Tk()
    rootadd.title('Adicionar produto')
    rootadd.resizable(width=False, height=False)
    rootadd.geometry('600x150+50+150')

#Adicionando Labels----------------

    instrucao_frame = Frame(rootadd, bg = "black" , width = 900 , height = 30)
    instrucao_frame.place(x=0, y = 0)

    instrucao_title = Label(rootadd, font=('courier new', 15),text='Adicionar Produto: ' ,bg = "black", fg = "white")
    instrucao_title.place(x = 160, y = 0)

    nameL = Label(rootadd, font=('courier new', 13),text='Produto: ')
    nameL.place(x = 0 , y = 55)

    prçL = Label(rootadd,font=('courier new ', 13), text='Preço: ')
    prçL.place(x = 0 , y = 85)

    obsL = Label(rootadd,font=('courier new', 13), text='Observação:')
    obsL.place(x = 0 , y = 115)

    prcRs= Label(rootadd, font=('courier new', 13), text='R$', bg = "white")
    prcRs.place(x = 115 , y = 85)

#Adicionando Entrys-----------------

    nameE = Entry(rootadd,font=('arial', 13) ,width=35, relief = "solid")
    nameE.place(x = 115 , y = 55)

    prçE = Entry(rootadd,font=('arial', 13), width=15, relief = "solid")
    prçE.place(x = 115 , y = 85)

    obsE = Entry(rootadd,font=('arial', 13) ,width=35 , relief = "solid")
    obsE.place(x = 115 , y = 115)


#Definindo funçao-------------------
    def add_prod():
        global var1
        global var2
        global var3
        var1 = nameE.get()
        var2 = prçE.get()
        var3 = obsE.get()
#MessageBox--------------------------
        if var1 == '' or var2 == '' or var3 == '':
            messagebox.showerror("!", "Por favor preencha todos os campos", parent= inbut)
#Adicionando ao banco de dados------
        else:
            sql = "INSERT INTO 'PRODUTOS' (produtos, preco, observacao) VALUES(?, ?, ?)"
            c.execute(sql, (var1, var2, var3))
            conn.commit()
            messagebox.showinfo(':D', "Produto " + str(var1) + " adicionado com sucesso", parent= inbut)
            nameE.delete(0, END)
            prçE.delete(0, END)
            obsE.delete(0, END)

#Adicionado BttAdd-------------------

    inbut = Button(rootadd, text='Adicionar',font=('arial', 11), width=12, height= 3, bg = "SpringGreen4", fg= "white",relief = "flat",command=add_prod)
    inbut.place(x=468, y=60)

#DropMenu=======================
menu = Menu(root) #Criando Menu
root.config(menu=menu) #Tkinter reconhece menu
#MenuProdutos===================
menuproduto= Menu(menu)
menuproduto.add_command(label= "Add Produtos" , command = add_fun)
menuproduto.add_command(label= "Lista De Produtos", command = viz_fun)
menu.add_cascade(label= "Produtos", menu = menuproduto)


def combo_input():
    c.execute('SELECT produtos FROM PRODUTOS ')

    data = []

    for row in c.fetchall():
        data.append(row[0])

    return data
    conn.commit()


searchcb = ttk.Combobox(root,font=('arial', 14), width = 18, textvariable = combostr)
searchcb.grid(row=2, column= 7)

searchcb['values'] = combo_input()


def comandas():
    rtcm = Tk()
    rtcm.geometry('550x300+50+150')
    rtcm.title("Comandas em aberto")
    rtcm.resizable(width=False, height=False)
#Treeview
    display = ttk.Treeview(rtcm, show='headings', height = 13)
    display.grid(row = 0, column = 0)

    display["columns"] = ("one", "two", "three", "four")
    display.column("one", width=100)
    display.column("two", width=220)
    display.column("three", width=15)
    display.column("four", width=105)
    display.heading("one", text='Comanda', anchor='w')
    display.heading("two", text="Status", anchor='w')
    display.heading("three", text="", anchor='w')
    display.heading("four", text="Valor Total", anchor='w')
    f = ("SELECT comandas, status,R$, valor FROM comanda")
    c.execute(f)
    raw = c.fetchall()
    for raw in raw :
        display.insert("",END ,values = raw)



    def zerar():
        vari1 = 0
        vari2 = 'Inativa'
        vari3 = "Nenhum produto adicionado"

        sele = display.selection()
        for sele in display.selection():
            sq = c.execute("UPDATE comanda SET valor = ? , status =?, produtos =? WHERE  comandas = ?", (vari1, vari2 , vari3,display.set(sele, '#1'),))
            if sele == "I001":
                sqw = c.execute("DELETE FROM consumidos WHERE ([1]) IS NOT NULL")
            elif sele == "I002":
                sqw = c.execute("DELETE FROM consumidos WHERE ([2]) IS NOT NULL")
            elif sele == "I003":
                sqw = c.execute("DELETE FROM consumidos WHERE ([3]) IS NOT NULL")
            elif sele == "I004":
                sqw = c.execute("DELETE FROM consumidos WHERE ([4]) IS NOT NULL")
            elif sele == "I005":
                sqw = c.execute("DELETE FROM consumidos WHERE ([5]) IS NOT NULL")
            elif sele == "I006":
                sqw = c.execute("DELETE FROM consumidos WHERE ([6) IS NOT NULL")
            elif sele == "I007":
                sqw = c.execute("DELETE FROM consumidos WHERE ([7]) IS NOT NULL")
            elif sele == "I008":
                sqw = c.execute("DELETE FROM consumidos WHERE ([8]) IS NOT NULL")
            elif sele == "I009":
                sqw = c.execute("DELETE FROM consumidos WHERE ([9) IS NOT NULL")
            elif sele == "I00A":
                sqw = c.execute("DELETE FROM consumidos WHERE ([10]) IS NOT NULL")
            elif sele == "I00B":
                sqw = c.execute("DELETE FROM consumidos WHERE ([11]) IS NOT NULL")
            elif sele == "I00C":
                sqw = c.execute("DELETE FROM consumidos WHERE ([12]) IS NOT NULL")
            elif sele == "I00D":
                sqw = c.execute("DELETE FROM consumidos WHERE ([13]) IS NOT NULL")
            elif sele == "I00E":
                sqw = c.execute("DELETE FROM consumidos WHERE ([14]) IS NOT NULL")
            elif sele == "I00F":
                sqw = c.execute("DELETE FROM consumidos WHERE ([15]) IS NOT NULL")


            messagebox.showinfo('Di Pastel', "Comanda zerada com sucesso !", parent= zerarc)
        display.delete(*display.get_children())

        aw = c.execute('SELECT comandas, status, R$, valor FROM comanda')
        raw= c.fetchall()
        for raw in raw:
            display.insert("", END, values = raw)


        conn.commit()
#======================================================================================================================================================================
    def fechar():
        global tot
        fech = Tk()
        fech.geometry('500x450+50+150')
        fech.title('Di Pastel')

        product = ttk.Treeview(fech , show="headings")
        product.place(x = 20, y= 80)
        product["columns"] = ("one")
        product.column("one", width = 450 )
        product.heading ("one" , text = "Consumidos", anchor = "w")

        def conc():
            vari1= 'Fechada'
            select = display.selection()
            for select in display.selection():
                sqw = c.execute("UPDATE comanda SET status = ? WHERE comandas = ?", (vari1, display.set(select, '#1'),))

            display.delete(*display.get_children())
            af = c.execute('SELECT comandas, status, R$, valor FROM comanda')
            rew= c.fetchall()
            for rew in rew:
                display.insert("", END, values = rew)

            fech.destroy()

            conn.commit()

        def cancel():
            fech.destroy()

        def passprods():
            selec = display.selection()
            for selec in display.selection():
                if selec == 'I001':
                    s = c.execute("SELECT ([1]) FROM consumidos WHERE ([1]) IS NOT NULL")
                elif selec == 'I002':
                    s = c.execute("SELECT ([2]) FROM consumidos WHERE ([2]) IS NOT NULL")
                elif selec == "I003":
                    s = c.execute("SELECT ([3]) FROM consumidos WHERE ([3]) IS NOT NULL")
                elif selec == "I004":
                    s = c.execute("SELECT ([4]) FROM consumidos WHERE ([4]) IS NOT NULL")
                elif selec == "I005":
                    s = c.execute("SELECT ([5]) FROM consumidos WHERE ([5]) IS NOT NULL")
                elif selec == "I006":
                    s = c.execute("SELECT ([6]) FROM consumidos WHERE ([6]) IS NOT NULL")
                elif selec == "I007":
                    s = c.execute("SELECT ([7]) FROM consumidos WHERE ([7]) IS NOT NULL")
                elif selec == "I008":
                    s = c.execute("SELECT ([8]) FROM consumidos WHERE ([8]) IS NOT NULL")
                elif selec == "I009":
                    s = c.execute("SELECT ([9]) FROM consumidos WHERE ([9]) IS NOT NULL")
                elif selec == "I00A":
                    s = c.execute("SELECT ([10]) FROM consumidos WHERE ([10]) IS NOT NULL")
                elif selec == "I00B":
                    s = c.execute("SELECT ([11]) FROM consumidos WHERE ([11]) IS NOT NULL")
                elif selec == "I00C":
                    s = c.execute("SELECT ([12]) FROM consumidos WHERE ([12]) IS NOT NULL")
                elif selec == "I00D":
                    s = c.execute("SELECT ([13]) FROM consumidos WHERE ([13]) IS NOT NULL")
                elif selec == "I00E":
                    s = c.execute("SELECT ([14]) FROM consumidos WHERE ([14]) IS NOT NULL")
                else:
                    s = c.execute("SELECT ([15]) FROM consumidos WHERE ([15]) IS NOT NULL")

                ruw = c.fetchall()
                for ruw in ruw:
                    product.insert('',END, values = ruw)

        passprods()



        def totalv():

            global t

            var1 = "1"
            var2 = "2"
            var3 = "3"
            var4 = "4"
            var5 = "5"
            var6 = "6"
            var7 = "7"
            var8 = "8"
            var8 = "8"
            var9 = "9"
            var10 = "10"
            var11 = "11"
            var12 = "12"
            var13 = "13"
            var14 = "14"
            var15 = "15"

            tselec = display.selection()
            for tselec in display.selection():
                if tselec == 'I001':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var1,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I002':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var2,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I003':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var3,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I004':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var4,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I005':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var5,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I006':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var6,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I007':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var7,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I008':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var8,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I009':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var9,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00A':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var10,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00B':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var11,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00C':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var12,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00D':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var13,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00E':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var14,))
                    row = c.fetchall()

                    for r in row:
                        t = r

                if tselec == 'I00F':
                    r = c.execute("SELECT valor FROM comanda WHERE comandas = ?", (var15,))
                    row = c.fetchall()

                    for r in row:
                        t = r

        totalv()

#WIDGETS FECH WINDOW
        comandaL = Label(fech, text=('Fechar comanda :'), font = ("arial", 19))
        comandaL.place(x=20,y=27)
#treeview

#label
        vtotal = Label(fech, text=('Valor \n Total'), font=('arial', 15))
        vtotal.place(x = 50 , y = 330)

        vrecebido = Label(fech, text=('Valor \n Recebido'), font=('arial', 15))
        vrecebido.place(x = 200 , y = 330)
#entry
        totalframe = Frame(fech, width = 110, height = 37, bg= 'white', bd = 1 , relief = GROOVE)
        totalframe.place(x = 35 , y = 390)

        trocoframe = Frame(fech, width = 100, height = 37, bg= 'white', bd = 1 , relief = GROOVE)
        trocoframe.place(x = 384 , y = 390)


        roc = StringVar()
        erecebido = Entry(fech, font=('arial', 20),width = 6, insertwidth= 4, justify = "right", textvariable = roc)
        erecebido.place(x = 200 , y = 390)

        # $$$
        first = Label(fech , text = ('R$ '), font=('arial', 11), bg='white')
        first.place(x = 40, y = 393)

        second = Label(fech , text = ('R$ '), font=('arial', 11), bg='white')
        second.place(x = 390, y = 393)

        third = Label(fech , text = ('R$ '), font=('arial', 11), bg='white')
        third.place(x = 202, y = 393)


#Button
        cancel = Button(fech, text=('Cacelar \n Operação'),font = ("Symbola 9"), bg = 'coral3',fg = "white", height = 4, width = 10, command = cancel , relief = "flat")
        cancel.place(x= 320, y=0)

        #concluir = Button(fech, text=('Concluir \n Operação'), bg = "green yellow", height = 4, width = 10, command = troco)
        #concluir.place(x= 405, y=0)

        ltotal = Label(fech,text=(t), font= ('arial', 17),  bg = "white")
        ltotal.place(x = 70 , y = 393)


        tvtroco = StringVar()

        def troco():

            global result1
            global t

            qt = float(erecebido.get())
            total1 = float(t[0])
            result1 = qt - total1

            ltroco = Label(fech,text=(result1), font= ('arial', 18), bg = "white")
            ltroco.place(x = 420, y = 393)


        ltroco = Label(fech,text=("0.0"), font= ('arial', 18), bg = "white")
        ltroco.place(x = 420, y = 393)

        troco = Button(fech, text=("Troco"), font=('arial', 15), borderwidth = 0,command = troco)
        troco.place(x = 400 , y = 350)




        concluir = Button(fech, text=('Concluir \n Operação'), bg = "SpringGreen4",fg = "white", height = 4, width = 10, command = conc, relief = "flat")
        concluir.place(x= 405, y=0)


    #Buttons
    zerarc = Button(rtcm, text=('Zerar \n comanda'), font=('Arial', 9),width = 13, height = 4, command = zerar, foreground = "white", bg = "coral3", relief = "flat")
    zerarc.place(x= 445, y = 215)

    #prodsB = Button(rtcm, text=('Produtos'), width = 13, height = 4, command= prod)
    #prodsB.place(x= 445, y = 73)

    fecharB = Button(rtcm, text=('Fechar \n comanda'),font=('Arial', 9), width = 13, height = 4, command = fechar, foreground = "white", bg = "NavajoWhite4", relief = "flat")
    fecharB.place(x= 445, y = 138)



def cmd():


    variavel1 = int(ncomandaE.get())
    variavel2 = "Aberto"
    variavel3 = rst.get()

    for row in addprod.get_children():
        variavel4 = addprod.item(row)['values'][1]
        var0 = str(variavel4)
        if variavel1 == 1:
            lite = "INSERT INTO 'consumidos'([1]) VALUES (?) "
            c.execute(lite, [var0])

            conn.commit()
        elif variavel1 == 2:
            lite = "INSERT INTO 'consumidos'([2]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 3:
            lite = "INSERT INTO 'consumidos'([3]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 4:
            lite = "INSERT INTO 'consumidos'([4]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 5:
            lite = "INSERT INTO 'consumidos'([5]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 6:
            lite = "INSERT INTO 'consumidos'([6]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 7:
            lite = "INSERT INTO 'consumidos'([7]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 8:
            lite = "INSERT INTO 'consumidos'([8]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 9:
            lite = "INSERT INTO 'consumidos'([9]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 10:
            lite = "INSERT INTO 'consumidos'([10]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 11:
            lite = "INSERT INTO 'consumidos'([11]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 12:
            lite = "INSERT INTO 'consumidos'([12]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 13:
            lite = "INSERT INTO 'consumidos'([13]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 14:
            lite = "INSERT INTO 'consumidos'([14]) VALUES (?) "
            c.execute(lite, [var0])
        elif variavel1 == 15:
            lite = "INSERT INTO 'consumidos'([15]) VALUES (?) "
            c.execute(lite, [var0])

    messagebox.showinfo('Di Pastel', "Comanda " + str(variavel1) + " salva com sucesso", parent= savebtt)

    sq = ("UPDATE comanda SET valor = valor + ?, status = ? WHERE comandas = ?")
    c.execute(sq, (variavel3,variavel2, variavel1))



    conn.commit()

savebtt = Button(root, text = 'Salvar Comanda', font=('arial', 12), width = 15, height = 4, bg = 'SpringGreen4', command = cmd, foreground = "white" , relief = "flat")
savebtt.place(x = 785, y=650)
#MenuComanda===================
menucomanda = Menu(menu)
menucomanda.add_command(label = "Comandas em aberto", command =comandas )
menu.add_cascade(label = "Comandas", menu = menucomanda)


#Definindo a func Usuarios
def usuarios():

    #Conectando com o banco de dados Login
    conn = sqlite3.connect("Login.db")
    c = conn.cursor()
    #Criando a Janena Usuarios
    usuario_root = Tk()
    usuario_root.geometry("482x350+50+150")
    usuario_root.title("Di Pastel")
    usuario_root.resizable(False,False)

    #Criando WIDGETS
    title_frame = Frame(usuario_root, width = 700, height= 40, bg= "black")
    title_frame.place(x= 0, y = 0)

    title_label = Label(usuario_root, text = "Usuários" , font = ("Courier new" , 16 ), bg = "black", fg = "White")
    title_label.place(x = 190, y = 4)

    #Criando treeview
    usuarios_tree = ttk.Treeview(usuario_root, show ="headings", height = 14)
    usuarios_tree.place(x = 0, y = 40)
    usuarios_tree["columns"] = ("one", "two")
    usuarios_tree.column("one" , width = 315)
    usuarios_tree.column("two", width = 80)
    usuarios_tree.heading("one", text = "Nome", anchor = "w")
    usuarios_tree.heading("two", text = "Código", anchor = "w")
    #Colocando os dodos do BD dentro da Treeview
    def show_users():
        get_user = ('SELECT nome, cod FROM login')
        c.execute(get_user)
        row = c.fetchall()
        for row in row:
            usuarios_tree.insert('', END, values = row)

    show_users()

    def delete_user():
        MsgBox = messagebox.askquestion ('Di Pastel','Tem certeza que deseja excluir esse usuário ? ',icon = 'warning', parent= del_user)
        if MsgBox == 'yes':
            select_user = usuarios_tree.selection()
            for select_user in usuarios_tree.selection():
                c.execute("DELETE FROM login WHERE nome=?", (usuarios_tree.set(select_user, '#1'),))
                conn.commit()
                usuarios_tree.delete(select_user)
        else:
            pass



    #Buttons
    del_user = Button(usuario_root, text = "Deletar \n Usuario", font= ('arial', 13) , relief = 'flat' , bg = 'coral3' , fg = 'White', command = delete_user)
    del_user.place(x = 400, y = 295)

    def adc_usuarios():

        tree_selection = usuarios_tree.selection()
        for tree_selection in usuarios_tree.selection():
            sql = c.execute( "SELECT * FROM login WHERE nome=? ", (usuarios_tree.set(tree_selection, '#1'),))
            for row in sql:
                nome = row[0]
                cod = row[1]


        edit_user_root = Tk()
        edit_user_root.geometry('310x220+100+150')
        edit_user_root.resizable(False, False)
        edit_user_root.title('Di Pastel ')

        title_frame = Frame(edit_user_root, width = 400, height = 30, bg = "black")
        title_frame.place( x = 0 , y = 0)

        #Labels
        titleL = Label(edit_user_root,font=('courier new', 14), text='Editar Usuario :', bg = "black", fg = "white")
        titleL.place(x= 60, y=0)

        editnome = Label(edit_user_root,font=('courier new', 13), text='Nome : ')
        editnome.place(x = 14, y = 40)

        editcod = Label(edit_user_root,font=('courier new', 13), text='Cod : ')
        editcod.place(x = 14, y = 80)

        editsa= Label(edit_user_root, text='Senha \n Antiga: ', font=('courier new', 13))
        editsa.place(x = 0, y = 110)

        editsn = Label(edit_user_root, text='Nova \n Senha: ', font=('courier new', 13))
        editsn.place(x = 0, y = 155)

        #Entrys
        editnomeE = Entry(edit_user_root, width=15, font=('courier new', 13), relief = "solid" )
        editnomeE.place(x = 90, y = 40)
        editnomeE.insert(END, str(nome))

        editcodE = Entry(edit_user_root, width=6, font=('courier new', 13), relief = "solid")
        editcodE.place(x = 90, y = 80)
        editcodE.insert(END, str(cod))

        editvsaE = Entry(edit_user_root, width = 6, font=('courier new', 13), relief = "solid", show = "*")
        editvsaE.place(x = 90, y = 120)

        editnsE = Entry(edit_user_root, width = 6, font=('courier new', 13), relief = "solid",show = "*")
        editnsE.place(x = 90, y = 165)

        def update_passaword():
            nome_updt = editnomeE.get()
            cod_updt = editcodE.get()
            senha_nova_updt = editnsE.get()



            get_old_passd = ('SELECT senha FROM login WHERE nome = ?')
            c.execute(get_old_passd, (usuarios_tree.set(tree_selection, '#1'),))
            raw = c.fetchall()

            conn.commit()

            for raw in raw:
                ruw = str(raw[0])
                if editvsaE.get() == ruw:
                    if editnsE.get() == "" or editvsaE.get() == "":
                        Error_msg = messagebox.showerror ('Di Pastel',  "Por favor, Preencha todos os campos", parent= save_button)
                    else:
                        login_updt= usuarios_tree.selection()
                        for login_updt in usuarios_tree.selection():
                            query = c.execute("UPDATE login SET nome=?, cod=?, senha=? WHERE nome=?", (nome_updt, cod_updt, senha_nova_updt, usuarios_tree.set(login_updt, '#1'),))
                            conn.commit()
                            messagebox.showinfo('Di Pastel', "Usuario " + nome_updt +  " atualizado com sucesso " , parent= save_button)
                            editvsaE.delete(0, END)
                            editnsE.delete(0, END)

                            usuarios_tree.delete(*usuarios_tree.get_children())

                            get_login_table = ("SELECT * FROM login")
                            c.execute(get_login_table)
                            i = c.fetchall()
                            for i in i :
                                usuarios_tree.insert("" , END, values = i )

                else:
                    Error_msg = messagebox.showerror ('Di Pastel',  "Senha Incorreta ! ", parent= save_button)
                    editvsaE.delete(0, END)
                    editnsE.delete(0,END)


        save_button= Button (edit_user_root, text='Salvar', width = 10, bg = "SpringGreen4", fg = "white", relief = "flat" ,command = update_passaword)
        save_button.place(x = 190 , y = 170)

    edit_user = Button(usuario_root, text = "Editar \n Usuario", font= ('arial', 13), relief = 'flat', bg = 'NavajoWhite4' , fg = 'White', command = adc_usuarios)
    edit_user.place(x = 400, y = 240)


def NovoUser():

    #Conectando com o banco de dados Login
    conn = sqlite3.connect("Login.db")
    c = conn.cursor()

    new_user_root = Tk()
    new_user_root.geometry('410x150+50+150')
    new_user_root.title("Di Pastel")
    new_user_root.resizable(False,False)

    instrucao_frame = Frame(new_user_root, bg = "black" , width = 900 , height = 30)
    instrucao_frame.place(x=0, y = 0)

    instrucao_title = Label(new_user_root, font=('courier new', 15),text='Adicionar Novo Usuário: ' ,bg = "black", fg = "white")
    instrucao_title.place(x =70, y = 0)

    nome_user = Label(new_user_root, font=('courier new', 13),text='Nome : ')
    nome_user.place(x = 0 , y = 55)

    cod_user = Label(new_user_root,font=('courier new', 13), text='Codigo : ')
    cod_user.place(x = 0 , y = 85)

    senha_user = Label(new_user_root,font=('courier new', 13), text='Senha :')
    senha_user.place(x = 0 , y = 115)


#Adicionando Entrys-----------------
    #defining A string var
    cod_value = StringVar()

    nome_userE = Entry(new_user_root,font=('courier new', 13) ,width=15, relief = "solid")
    nome_userE.place(x = 115 , y = 55)

    cod_userE = Entry(new_user_root,font=('courier new', 13), width=15, relief = "solid" , textvariable = cod_value)
    cod_userE.place(x = 115 , y = 85)

    senha_userE = Entry(new_user_root,font=('courier new', 13) ,width=15 , relief = "solid")
    senha_userE.place(x = 115 , y = 115)

    ##
    def adc_novousuario():
        novo_nome = nome_userE.get()
        novo_cod = cod_userE.get()
        nova_senha= senha_userE.get()

        add_database = ("INSERT INTO login(nome, cod, senha) VALUES (?,?,?)")
        c.execute(add_database , (novo_nome, novo_cod, nova_senha,))
        row_by_row = c.fetchall()
        messagebox.showinfo("Di Pastel", "Usuario " + novo_nome + " adicionado com sucesso ", parent =add_user_button )

        new_user_root.destroy()
        conn.commit()


        for row_by_row in row_by_row:
            usuarios_tree.insert("", END, values = row_by_row)


    add_user_button = Button(new_user_root, text = 'Adicionar', relief = 'flat', font= ('arial', 11), width=11, height= 2, bg = 'SpringGreen4' , fg = 'white', command = adc_novousuario)
    add_user_button.place(x = 290 , y = 92)

    #function for limit the characters of a entry
    def LimitCharacters(cod_value):
        if len(cod_value.get()) > 3:
            cod_value.set(cod_value.get()[:3])


    cod_value.trace('w',  LimitCharacters(cod_value))








menu_login = Menu(menu)
menu_login.add_command(label = "Usuários" , command = usuarios)
menu_login.add_command(label = "Novo usuário" , command = NovoUser)
menu.add_cascade(label = "Configuração", menu = menu_login)


root.mainloop()
