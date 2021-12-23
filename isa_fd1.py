
#This is Pranav's change
clientName = ['Dhiru Ram', 'Bharadwaj Pranav', 'Samar Pratap', 'Rodri Martinez', 'Kevin de Bruyne', 'Younis Khan', 'Idris Alba']
clientPins = ['0001','0002', '0003','0004','0005','0006','0007']
clientBalances = [7000,9000,10000,20000,150150010,250000,25250020]
clientDeposition = 0
clientWithdrawal = 0
clientBalance=0
while True:
    print("*"*80)
    print("WELCOME TO PES BANKING SYSTEM".center(80, '='))
    print("*"*80)
    print("(a). Open New Client Account".center(80))
    print("(b). Withdraw money".center(80))
    print("(c). Deposit money".center(80))
    print("(d). Check balalnce".center(80))
    print("(g). Loan".center(80))
    print("(h). Loan status".center(80))
    print("(i). Check Balance".center(80))
    print("(e). Quit".center(80))
    print("*"*80)

    enterLetter = input("Select an option from the menu above: ")
    def opna():
        global u
        u=0
        global disk1
        disk1= 1
        global disk2
        disk2 = len(clientName)

        print("'Open New Client Account' is selected by the Client")
        numOfClient = eval(input("Number of clients : "))
        u=u+numOfClient

        if u > 3:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            u=u-numOfClient
        else:
            while disk1 <= u:
                name = input("Write your Full Name : ")
                clientName.append(name)
                print("Your name is added to Client list".center(80, '-'))
                pin = str(input("Please enter a PIN to secure your Account : "))
                clientPins.append(pin)
                print("Your pin is added".center(80, '-'))
                clientBalance = 0
                clientDeposition = eval(input("Please enter the amount of Money you wish to Deposit to start an Account : "))
                clientBalance = clientBalance + clientDeposition
                clientBalances.append(clientBalance)
                print("Your balance is updated".center(80, '-'))
                print("\nName : ", end=" ")
                print(clientName[disk2])

                print("Pin : ", end=" ")
                print(clientPins[disk2])

                print("Balance : ", "$", end=" ")
                print(clientBalances[disk2], end="\n")

                disk1 = disk1 + 1
                disk2 = disk2 + 1



        print("New Client account created successfully !".center(80, '-'))
        print("\n")
        print("Your name is available on the client list now : ".center(80, '-'))
        print(clientName)
        print("\n")
        print("Note! Please remember the Name and Pin".center(80, '-'))
        print("="*80)

        mainMenu = input("Press Enter key to go back to Main Menu to conduct another transaction or Quit")


    def opnb():
        v=0
        print("'Withdraw Money' is selected by the client")
        while v<1:
            w=-1
            name = input("Please enter account name: ")
            pin = input("Please enter account pin: ")
            while w < len(clientName) - 1:
                w=w+1
                if name == clientName[w]:
                    if pin == clientPins[w]:
                        v=v+1
                        print("\nYour current Balance: ", "$", end=" ")
                        print(clientBalances[w], end=" ")
                        print("\n")
                        clientBalance = (clientBalances[w])
                        clientWithdrawal = eval(input("Insert value for Withdrawal: "))
                        if clientWithdrawal > clientBalance:
                            print("\nWithrawal amount exceeds Balance!")
                            break
                        clientBalance = clientBalance - clientWithdrawal
                        print("\n")
                        print("Withdrawal Successful!".center(80, '-'))
                        clientBalances[w] = clientBalance
                        print("\nYour new balance: ", "$", clientBalance, end=" ")
                        print("\n\n")
            if v<1:
                print("\nYour name and pin do not match!\n")
                break


        mainMenu = input("\nPress Enter key to go back to Main Menu to conduct another transaction or Quit")

    def opnc():
            v=0
            print("'Deposit Money' is selected by the Client".center(80, '-'))
            while v<1:
                w= -1
                name = input("Please enter account name: ")
                pin = input("Please enter account pin: ")
                while w < len(clientName)-1 :
                    w=w+1
                    if name == clientName[w]:
                        if pin == clientPins[w]:
                            v=v+1
                            print("\nYour current balance: ", "$", end=" ")
                            print(clientBalances[w], end=" ")
                            clientBalance=(clientBalances[w])
                            print("\n")
                            clientDeposition = eval(input("Enter the value you want to deposit: "))
                            clientBalance = clientBalance + clientDeposition
                            clientBalances[w] = clientBalance
                            print("\n")
                            print("Deposition successful!".center(80, '-'))
                            print("\nYour new balance: ", "$", clientBalance, end=" ")
                            print("\n")
                if v<1:
                    print("Your name and pin do not match! \n")
                    break

            mainMenu = input("Press Enter key to go Back to Main Menu to conduct another transaction or Quit")

    def opnd():
            print("'Check Balance' is selected by the Client")
            w=0
            print("Client name list and balances mentioned below: ")
            print("\n")
            while w<= len(clientName) - 1:
                    print("-> Customer = ",clientName[w])
                    print("-> Balance = ", "$", clientBalances[w], end=" ")
                    print("\n")
                    w=w+1
            mainMenu = input("Press Enter key to go Back to Main Menu to conduct another transaction or Quit")


    def opng():

        loanAccount=[]
        v=0
        print("'Deposit Money' is selected by the Client".center(80, '-'))
        while v<1:
            w= -1
            name = input("Please enter account name: ")
            pin = input("Please enter account pin: ")
            while w < len(clientName)-1 :
                w=w+1
                if name == clientName[w]:
                    if pin == clientPins[w]:
                        v=v+1
                        loan_amt=int(input("Enter the loan amount to be borrowed "))
                        n=20*int(clientBalances[w])
                        if loan_amt>n:
                            print("Applicable loan amount exceeded")
                        else:
                            clientBalances[w]=clientBalances[w]+loan_amt
                            print("LOAN APPROVED")
                            print("New balance: $",clientBalances[w])
                            loanAccount.append(clientName[w])
                            print("Loan account list: ",loanAccount)
        mainMenu=input("Press Enter key to go Back to Main Menu to conduct another transaction or Quit")


    if enterLetter == "a":
        opna()

    elif enterLetter == "b":
        opnb()

    elif enterLetter == "c":
        opnc()

    elif enterLetter == "d":
        opnd()

    elif enterLetter == "g":
        opng()

    elif enterLetter == "e":
        print("The client has chosen the Quit option")
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid option!")
        print("Please try again!")
        mainMenu = input("Press Enter key to go Back to Main Menu to conduct another transaction or Quit")
