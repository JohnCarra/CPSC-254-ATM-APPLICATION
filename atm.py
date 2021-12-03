import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import random
 
current_balance = 1000
 
class SampleApp(tk.Tk):
 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
 
        self.shared_data = {'Balance':tk.IntVar()}
 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
 
        self.frames = {}
        for F in (StartPage, NewAccountPage, MessagePage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
 
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame("StartPage")
 
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
 
 
class StartPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
        self.controller.title('XM2 Reginleif Banking')
        self.controller.state()
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('times new roman',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        space_label = tk.Label(self,height=4,bg='#5c3d3d')
        space_label.pack()
 
        username_label = tk.Label(self,
                                                      text='User Name: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        username_label.pack(pady=10)
 
        username = tk.StringVar()
        username_box = tk.Entry(self, 
                                                      textvariable=username,
                                                      font=('orbitron',12),
                                                      width=25)
 
        username_box.focus_set()
        username_box.pack(ipady=7)
 
        password_label = tk.Label(self,
                                                      text='Password: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        password_label.pack(pady=10)
 
        password_number = tk.StringVar()
        password_box = tk.Entry(self, 
                                                      textvariable=password_number,
                                                      font=('orbitron',12),
                                                      width=25)
 
        password_box.focus_set()
        password_box.pack(ipady=7)
        password_box.config(show="*")


        def new_account():
            controller.show_frame('NewAccountPage')
 
 
 
        space_label = tk.Label(self,height=4,bg='#5c3d3d')
        space_label.pack()

        def login_validation():
            username = username_box.get()
            password_number = password_box.get()
 
            msg = ''
 
            if len(username) == 0:
                msg = 'Username can\'t be empty'
                messagebox.showinfo('Error!', msg)
            elif len(password_number) == 0:
                msg = msg = 'Password can\'t be empty'
                messagebox.showinfo('Error!', msg) 
            else:
                try:
                    controller.show_frame('MenuPage')
 
                except Exception as ep:
                    messagebox.showerror('Error!', ep)
 
        incorrect_password_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        fg='white',
                                                                        bg='#5c3d3d',
                                                                        anchor='n')
 
        login_button = tk.Button(self,
                                                     text='Login',
                                                     command=login_validation,
                                                     font=('orbitron', 20, 'bold'),
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=15,
                                                     height=2,
                                                     anchor='n')
        login_button.pack(pady=10)
 
        createAccount_button = tk.Button(self,
                                                     text='Create New Account',
                                                     command=new_account,
                                                     font=('orbitron', 20, 'bold'),
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=20,
                                                     height=2,
                                                     anchor='n')
        createAccount_button.pack(pady=10)
 
        incorrect_password_label.pack(fill='both',expand=True)
 
 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
 
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
 
        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
 
        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
 
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
 
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
 
        tick()
 
 
 
 
 
class NewAccountPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('times new roman',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        new_account_label = tk.Label(self,
                                                           text='Create New Account',
                                                           font=('orbitron',20, 'bold'),
                                                           fg='white',
                                                           bg='#5c3d3d')
        new_account_label.pack()
 
 
        firstname_label = tk.Label(self,
                                                      text='First Name: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        firstname_label.pack(pady=10)
 
        firstname = tk.StringVar()
        firstname_box = tk.Entry(self, 
                                                      textvariable=firstname,
                                                      font=('orbitron',12),
                                                      width=25)
 
        firstname_box.focus_set()
        firstname_box.pack(ipady=7)
 
        lastname_label = tk.Label(self,
                                                      text='Last Name: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        lastname_label.pack(pady=10)
 
        lastname = tk.StringVar()
        lastname_box = tk.Entry(self, 
                                                      textvariable=lastname,
                                                      font=('orbitron',12),
                                                      width=25)
 
        lastname_box.focus_set()
        lastname_box.pack(ipady=7)
 
 
        cnicnum_label = tk.Label(self,
                                                      text='9-Digit SSN: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        cnicnum_label.pack(pady=10)
 
        cnic_number = tk.StringVar()
        cnicnum_box = tk.Entry(self, 
                                                      textvariable=cnic_number,
                                                      font=('orbitron',12),
                                                      width=25)
 
        cnicnum_box.focus_set()
        cnicnum_box.pack(ipady=7)
 
        username_label = tk.Label(self,
                                                      text='User Name: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        username_label.pack(pady=10)
 
        username = tk.StringVar()
        username_box = tk.Entry(self, 
                                                      textvariable=username,
                                                      font=('orbitron',12),
                                                      width=25)
 
        username_box.focus_set()
        username_box.pack(ipady=7)
 
        password_label = tk.Label(self,
                                                      text='Password: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        password_label.pack(pady=10)
 
        password_number = tk.StringVar()
        password_box = tk.Entry(self, 
                                                      textvariable=password_number,
                                                      font=('orbitron',12),
                                                      width=25)
 
        password_box.focus_set()
        password_box.pack(ipady=7)
        password_box.config(show="*")
 
        retype_label = tk.Label(self,
                                                      text='Re-Type Password: ',
                                                      font=('orbitron',15),
                                                      bg='#5c3d3d',
                                                      fg='white')
 
        retype_label.pack(pady=10)
 
        retype_number = tk.StringVar()
        retype_box = tk.Entry(self, 
                                                      textvariable=retype_number,
                                                      font=('orbitron',12),
                                                      width=25)
 
        retype_box.focus_set()
        retype_box.pack(ipady=7)
        retype_box.config(show="*")
 
        def validation():
            name = firstname_box.get()
            ssn = cnicnum_box.get()
            lastname = lastname_box.get()
            username = username_box.get()
            passWord = password_box.get()
            retypePass = retype_box.get()
 
            msg = ''
 
            if len(name) == 0:
                msg = 'Firstname can\'t be empty'
                messagebox.showinfo('Error!', msg)
            elif len(lastname) == 0:
                msg = msg = 'Lastname can\'t be empty'
                messagebox.showinfo('Error!', msg) 
            elif len(ssn) == 0:
                msg = msg = 'SSN can\'t be empty'
                messagebox.showinfo('Error!', msg)
            elif any(ch.isalpha() for ch in ssn):
                msg = 'SSN can\'t have letters' 
                messagebox.showinfo('Error!', msg)
            elif len(username) == 0:
                msg = msg = 'Username can\'t be empty'
                messagebox.showinfo('Error!', msg)
            elif len(passWord) == 0:
                msg = msg = 'Password can\'t be empty'
                messagebox.showinfo('Error!', msg) 
            elif len(retypePass) == 0:
                msg = msg = 'Re-Type Password can\'t be empty'
                messagebox.showinfo('Error!', msg)
            elif any(ch.isdigit() for ch in name):
                msg = 'First Name can\'t have numbers'
                messagebox.showinfo('Error!', msg)
            elif any(ch.isdigit() for ch in lastname):
                msg = 'Last name can\'t have numbers'
                messagebox.showinfo('Error!', msg)   
            elif len(name) <= 2:
                msg = 'name is too short.'
                messagebox.showinfo('Error!', msg)
            elif len(lastname) <= 2:
                msg = 'name is too short.'
                messagebox.showinfo('Error!', msg)
            elif len(name) > 100:
                msg = 'name is too long.'
                messagebox.showinfo('Error!', msg)
            elif len(lastname) > 100:
                msg = 'name is too long.'
                messagebox.showinfo('Error!', msg)
            elif len(ssn) <= 8:
                msg = 'SSN is too short.'
                messagebox.showinfo('Error!', msg)
            elif len(ssn) > 9:
                msg = 'SSN is too long.'
                messagebox.showinfo('Error!', msg)
            elif len(passWord) != len(retypePass):
                msg = 'Passwords must match.'
                messagebox.showinfo('Error!', msg)
            else:
                try:
                    controller.show_frame('MessagePage')
                except Exception as ep:
                    messagebox.showerror('Error!', ep)
 
 
 
        done_button = tk.Button(self,
                                                     text='Done',
                                                     command=validation,
                                                     font=('orbitron', 15, 'bold'),
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=20,
                                                     height=3,
                                                     anchor='n')
        done_button.pack(pady=10)
 
 
        def exit():
            controller.show_frame('StartPage')
 
        exit_button = tk.Button(self,
                                                     text='Exit',
                                                     command=exit,
                                                     font=('orbitron', 15, 'bold'),
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=20,
                                                     height=3,
                                                     anchor='n')
        exit_button.pack(pady=10)
 
 
class MessagePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('times new roman',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        space_label = tk.Label(self,height=4,bg='#5c3d3d')
        space_label.pack()
 
        randomNumber = random.randint(10000,99999)
 
        message_label = tk.Label(self,
                                                           text='Congratulations! Your account is created successfully. Your account number is ' + str(randomNumber) + '.',
                                                           font=('orbitron', 22, 'bold', 'italic'),
                                                           fg='white',
                                                           bg='#5c3d3d',
                                                           anchor='w')
        message_label.pack(fill='x')
 
        space_label = tk.Label(self,height=4,bg='#5c3d3d')
        space_label.pack()
 
        def exit():
            controller.show_frame('StartPage')
 
        exit_button = tk.Button(self,
                                                     text='Exit',
                                                     command=exit,
                                                     font=('orbitron', 13, 'bold'),
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=10,
                                                     height=3,
                                                     anchor='n')
        exit_button.pack(pady=10)
 
 
 
 
 
class MenuPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('times new roman',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('orbitron',20, 'bold'),
                                                           fg='white',
                                                           bg='#5c3d3d')
        main_menu_label.pack()
 
        selection_label = tk.Label(self,
                                                           text='Please make a selection',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#5c3d3d',
                                                           anchor='w')
        selection_label.pack(fill='x')
 
        button_frame = tk.Frame(self,bg='#5c3d3d')
        button_frame.pack(fill='both',expand=True)
 
        def withdraw():
            controller.show_frame('WithdrawPage')
 
        withdraw_button = tk.Button(button_frame,
                                                            text='Withdraw',
                                                            command=withdraw,
                                                            font=('orbitron', 15, 'bold'),
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        withdraw_button.grid(row=0,column=0,pady=5)
 
        def deposit():
            controller.show_frame('DepositPage')
 
        deposit_button = tk.Button(button_frame,
                                                            text='Deposit',
                                                            command=deposit,
                                                            font=('orbitron', 15, 'bold'),
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        deposit_button.grid(row=1,column=0,pady=5)
 
        def balance():
            controller.show_frame('BalancePage')
 
        balance_button = tk.Button(button_frame,
                                                            text='Balance',
                                                            command=balance,
                                                            font=('orbitron', 15, 'bold'),
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        balance_button.grid(row=2,column=0,pady=5)
 
        def exit():
            controller.show_frame('StartPage')
 
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            font=('orbitron', 15, 'bold'),
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        exit_button.grid(row=3,column=0,pady=5)
 
 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
 
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
 
        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
 
        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
 
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
 
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
 
        tick()
 
 
class WithdrawPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BABKING',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        choose_amount_label = tk.Label(self,
                                                           text='Choose the amount you want to withdraw',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#5c3d3d')
        choose_amount_label.pack()
 
        button_frame = tk.Frame(self,bg='#5c3d3d')
        button_frame.pack(fill='both',expand=True)
 
        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
 
        twenty_button = tk.Button(button_frame,
                                                       text='20',
                                                       command=lambda:withdraw(20),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        twenty_button.grid(row=0,column=0,pady=5)
 
        forty_button = tk.Button(button_frame,
                                                       text='40',
                                                       command=lambda:withdraw(40),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        forty_button.grid(row=1,column=0,pady=5)
 
        sixty_button = tk.Button(button_frame,
                                                       text='60',
                                                       command=lambda:withdraw(60),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        sixty_button.grid(row=2,column=0,pady=5)
 
        eighty_button = tk.Button(button_frame,
                                                       text='80',
                                                       command=lambda:withdraw(80),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        eighty_button.grid(row=3,column=0,pady=5)
 
        one_hundred_button = tk.Button(button_frame,
                                                       text='100',
                                                       command=lambda:withdraw(100),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=555)
 
        two_hundred_button = tk.Button(button_frame,
                                                       text='200',
                                                       command=lambda:withdraw(200),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        two_hundred_button.grid(row=1,column=1,pady=5)
 
        three_hundred_button = tk.Button(button_frame,
                                                       text='300',
                                                       command=lambda:withdraw(300),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        three_hundred_button.grid(row=2,column=1,pady=5)
 
        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                                              textvariable=cash,
                                                              width=59,
                                                              justify='right')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=30)
 
        def other_amount(_):
            global current_balance
            current_balance -= float(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
 
        other_amount_entry.bind('<Return>',other_amount)
 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
 
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
 
        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
 
        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
 
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
 
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
 
        tick()
 
 
class DepositPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        space_label = tk.Label(self,height=4,bg='#5c3d3d')
        space_label.pack()
 
        enter_amount_label = tk.Label(self,
                                                      text='Enter amount',
                                                      font=('orbitron',13),
                                                      bg='#5c3d3d',
                                                      fg='white')
        enter_amount_label.pack(pady=10)
 
        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        deposit_entry.pack(ipady=7)
 
        def deposit_cash():
            global current_balance
            current_balance += float(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
 
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=deposit_cash,
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=10)
 
        two_tone_label = tk.Label(self,bg='#5c3d3d')
        two_tone_label.pack(fill='both',expand=True)
 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
 
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
 
        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
 
        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
 
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
 
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
 
        tick()
 
 
class BalancePage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#5c3d3d')
        self.controller = controller
 
 
        heading_label = tk.Label(self,
                                                     text='XM2 REGINLEIF BANKING',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#5c3d3d')
        heading_label.pack(pady=25)
 
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('orbitron',13),
                                                  fg='white',
                                                  bg='#5c3d3d',
                                                  anchor='w')
        balance_label.pack(fill='x')
 
        button_frame = tk.Frame(self,bg='#5c3d3d')
        button_frame.pack(fill='both',expand=True)
 
        def menu():
            controller.show_frame('MenuPage')
 
        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        menu_button.grid(row=0,column=0,pady=5)
 
        def exit():
            controller.show_frame('StartPage')
 
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=50,
                                                 height=5)
        exit_button.grid(row=1,column=0,pady=5)
 
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
 
        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo
 
        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo
 
        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo
 
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
 
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
 
        tick()
 
 
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()