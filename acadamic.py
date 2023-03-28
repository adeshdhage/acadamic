from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Login():
    def __init__(self):
        self.root = root
        def search_data():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="stm"
            )
            mycursor = mydb.cursor()
            search=self.search_by.get()
            searchtxt=self.search_txt.get()
            # mycursor.execute("select * from accounts where account_number LIKE '%self.search_txt.get()%'" )
            cute = "select * from accounts where  account_number LIKE'%"+searchtxt+"%' OR account_holder LIKE'%"+searchtxt+"%'"
            mycursor.execute(cute)
            rows = mycursor.fetchall()
            if len(rows) != 0:
                self.ac_table.delete(*self.ac_table.get_children())
                for row in rows:
                    self.ac_table.insert('', END, values=row)

                mydb.commit()
            mydb.close()



        def delete_data():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="stm"
            )
            mycursor = mydb.cursor()

            sql = "DELETE FROM accounts WHERE account_number = %s"
            adr = (self.number_var.get(),)

            mycursor.execute(sql, adr)

            mydb.commit()

            fetch_data(self)
            clear()
            messagebox.showinfo("info", 'entry is deleted')

        def update_data():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="stm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("update accounts set date=%s,account_holder=%s,magil_shillk=%s,karj=%s,yene_karj=%s,jama_karj=%s,jama_vyaj=%s,shillk=%s where account_number=%s",(
            self.date_var.get(),
            self.account_var.get(),
            self.magil_shillk_var.get(),
            self.karj_var.get(),
            self.yene_karj_var.get(),
            self.jama_karj_var.get(),
            self.jama_vyaj_var.get(),
            self.shillk_var.get(),
            self.number_var.get()
))


            mydb.commit()
            fetch_data(self)
            clear()
            mydb.close()
            messagebox.showinfo("info", 'entry is updated')

        def get_cursor(ev):
            cursor_row=self.ac_table.focus()
            contents=self.ac_table.item(cursor_row)
            row=contents['values']


            self.number_var.set(row[0])
            self.date_var.set(row[1])
            self.account_var.set(row[2])
            self.magil_shillk_var.set(row[3])
            self.karj_var.set(row[4])
            self.yene_karj_var.set(row[5])
            self.jama_karj_var.set(row[6])
            self.jama_vyaj_var.set(row[7])
            self.shillk_var.set(row[8])
            # self.txt_address.delete("1.0",END)
            # self.txt_address.insert(END,row[9])

        def clear():
            self.number_var.set("")
            self.date_var.set("")
            self.account_var.set("")
            self.magil_shillk_var.set("")
            self.karj_var.set("")
            self.yene_karj_var.set("")
            self.jama_karj_var.set("")
            self.jama_vyaj_var.set("")
            self.shillk_var.set("")

        def fetch_data(self):
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="stm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("select * from accounts")
            rows = mycursor.fetchall()
            if len(rows) != 0:
                self.ac_table.delete(*self.ac_table.get_children())
            for row in rows:
                self.ac_table.insert('', END, values=row)

            mycursor.close()
        def data():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="stm"
            )
            mycursor = mydb.cursor()
            mycursor.execute("select * from accounts")
            rows = mycursor.fetchall()
            if len(rows) != 0:
                self.ac_table.delete(*self.ac_table.get_children())
            for row in rows:
                self.ac_table.insert('', END, values=row)

            mycursor.close()
        def add():
            if self.number_var.get()=="" or self.account_var.get()=="":
               messagebox.showerror("error", 'All filds are require')
            else:
                number1 = (self.number_var.get())
                date1 = (self.date_var.get())
                accounth1 = (self.account_var.get())
                magil_shillk1 = (self.magil_shillk_var.get())
                karj1 = (self.karj_var.get())
                yene_karj1 = (self.yene_karj_var.get())
                jama_karj1 = (self.jama_karj_var.get())
                jama_vyaj1 = (self.jama_vyaj_var.get())
                shillk1 = (self.shillk_var.get())
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="stm"
                )
                mycursor = mydb.cursor()
                sql = "INSERT INTO accounts (account_number,date,account_holder,magil_shillk , karj,yene_karj,jama_karj,jama_vyaj,shillk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (number1, date1, accounth1, magil_shillk1, karj1, yene_karj1, jama_karj1, jama_vyaj1, shillk1)
                mycursor.execute(sql, val)

                mydb.commit()
                fetch_data(self)
                clear()
                mydb.close()
                messagebox.showinfo("info", 'your entry is added')









        self.root.title('छत्रपती महिला बचत गट')
        self.root.geometry('1199x600+50+40')
        self.root.resizable(FALSE, FALSE)




        title = Label(self.root, text="खातेदार", font=('times new roman', 30, 'bold'), bg='red', fg='white')
        title.pack(side=TOP, fill=X, pady=5)
        # ***************** manage frame ****************
        manage_frame = Frame(self.root, bg='cyan', bd=4, relief=RIDGE)
        manage_frame.place(x=35, y=80, width=380, height=500)
        # ***************** details frame ****************
        details_frame = Frame(self.root, bg='cyan', bd=4, relief=RIDGE)
        details_frame.place(x=430, y=80, width=750, height=500)
        m_title = Label(manage_frame, text=("manage accounts"), bg='cyan', fg='black',
                            font=('times new roman', 20, 'bold'))
        m_title.grid(row=0, columnspan=4, pady=15, padx=30)
        # ******************** all variable *******************
        self.number_var = IntVar()
        self.date_var = StringVar()
        self.account_var = StringVar()
        self.magil_shillk_var = IntVar()
        self.karj_var = IntVar()
        self.yene_karj_var = IntVar()
        self.jama_karj_var = IntVar()
        self.jama_vyaj_var = IntVar()
        self.shillk_var = IntVar()
        self.search_by= StringVar()
        self.search_txt = StringVar()
        # ******************** manage frame section *******************

        m_number = Label(manage_frame, text=("Account number"), bg='cyan', fg='black',
                             font=('times new roman', 13, 'bold'))
        m_number.grid(row=3, column=0, padx=5, pady=5)
        numentry = Entry(manage_frame, fg='black', textvariable=self.number_var,
                             font=('times new roman', 13, 'bold'), bd=4)
        numentry.grid(row=3, column=3, padx=20, pady=5)

        m_name = Label(manage_frame, text=("date"), bg='cyan', fg='black', font=('times new roman', 13, 'bold'))
        m_name.grid(row=9, column=0, columnspan=1, padx=0, pady=5)
        nameentry = Entry(manage_frame, fg='black', textvariable=self.date_var,
                              font=('times new roman', 13, 'bold'), bd=4)
        nameentry.grid(row=9, column=3, padx=20, pady=5)
        m_name = Label(manage_frame, text=("account holder"), bg='cyan', fg='black',
                           font=('times new roman', 13, 'bold'))
        m_name.grid(row=10, column=0, columnspan=1, padx=0, pady=5)
        nameentry = Entry(manage_frame, fg='black', textvariable=self.account_var,
                              font=('times new roman', 13, 'bold'), bd=4)
        nameentry.grid(row=10, column=3, padx=20, pady=5)

        m_shillk = Label(manage_frame, text=("magil shillak"), bg='cyan', fg='black',
                             font=('times new roman', 13, 'bold'))
        m_shillk.grid(row=12, column=0, padx=0)

        m_karj = Label(manage_frame, text=("  karj"), bg='cyan', fg='black', font=('times new roman', 13, 'bold'))
        m_karj.grid(row=16, pady=10, padx=0)
        karjentry = Entry(manage_frame, fg='black', textvariable=self.karj_var,
                              font=('times new roman', 13, 'bold'), bd=4)
        karjentry.grid(row=16, column=3, padx=20)

        shillkentry = Entry(manage_frame, fg='black', textvariable=self.magil_shillk_var,
                                font=('times new roman', 13, 'bold'), bd=4)
        shillkentry.grid(row=12, column=3, padx=20)

        ykarj = Label(manage_frame, text=("yene vyaj"), bg='cyan', fg='black', font=('times new roman', 13, 'bold'))
        ykarj.grid(row=18, padx=0)
        ykarjentry = Entry(manage_frame, fg='black', textvariable=self.yene_karj_var,
                               font=('times new roman', 13, 'bold'), bd=4)
        ykarjentry.grid(row=18, column=3, padx=20)

        jama_karj = Label(manage_frame, text=(" jama karj"), bg='cyan', fg='black',
                              font=('times new roman', 13, 'bold'))
        jama_karj.grid(row=22, pady=12, padx=0)
        jamakarjentry = Entry(manage_frame, fg='black', textvariable=self.jama_karj_var,
                                  font=('times new roman', 13, 'bold'), bd=4)
        jamakarjentry.grid(row=22, column=3, padx=20)

        jamavyaj = Label(manage_frame, text=("jama vyaj"), bg='cyan', fg='black',
                             font=('times new roman', 13, 'bold'))
        jamavyaj.grid(row=26, padx=0)
        jamavyajentry = Entry(manage_frame, fg='black', textvariable=self.jama_vyaj_var,
                                  font=('times new roman', 13, 'bold'), bd=4)
        jamavyajentry.grid(row=26, column=3, padx=20)

        nshillak = Label(manage_frame, text=("shillk"), bg='cyan', fg='black', font=('times new roman', 13, 'bold'))
        nshillak.grid(row=28, padx=0)
        nshillakentry = Entry(manage_frame, fg='black', textvariable=self.shillk_var,
                                  font=('times new roman', 13, 'bold'), bd=4)
        nshillakentry.grid(row=28, column=3, padx=20, pady=10)

        btframe = Frame(manage_frame, bg='cyan', bd=0)
        btframe.place(x=25, y=430, width=330, height=50)


        #**********************____button_____**********************

        addbutton = Button(btframe, text='Add', width=5, cursor='hand2',command=add).grid(row=0, column=1, padx=10,
                                                                                               pady=25)
        updatebutton = Button(btframe, text='Update', width=5, cursor='hand2',command=update_data).grid(row=0, column=2, padx=10,
                                                                                        pady=10)
        deletebutton = Button(btframe, text='Delete', width=5, cursor='hand2',command=delete_data).grid(row=0, column=3, padx=10,
                                                                                        pady=10)
        clearbutton = Button(btframe, text='Clear  ', width=5, cursor='hand2',command=clear).grid(row=0, column=4, padx=10,

                                                                                        pady=10)

        # *********************DETAILS FRAME EDITS******************
        Label(details_frame, text=('Search by account number or name'), bg='cyan', font=("times of roman", 11, "bold")).grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=20,
                                                                                                          pady=10)

        searchentry = Entry(details_frame, textvariable=self.search_txt,fg='black', font=('times new roman', 12, 'bold'), bd=4)
        searchentry.grid(row=0, column=4, padx=20, pady=10)

        searchbutton = Button(details_frame, text='search', width=5, cursor='hand2',command=search_data).grid(row=0, column=5, padx=8,
                                                                                              pady=10)
        showallbutton = Button(details_frame, text='showall', width=5, cursor='hand2',command=data).grid(row=0, column=6,
                                                                                                padx=20, pady=10)
        # *************************** table frame ********************
        table_frame = Frame(details_frame, bg='white', bd=4, relief=RIDGE)
        table_frame.place(x=15, y=65, width=710, height=410)
        self.scrool_x = Scrollbar(table_frame, orient=HORIZONTAL)
        self.scrool_y = Scrollbar(table_frame, orient=VERTICAL)
        self.ac_table = ttk.Treeview(table_frame, columns=(
            'account number', 'date', 'name', 'magil shillk', 'karj', 'yene vyaj', 'jama karj ', 'jama vyaj', 'shillk'),
                                         xscrollcommand=self.scrool_x.set, yscrollcommand=self.scrool_y.set)
        self.scrool_x.pack(side=BOTTOM, fill=X)
        self.scrool_y.pack(side=RIGHT, fill=Y)
        self.scrool_x.config(command=self.ac_table.xview)
        self.scrool_y.config(command=self.ac_table.yview)
        self.ac_table.heading('account number', text='ac no')
        self.ac_table.heading('date', text='date')
        self.ac_table.heading('name', text='holder name')
        self.ac_table.heading('magil shillk', text='magil shillk')
        self.ac_table.heading('karj', text='karj')
        self.ac_table.heading('yene vyaj', text='yene vyaj')
        self.ac_table.heading('jama karj ', text='jama karj ')
        self.ac_table.heading('jama vyaj', text='jama vyaj')
        self.ac_table.heading('shillk', text='shillk')
        self.ac_table['show'] = 'headings'
        self.ac_table.column('account number', width=50)
        self.ac_table.column('date', width=130)
        self.ac_table.column('name', width=170)
        self.ac_table.column('magil shillk', width=130)
        self.ac_table.column('karj', width=80)
        self.ac_table.column('yene vyaj', width=100)
        self.ac_table.column('jama karj ', width=100)
        self.ac_table.column('jama vyaj', width=100)
        self.ac_table.column('shillk', width=100)
        self.ac_table.bind("<ButtonRelease-1>",get_cursor)

        self.ac_table.pack(fill=BOTH, expand=1)


        fetch_data(self)

        clear()

root=Tk()
obj=Login()
root.mainloop()
