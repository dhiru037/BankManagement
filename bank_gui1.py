from tkinter import *
from tkinter import messagebox
#data
clientName = ['Dhiru Ram', 'Bharadwaj Pranav', 'Samar Pratap', 'Rodri Martinez', 'Kevin de Bruyne', 'Younis Khan', 'Idris Alba']
clientPins = ['0001','0002', '0003','0004','0005','0006','0007']
clientBalances = [7000,9000,10000,20000,150150010,250000,25250020]
clientDeposition = 0
clientWithdrawal = 0
clientBalance=0
global loanAct
loanAct=[]
global loanActpin
loanActpin = []
global loanAmtlist
loanAmtlist=[]
global loanAmt
loanAmt=0


#data


root = Tk()
root.geometry='700x700'

#new account window

def clients():

   new2 = Toplevel(root)
   new2.geometry("750x250")
   new2.title("CLient Details")




def account():
   global u
   u = 0
   global disk1
   disk1 = 1
   global disk2
   disk2 = len(clientName)
   new = Toplevel(root)
   new.geometry("750x500")
   new.title("New Account")

   label1 = Label(new, text="New client account", font=('Helvetica 17 bold'))
   label2 = Label(new, text="Please enter the name of client")
   name_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   #name=name_entry.get()
   label3 = Label(new, text="Please enter a PIN to secure your account")
   pin_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   #pin=pin_entry.get()
   label4 = Label(new, text="Please enter the amount of Money you wish to Deposit to start an Account")
   amount_entry = Entry(new,  font=('calibre', 10, 'normal'), width = 60)
   amount_entry.insert(0, 0)
   #amount=int(amount_entry.get())
   def value(a, b, c):
      x = a.get()
      y = b.get()
      z = int(c.get())
      clientName.append(x)
      clientPins.append(y)
      clientBalances.append(z)


   def passer():
      n = value(name_entry, pin_entry, amount_entry)
   def msg1():
      messagebox.showinfo("alert", "Your account details have been successfully entered")
   submitbutton= Button(new, text="Submit", command=lambda:[passer(), msg1()])










   label1.pack(padx = 30)
   label2.pack(pady=30)
   name_entry.pack()
   label3.pack(pady=30)
   pin_entry.pack()
   label4.pack(pady=30)
   amount_entry.pack()
   submitbutton.pack()


#withdraw money window

def withdraw():
   new2 = Toplevel(root)
   new2.geometry("750x500")
   new2.title("Withdraw money")

   label1 = Label(new2, text="Withdraw money from your account", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)


   ####################################################

   wlabel1 = Label(new2, text="Please enter the name of client")
   wname_entry = Entry(new2, font=('calibre', 10, 'normal'), width=60)
   wlabel2 = Label(new2, text="Please enter your PIN here")
   wpin_entry = Entry(new2, font=('calibre', 10, 'normal'), width=60)


   def wsubmit(a, b):
      wcounter = 0
      for i in range(len(clientName)):
         if clientName[i]==a and clientPins[i]==b:
            global withdrawcount
            withdrawcount = i

            withdrawmoney()
            wcounter +=1
      if wcounter < 1:
         messagebox.showerror("warning", "the client details don't match! please ensure that both the name and pin are correctly entered")
   wsubmitbutton= Button(new2, text = 'submit', command=lambda:wsubmit(wname_entry.get(), wpin_entry.get()))

   def withdrawmoney():
      new3 = Toplevel(root)
      new3.geometry("750x500")
      new3.title("Withdraw money")
      wlabel03 = Label(new3, text="Your current balance is INR "+str(clientBalances[withdrawcount]))
      wlabel3 = Label(new3, text="Please enter the amount you want to withdraw from your account")
      wamount_entry = Entry(new3, font=('calibre', 10, 'normal'), width=60)
      wamount_entry.insert(0, 0)

      def wpasser():
         if int(wamount_entry.get()) < clientBalances[withdrawcount]:
            clientBalances[withdrawcount] -= int(wamount_entry.get())
            messagebox.showinfo(title='success', message=f'Your withdrawal was successful.You now have INR {clientBalances[withdrawcount]} in your account')

         else:
            messagebox.showerror(title="Alert", message="You don't have enough money in your account to complete this transaction")

      wamount_submit = Button(new3, text = 'submit', command = wpasser)

      wlabel03.pack()
      wlabel3.pack()
      wamount_entry.pack()
      wamount_submit.pack()









   wlabel1.pack(pady = 30)
   wname_entry.pack()
   wlabel2.pack(pady = 30)
   wpin_entry.pack()
   wsubmitbutton.pack(pady= 30)



#deposit money window

def deposit():

      new3 = Toplevel(root)
      new3.geometry("750x500")
      new3.title("Deposit money")

      label1 = Label(new3, text="Deposit money into your account", font=('Helvetica 17 bold'))
      label1.pack(padx=30)

      ####################################################

      dlabel1 = Label(new3, text="Please enter the name of client")
      dname_entry = Entry(new3, font=('calibre', 10, 'normal'), width=60)
      dlabel2 = Label(new3, text="Please enter your PIN here")
      dpin_entry = Entry(new3, font=('calibre', 10, 'normal'), width=60)

      def dsubmit(a, b):
         dcounter = 0
         for i in range(len(clientName)):
            if clientName[i] == a and clientPins[i] == b:
               global depositcount
               depositcount = i

               depositmoney()
               dcounter += 1
         if dcounter < 1:
            messagebox.showerror("warning",
                                 "the client details don't match! please ensure that both the name and pin are correctly entered")

      dsubmitbutton = Button(new3, text='submit', command=lambda: dsubmit(dname_entry.get(), dpin_entry.get()))

      def depositmoney():
         new4 = Toplevel(root)
         new4.geometry("750x500")
         new4.title("Deposit money")
         dlabel01= Label(new4, text="Your current balance is INR "+str(clientBalances[depositcount]))
         dlabel3 = Label(new4, text="Please enter the amount you want to deposit into your account")
         damount_entry = Entry(new4, font=('calibre', 10, 'normal'), width=60)
         damount_entry.insert(0, 0)

         def dpasser():
            clientBalances[depositcount] += int(damount_entry.get())
            messagebox.showinfo(title='success', message=f"Your deposit was successful. You now have INR {clientBalances[depositcount]} in your account")
            #print(clientBalances[depositcount])
           # else:
           #    messagebox.showerror(title="Alert",
           #                         message="You don't have enough money in your account to complete this transaction")

         damount_submit = Button(new4, text='submit', command=dpasser)

         dlabel01.pack()
         dlabel3.pack()
         damount_entry.pack()
         damount_submit.pack()

      dlabel1.pack(pady=30)
      dname_entry.pack()
      dlabel2.pack(pady=30)
      dpin_entry.pack()
      dsubmitbutton.pack(pady=30)


#check balance window

def balance():
   new5 = Toplevel(root)
   new5.geometry("750x500")
   new5.title("Check Balance")

   label1 = Label(new5, text="Check your account balance", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)

   blabel1 = Label(new5, text="Please enter the name of client")
   bname_entry = Entry(new5, font=('calibre', 10, 'normal'), width=60)
   blabel2 = Label(new5, text="Please enter your PIN here")
   bpin_entry = Entry(new5, font=('calibre', 10, 'normal'), width=60)

   def bsubmit(a, b):
      bcounter = 0
      for i in range(len(clientName)):
         if clientName[i] == a and clientPins[i] == b:
            global balancecount
            balancecount = i

            messagebox.showinfo(title="Balance", message=f"Your account balance is INR {clientBalances[i]}")
            bcounter += 1
      if bcounter < 1:
         messagebox.showerror("warning",
                              "the client details don't match! please ensure that both the name and pin are correctly entered")

   bsubmitbutton = Button(new5, text='submit', command=lambda: bsubmit(bname_entry.get(), bpin_entry.get()))

   #blabel1.pack()
   #bamount_entry.pack()
   #bamount_submit.pack()


   blabel1.pack(pady=30)
   bname_entry.pack()
   blabel2.pack(pady=30)
   bpin_entry.pack()
   bsubmitbutton.pack(pady=30)





#loan window

def loan():

      new6 = Toplevel(root)
      new6.geometry("750x500")
      new6.title("Loan window")

      label1 = Label(new6, text="Apply for Loan", font=('Helvetica 17 bold'))
      label1.pack(padx=30)


      ####################################################

      llabel1 = Label(new6, text="Please enter the name of client")
      lname_entry = Entry(new6, font=('calibre', 10, 'normal'), width=60)
      llabel2 = Label(new6, text="Please enter your PIN here")
      lpin_entry = Entry(new6, font=('calibre', 10, 'normal'), width=60)


      def lsubmit(a, b):
         lcounter = 0
         for i in range(len(clientName)):
            if clientName[i] == a and clientPins[i] == b:
               global loancount
               loancount = i

               if clientName[loancount] in loanAct:
                   messagebox.showerror("alert","You have already applied for loan! Check loan status!")
                   lcounter+=1

               else:
                   loanmoney()
                   lcounter += 1
         if lcounter < 1:
            messagebox.showerror("warning",
                                 "the client details don't match! please ensure that both the name and pin are correctly entered")

      lsubmitbutton = Button(new6, text='submit', command=lambda: lsubmit(lname_entry.get(), lpin_entry.get()))

      def loanmoney():
         new7 = Toplevel(root)
         new7.geometry("750x500")
         new7.title("Loan Window")
         llabel01= Label(new7, text="Your current balance is INR "+str(clientBalances[loancount]))
         llabel3 = Label(new7, text="Please enter the amount you want to apply for loan")
         lamount_entry = Entry(new7, font=('calibre', 10, 'normal'), width=60)
         lamount_entry.insert(0, 0)

         loanAmt = int(lamount_entry.get())




         def lpasser():

            if int(lamount_entry.get())>20*clientBalances[loancount]:
                messagebox.showerror("Warning", "Loan amount exceeds limit")


            else:
                clientBalances[loancount] = clientBalances[loancount] + int(lamount_entry.get())


                loanAmt=int(lamount_entry.get())

                loanAct.append(clientName[loancount])

                loanActpin.append(clientPins[loancount])

                loanAmtlist.append(loanAmt)

                messagebox.showinfo(title='success', message=f"Your loan was approved! You now have INR {clientBalances[loancount]} in your account")




         lamount_submit = Button(new7, text='submit', command=lpasser)

         llabel01.pack()
         llabel3.pack()
         lamount_entry.pack()
         lamount_submit.pack()




      llabel1.pack(pady=30)
      lname_entry.pack()
      llabel2.pack(pady=30)
      lpin_entry.pack()
      lsubmitbutton.pack(pady=30)



   #label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))

#loan status window

def loans():
   new = Toplevel(root)
   new.geometry("750x250")
   new.title("New Window")

   label1 = Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold'))
   label1.pack(padx = 30)




#main buttons here


titlelabel = Label(root, text = "Welcome to PES banking system", font = ("Helvetica 17 bold", 30))
titlelabel.grid(row = 0, column = 1, pady = 20, padx = 10)
#button1
newaccount = Button(root, text = "Open a new client account", font = ("Helvetica 17 bold", 10), height = 5, command = account)
newaccount.grid(row = 1, column = 0,  pady = 20)
#button2
withdraw = Button(root, text = "Withdraw money from your account", font = ("Helvetica 17 bold", 10), height = 5, command = withdraw)
withdraw.grid(row = 1, column = 1,  pady = 20)
#button3
deposit = Button(root, text = "Deposit money in your account", font = ("Helvetica 17 bold", 10), height = 5, command = deposit)
deposit.grid(row = 1, column = 2, pady = 20)
#button4
checkbalance = Button(root, text = "Check your account balance", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = balance)
checkbalance.grid(row = 2, column = 0, padx = 70, pady = 20)
#button5
loan = Button(root, text = "loan window", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = loan)
loan.grid(row = 2, column = 1, padx = 70, pady = 20)
#button6
loanstatus = Button(root, text = "Check your loan status", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = loans)
loanstatus.grid(row = 2, column = 2,  pady = 20)
#button7
def quitter():
   root.destroy()
quitbank = Button(root, text = "Quit", font = ("Helvetica 17 bold", 10), height = 5, width = 30, command = quitter)
quitbank.grid(row = 3, column = 1, padx = 70, pady = 50)








root.mainloop()
