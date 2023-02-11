import sqlite3
import tkinter
import tkinter as tk
from tkinter import messagebox as mb
try:
    cnt=sqlite3.connect('shop.db')
    print("opened database successfully!")
except:
    print("Error!")

#-------------------create users table-----------------------------
# query='''CREATE TABLE users
#     (ID INTEGER PRIMARY KEY,
#     user CHAR(25) NOT NULL,
#     password CHAR(25) NOT NULL,
#     addr CHAR(50) NOT NULL
#     )'''
# cnt.execute(query)
# cnt.close()

#-------------------insert date to users table----------------------

# query='''INSERT INTO users (user,password,addr)
#     VALUES ("admin","123456789","rasht")'''
# cnt.execute(query)
# cnt.commit()
# cnt.close()
#-----------------------functions----------------------------
def login():
    user=txt_user.get()
    pas=txt_pass.get()
    
    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    
    btn_login.configure(state="disabled")
    lbl_msg.configure(text="welcome to your account!",fg="blue")
    btn_logout.configure(state="disabled")
    btn_delete.configure(state="normal")
#----------------------------------------------------    
def submit():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
#-------win2-------
    win2=tkinter.Toplevel(win)
    win2.geometry("300x300")
    win2.configure(bg="pink", height='300px', width='300px', cursor="wait")
    
    lbl_user2=tkinter.Label(win2,text="username: ")
    lbl_user2.pack()

    txt_user2=tkinter.Entry(win2,width=15)
    txt_user2.pack()

    lbl_pass2=tkinter.Label(win2,text="password: ")
    lbl_pass2.pack()

    txt_pass2=tkinter.Entry(win2,width=15)
    txt_pass2.pack()

    lbl_addr=tkinter.Label(win2,text="address: ")
    lbl_addr.pack()

    txt_addr=tkinter.Entry(win2,width=15)
    txt_addr.pack()

    lbl_msg2=tkinter.Label(win2,text="")
    lbl_msg2.pack()

    btn_second_sub=tkinter.Button(win2,text="Submit",command=second_sub)
    btn_second_sub.pack(pady=5)
    
    win2.mainloop()
#----------------------------------------
def second_sub():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    
    user2=txt_user2.get()
    pas2=txt_pass2.get()
    addr=txt_addr.get()
    
    query1='''SELECT id FROM users WHERE user=?'''
    result=cnt.execute(query1,(user2,))
    rows=result.fetchall()
        
    if(len(rows)!=0):
        lbl_msg2.configure(text="This username is already taken!!",fg="red")
        return
    
    if(len(user2)==0):
        lbl_msg2.configure(text="user field is blank!",fg="red")
        return
    
    if(len(pas2)==0):
        lbl_msg2.configure(text="password field is blank!",fg="red")
        return
    
    if(len(pas2)<8):
        lbl_msg2.configure(text="password length should be at least 8 chars!!",fg="red")
        return
    
    if(len(addr)==0):
        lbl_msg2.configure(text="address field is blank!",fg="red")
        return
    
    
    
    query2='''INSERT INTO users(user,password,addr)
        VALUES(?,?,?)'''
    cnt.execute(query2,(user2,pas2,addr))
    cnt.commit()
    # cnt.close()
    # btn_submit.configure(state="disabled")
    lbl_msg2.configure(text="submit done!!",fg="blue")
#----------------------------------------------------    

def delete():
    user=txt_user.get()
    pas=txt_pass.get()
    
    btn_delete.configure(state="disable")
    btn_logout.configure(state="disable")
    btn_login.configure(state="normal")

    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    
    if(len(rows)==0):
        lbl_msg.configure(text="This account does not exist!check user or pass!",fg="red")
        return
    
    
    if mb.askyesno('Delete account', 'Are U sure?'):
            mb.showwarning('Yes','click ok if you are totally sure')
            query='''SELECT id FROM  users WHERE user=? AND password=?'''
            result=cnt.execute(query,(user,pas))
            rows=result.fetchall()

            if(len(rows)!=0):
                query2='''Delete FROM users WHERE user=? AND password=?'''
                cnt.execute(query2,(user,pas))
                cnt.commit()
                lbl_msg.configure(text="Your account deleted successfully!!",fg="blue")
    else:
            mb.showinfo('No', 'Delete has been cancelled')
            lbl_msg.configure(text="delete canceled by user!!",fg="red")
  
    tk.mainloop()
#---------------------------------------------

def logout():
    user3=txt_user.get()
    pas3=txt_pass.get()
    
    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user3,pas3))
    rows=result.fetchall()
    
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    
    else:
        
        btn_login.configure(state="normal")
        lbl_msg.configure(text="logout done!",fg="blue")
        btn_logout.configure(state="disable")
#------------------------Main---------------------------------
    
win=tkinter.Tk()
win.geometry("400x300")
win.configure(bg="light blue", height='300px', width='300px', cursor="wait")

lbl_user=tkinter.Label(text="username: ")
lbl_user.pack()

txt_user=tkinter.Entry(width=25)
txt_user.pack()

lbl_pass=tkinter.Label(text="password: ")
lbl_pass.pack()

txt_pass=tkinter.Entry(width=25)
txt_pass.pack()

lbl_msg=tkinter.Label(text="")
lbl_msg.pack()

btn_login=tkinter.Button(text="Login",command=login)
btn_login.pack(pady=5)

btn_submit=tkinter.Button(text="Submit",command=submit)
btn_submit.pack(pady=5)

btn_delete=tkinter.Button(text="Delete",command=delete)
btn_delete.pack(pady=5)
btn_delete.configure(state="disabled")


btn_logout=tkinter.Button(text="logout",command=logout)
btn_logout.pack(pady=5)

win.mainloop()