from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from PIL import Image,ImageTk


mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Bhavy1344#",
    database="airport"
)
mycur = mydb.cursor()

root = tkinter.Tk()
root.title("AIRPORT RESERVATION SYSTEM")
root.geometry("1550x800+0+0")

bg=ImageTk.PhotoImage(file="images/airport_logo.jpg")
lbl_bg=Label(root,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(root,bg='light green')
frame.place(x=610,y=170,width=340,height=450)


#label
username=Label(frame,text='USERID',font=('times new roman',15,'bold'),fg='black')
username.place(x=110,y=30)

txtuser=ttk.Entry(frame,font=('times new roman',15,'bold'))
txtuser.place(x=40,y=75,width=270)

password=Label(frame,text='PASSWORD',font=('times new roman',15,'bold'),fg='black')
password.place(x=110,y=130)

txtpass=ttk.Entry(frame,font=('times new roman',15,'bold'))
txtpass.place(x=40,y=175,width=270)
txtpass=ttk.Entry(frame,font=('times new roman',15,'bold'),show='*')
txtpass.place(x=40,y=175,width=270)

def loginuser(value):

    if value == 1:
        mycur = mydb.cursor()
        uid = txtuser.get()
        password = txtpass.get()

        sql = "select * from emplogin where e_id=%s and e_pass=%s"
        mycur.execute(sql, [uid, password])
        res = mycur.fetchall()
        if res:
            messagebox.showinfo("Success login", "Employee login successful")
            openemp(uid)

        else:
            messagebox.showinfo("Failure", "Incorrect credentials")

    elif value == 2:
        mycur1 = mydb.cursor()
        uid = txtuser.get()
        password = txtpass.get()

        sql = "select * from custlogin where c_id=%s and c_pass=%s"
        mycur1.execute(sql, [uid, password])
        res = mycur1.fetchall()
        if res:
            messagebox.showinfo("Success login", "Customer login successful")
            opencust(uid)

        else:
            messagebox.showinfo("Failure", "Incorrect credentials")
    else:
        messagebox.showwarning("", "Something is missing\nTry Again")


v = IntVar()
#radiobuttons
emp_rdiobtn1=Radiobutton(frame, text="Employee", variable=v, value=1,font=("arial",10,"bold"),fg="green",bg="light green",activeforeground="white")
emp_rdiobtn1.place(x=70,y=220)

emp_rdiobtn2=Radiobutton(frame, text="Customer", variable=v, value=2,font=("arial",10,"bold"),fg="green",bg="light green",activeforeground="white")
emp_rdiobtn2.place(x=200,y=220)

#login button
loginbtn=Button(frame,text='Login',command=lambda: loginuser(v.get()),font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
loginbtn.place(x=110,y=270,width=140,height=35)

#register button
registerbtn=Button(frame,text='Register',font=('times new roman',13,'bold'),borderwidth=0,fg='white',bg='light green',activeforeground='white',activebackground='light green')
registerbtn.place(x=110,y=310,width=160)
#forgot password
forgotbtn=Button(frame,text='Forgot Password',font=('times new roman',13,'bold'),borderwidth=0,fg='white',bg='light green',activeforeground='white',activebackground='light green')
forgotbtn.place(x=110,y=340,width=160)


def newCust(value):

    #Employee adding new customer
    mycur = mydb.cursor()
    newcust = tkinter.Tk()
    newcust.title('Add Customer')
    newcust.geometry("510x320+520+420")

    root1=Frame(newcust,bg="black")
    root1.place(x=0,y=0,width=510,height=320)

    Label(root1, text="Name",font=("arial",14,"bold"),fg="white",bg="black").place(x=50,y=50)
    Label(root1, text="Id",font=("arial",14,"bold"),fg="white",bg="black").place(x=50,y=90)
    Label(root1, text="DOB",font=("arial",14,"bold"),fg="white",bg="black").place(x=50,y=130)
    Label(root1, text="Password",font=("arial",14,"bold"),fg="white",bg="black").place(x=50,y=170)    

    custname = ttk.Entry(root1,font=("arial",15,"bold"))
    custname.place(x=250,y=50)
    custid = Entry(root1,font=("arial",15,"bold"))
    custid.place(x=250,y=90)
    custdob = ttk.Entry(root1,font=("arial",15,"bold"))
    custdob.place(x=250,y=130)
    custpass=ttk.Entry(root1,font=("arial",15,"bold"))
    custpass.place(x=250,y=170)


    def addcust():
        
        mycur.execute("insert into Customer(c_name, c_id, c_dob,e_id) values(%s,%s,%s,%s)",
                      (custname.get(), custid.get(), custdob.get(),value)
                      )
        mycur.execute("insert into custlogin(c_Id, c_Pass) values(%s,%s)", (custid.get(), custpass.get()))
        mydb.commit()
        messagebox.showinfo("Customer", "Customer Added successfully")
        newcust.destroy()

    def delcust():
        mycur.execute("delete from custlogin where c_ID = %s", [custid.get()])
        mycur.execute("delete from customer where c_ID = %s", [custid.get()])
        mydb.commit()
        messagebox.showinfo("Customer", "Customer Removed")
        newcust.destroy()

    Button(root1, text="ADD", command=addcust,font=("arial",12,"bold"),relief=RIDGE,fg="white",bg="green").place(x=50,y=220)
    Button(root1, text="DELETE", command=delcust,font=("arial",12,"bold"),relief=RIDGE,fg="white",bg="red").place(x=250,y=220)


def openemp(val):

    #Employee window
    root.destroy()
    emp = tkinter.Tk()
    emp.title("Employee")
    emp.geometry("1550x800+0+0")
    
    frame2 = Frame(emp, bg="sky blue")
    frame2.place(x=100,y=50, width=1150, height=600)

    Label(frame2, text="INFORMATION", font=("arial",30,"bold"), fg="black").place(x=450, y=20)
    
    mycur1 = mydb.cursor()
    sql1 = "select e_Name,e_Id,e_exp,e_sal from Employee where e_Id=%s"
    mycur1.execute(sql1, [val])
    res1 = mycur1.fetchall()
    
    dres = ''
    for rec in res1[0]:
        dres += " || " + str(rec)

    Label(frame2, text=dres+"||" ,fg="black",font=("arial",20,"bold")).place(x=460,y=80)
    ttk.Separator(frame2, orient='horizontal').place(y=70, relwidth=1)
    
    custbtn=Button(frame2,text="Add Customer", command= lambda: newCust(val),font=("arial",12,"bold"),
                   relief=RIDGE,fg="black",bg="light blue")
    custbtn.place(x=500,y=140)

def opencust(val):
    #Customer window
    root.destroy()
    cust = tkinter.Tk()
    cust.geometry("1550x800+0+0")
    cust.title("Customer")
    root2 = Frame(cust, bg="sky blue")
    root2.place(x=100,y=50, width=1150, height=600)

    Label(root2, text="Welcome", font=("arial",30,"bold"), fg="black").place(x=530, y=20)
    mycur1 = mydb.cursor()
    sql1 = "select c_Name,c_Id from Customer where c_Id=%s"
    mycur1.execute(sql1, [val])
    res1 = mycur1.fetchall()
    dres = ''
    for rec in res1[0]:
        dres += "||" + str(rec)

    Label(root2, text=dres + "||", fg="black", font=("arial", 20, "bold")).place(x=540, y=80)
    custbtn = Button(root2, text="Book Tickets",command= lambda : booktick(val), font=("arial", 12, "bold"),
                     relief=RIDGE, fg="white", bg="blue")
    custbtn.place(x=550, y=140)
    updbtn = Button(root2, text="Update Profile",command=lambda: updatecust(val), font=("arial", 12, "bold"),
                    relief=RIDGE, fg="white", bg="blue")
    updbtn.place(x=550, y=200)

    ttk.Separator(root2, orient='horizontal').place(y=70, relwidth=1)

def booktick(val):
    #Ticket window
    mycur = mydb.cursor()
    bookwin = tkinter.Tk()
    bookwin.geometry("532x442+325+308")
    bookwin.title("Book Tickets")

    frame1=Frame(bookwin,bg="blue")
    frame1.place(x=0,y=0,width=532,height=442)
    
    tNo=Label(frame1, text="Ticket No",font=("arial",14,"bold"),fg="white",bg="blue")
    tNo.place(x=50,y=90)
    Label(frame1, text="Source",font=("arial",14,"bold"),fg="white",bg="blue").place(x=50,y=130)
    Label(frame1, text="Destination",font=("arial",14,"bold"),fg="white",bg="blue").place(x=50,y=170)
    Label(frame1, text="Date",font=("arial",14,"bold"),fg="white",bg="blue").place(x=50,y=210)

    tid = IntVar(tNo, id(tNo))
    t_no =ttk.Entry(frame1,font=("arial",15,"bold"), textvariable=tid)
    t_no.place(x=250,y=90)
    t_source =ttk.Entry(frame1,font=("arial",15,"bold"))
    t_source.place(x=250,y=130)
    t_des = ttk.Entry(frame1,font=("arial",15,"bold"))
    t_des.place(x=250,y=170)
    t_date=ttk.Entry(frame1,font=("arial",15,"bold"))
    t_date.place(x=250,y=210)

    def book():
        mycur.execute("SELECT f_no FROM flight ORDER BY RAND() LIMIT 1")
        res = mycur.fetchone()

        mycur.execute("INSERT INTO ticket(t_no, t_source, t_des, t_date, c_id, f_no) "
                      "VALUES (%s, %s, %s, %s, %s, %s)",
                      (t_no.get(), t_source.get(), t_des.get(), t_date.get(), val, res[0]))
        mydb.commit()
        messagebox.showinfo("Book", "Ticket booked successfully")

        bookwin.destroy()



    def can():
#not executing issue eventid 
        if(t_no.get()!=''):
            mycur.execute("delete from ticket where t_no=%s",[t_no.get()])
            mydb.commit()
            messagebox.showinfo("Event", "Ticket Cancelled")


        else:
            messagebox.showinfo("Event", "Could not complete your request")

        bookwin.destroy()

    Button(frame1, text="BOOK", command=book,font=("arial",12,"bold"),relief=RIDGE,fg="white",bg="red").place(x=50,y=250)
    Button(frame1, text="CANCEL", command=can,font=("arial",12,"bold"),relief=RIDGE,fg="white",bg="red").place(x=250,y=250)
    

def updatecust(val):
    upcust = tkinter.Tk()
    upcust.title("Update Customer")
    upcust.geometry("532x442+325+308")

    frame3 = Frame(upcust, bg="sky blue")
    frame3.place(x=0, y=0, width=532, height=442)

    Label(frame3, text="Enter the values to be updated", font=("arial", 14, "bold"), fg="white",
          bg="grey").place(x=50, y=50)
    Label(frame3, text="Name", font=("arial", 14, "bold"), fg="white", bg="grey").place(x=50, y=90)
    Label(frame3, text="Password", font=("arial", 14, "bold"), fg="white", bg="grey").place(x=50, y=130)
    upName = ttk.Entry(frame3, font=("arial", 15, "bold"))
    upName.place(x=250, y=90)
    upPass = ttk.Entry(frame3, font=("arial", 15, "bold"))
    upPass.place(x=250, y=130)

    def update():
        if upName.get() != "":
            sql = "UPDATE Customer SET c_name = %s WHERE c_id = %s"
            mycur.execute(sql, (upName.get(), val))
            mydb.commit()

        if upPass.get() != "":
            sql = "UPDATE custLogin SET c_pass = %s WHERE c_id = %s"
            mycur.execute(sql, (upPass.get(), val))
            mydb.commit()

        upcust.destroy()
        messagebox.showinfo("Update", "Data have been succefully updated")

    Button(frame3, text="Update", command=update, font=("arial", 12, "bold"), relief=RIDGE, fg="white",
           bg="red").place(x=230, y=220)


root.mainloop()
