#Importing tkinter libary and creating a GUI window

from tkinter import *
from _ast import Lambda
import sqlite3
from tkinter import messagebox
root = Tk()

root.configure(bg='black')
root.title('Calculator')
root.iconbitmap('cc.ico')


#Creating a Enrty window to enter our numbers.
e = Entry(root, width=15, borderwidth=5, font=('Arial bold', 30))
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

conn = sqlite3.connect('calculator.db')
c = conn.cursor()

# #creating datbase



# c.execute(""" CREATE TABLE addresses(
#       numbers integers
#
# ) """)
#
# conn.commit()
# conn.close()

# def submit():
#     conn=sqlite3.connect("calculator.db")
#     c=conn.cursor()
#     c.execute("INSERT INTO addresses VALUES (:numbers)", {
#
#         'numbers': e.get(),
#
#     })
#     # print('Address inserted successfully')
#     messagebox.showinfo('Addresses','Inserted Successfully')
#
#     conn.commit()
#     conn.close()
#
#     e.delete(0,END)
#



#Creating functions.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Button_num(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_square():
    global math
    global f_num
    first_number = e.get()
    f_num = int(first_number)
    math = "square"
    current = e.get()
    e.delete(0, END)
    e.insert(0, int(current) ^ int(first_number))

def button_mod():
    first_number = e.get()
    global f_num
    global math
    math = "mod"
    f_num = float(first_number)
    e.delete(0, END)

def button_plusminus():
    first_number = e.get()
    global f_num
    global math
    math = "plusminus"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "square":
        e.insert(0, f_num ** int(2))
    if math == "mod":
        e.insert(0, f_num % float(second_number))
    if math == "plusminus":
        e.insert(0, f_num - float(second_number))
    conn = sqlite3.connect("calculator.db")
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:numbers)", {

        'numbers': e.get(),

    })
    # print('Address inserted successfully')
    messagebox.showinfo('Addresses', 'Inserted Successfully')

    conn.commit()
    conn.close()

    e.delete(0, END)

def button_delete():
    current = e.get()
    lenght = len(current) - 1
    e.delete(lenght, END)


def button_exit():
    root.destroy()

def query():
    global root1
    root1=Toplevel()
    root1.title("History")
    root1.geometry("400x400")
    root1.iconbitmap("hi.ico")
    # root.configure(bg="black")
    Button(root1, text="Clear All",bg="red",fg="white",command=delete).place(x=180, y=360)




    # Create a databases or connect to one
    conn = sqlite3.connect('calculator.db')
    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record+=str(record[1])+' )'+str(record[0])+'\n'
    Label(root1,text=print_record).grid(row=8,column=0,columnspan=2)






    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('calculator.db')
    c = conn.cursor()
    c.execute('DELETE from addresses;')
    print("Deleted successfully")
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record[1]) + ' )' + str(record[0]) + '\n'
    Label(root1, text=print_record).grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()
    root1.destroy()



#Creating buttons widgets for our calculator.
Button(root, text="<--", padx=35, pady=15, command=button_delete, border="4", bg='white').grid(row=1, column=3, )
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), border="4", bg='black',fg='white', font=('Arial bold', 10) )
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), border="4", bg='black',fg='white', font=('Arial bold', 10))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), border="4", bg='black',fg='white', font=('Arial bold', 10))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), border="4", bg='black',fg='white', font=('Arial bold', 10))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), border="4", bg='black',fg='white', font=('Arial bold', 10))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), border="4", bg='black',fg='white', font=('Arial bold', 10))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), border="4", bg='black',fg='white', font=('Arial bold', 10))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), border="4", bg='black',fg='white', font=('Arial bold', 10))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), border="4", bg='black',fg='white', font=('Arial bold', 10))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), border="4", bg='black',fg='white', font=('Arial bold', 10))
b_dot = Button(root, text='.', padx=40, pady=20, command=lambda: Button_num("."), border="4",bg='white' , font=('Arial bold', 10))
b_add = Button(root, text="+", padx=39, pady=20, command=button_add, border="4", bg='white', font=('Arial bold', 10))
b_sub = Button(root, text="━", padx=35, pady=20, command=button_sub, border="4", bg='white', font=('Arial bold', 10))
b_mul = Button(root, text="x", padx=39, pady=20, command=button_mul, border="4", bg='white', font=('Arial bold', 10))
b_div = Button(root, text="/", padx=39, pady=20, command=button_div, border="4", bg='white', font=('Arial bold', 10))
b_mod = Button(root, text="MOD", padx=30, pady=20, command=button_mod, border="4", bg='white')
button_plusminus = Button(root, text="+/-", padx=36, pady=20, command=button_div, border="4", bg='white', font=('Arial bold', 10))
b_history=Button(root, text='History', padx=27, pady=10, border="4",bg='white' , font=('Arial bold', 10),command=query)
b_square = Button(root, text="x²", padx=40, pady=20, command=button_square, border="4", bg='white', font=('Arial bold', 10))
b_equal = Button(root, text="=", padx=30, pady=9, command=button_equal, border="4", bg='orange',fg='white', font=('Arial bold', 18))
b_clear = Button(root, text="C", padx=40, pady=20, command=button_clear, border="4", bg='white',fg='red',font=('Arial bold', 10))
b_exit = Button(root, text="Exit", padx=45, pady=10, command=button_exit, border="4", bg='red', fg='white', font=('Arial bold', 10))


#displaying all Button widget using grid method.
b1.grid(row=5, column=0, padx=5, pady=10)
b2.grid(row=5, column=1, padx=5, pady=10)
b3.grid(row=5, column=2, padx=5, pady=10)
b4.grid(row=4, column=0, padx=5, pady=10)
b5.grid(row=4, column=1, padx=5, pady=10)
b6.grid(row=4, column=2, padx=5, pady=10)
b7.grid(row=3, column=0, padx=5, pady=10)
b8.grid(row=3, column=1, padx=5, pady=10)
b9.grid(row=3, column=2, padx=5, pady=10)
b0.grid(row=6, column=1, padx=5, pady=10)
b_dot.grid(row=6, column=2, padx=5, pady=10)
b_add.grid(row=5, column=3)
b_sub.grid(row=4, column=3)
b_mul.grid(row=3, column=3)
b_div.grid(row=2, column=3)
b_mod.grid(row=2, column=1)
button_plusminus.grid(row=2, column=2)
b_square.grid(row=6, column=0)
b_clear.grid(row=2, column=0)
b_equal.grid(row=6, column=3)
b_exit.grid(row=7, column=1, columnspan=2, padx=5, pady=10)
b_history.grid(row=7, column=0)


root.mainloop()
