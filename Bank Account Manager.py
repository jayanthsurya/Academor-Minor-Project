# A Simple Financial Account Operator:

#to generate account numbers at random
from random import randint

#dictionary of existing accounts with account password
acc_det = {'202314': 9897, '202315': 5723, '202317': 8520}
#dictionary of existing accounts with account balance
acc_bal = {'202314': 50500, '202315': 15723, '202317': 108520}

#class containing every operation that the project needs
class Operations:

    def create_acc(self): #function to create an account
        new_acc = str(randint(201000, 999000))
        if new_acc not in acc_det.keys() and len(new_acc) == 6:
            print("Your new Account number: ", new_acc)
            new_acc_pass = int(input("Create new password of 4 digits: "))
            if len(str(new_acc_pass)) == 4:
                if new_acc_pass+1-1 == new_acc_pass:
                    acc_det.update({new_acc: new_acc_pass})
                    acc_bal.update({new_acc: 0})
                    print("A new Account was created!")
                    print("Your new Account number: ", new_acc)
                    print("Your new Account Password: ", new_acc_pass)
                else:
                    print("Account password must contain only integral Numbers!")
                    print("Your process of creating an account was terminated!\nPlease try again!!")
            else:
                print("Account password must contain only 4 digits!")
                print("Your process of creating an account was terminated!\nPlease try again!!")
        else:
            Operations.create_acc(self)

    def delete_acc(self):  #function to delete an account
        global acc_num
        assure = input("Are you sure you want to delete your account?\nIf yes press 'y' else press 'n' for No")
        if assure == 'y' or assure == 'Y':
            assure_acc_num = input("Re-enter your account number for confirmation: ")
            if assure_acc_num == acc_num:
                assure_acc_pass = int(input("Enter you 4 digit password for confirmation: "))
                if acc_det[assure_acc_num] == assure_acc_pass:
                    del (acc_det[assure_acc_num])
                    del (acc_bal[assure_acc_num])
                    print("Your account was deleted successfully")
                else:
                    print("Incorrect Account password")
                    print("Your process of deleting account was terminated!\nPlease try again!!")
            else:
                print("Incorrect Account number")
                print("Your process of deleting account was terminated!\nPlease try again!!")
        else:
            print("Process terminated!")

    def deposit(self): #function to deposit amount in an account
        global acc_num
        curr_bal = acc_bal[acc_num]
        print("Current Account Balance = ", curr_bal)
        dep_amt = int(input("Enter amount to be deposited: "))
        if dep_amt+1-1 == dep_amt:
            if dep_amt >= 0:
                curr_bal += dep_amt
                acc_bal[acc_num] = curr_bal
                print("Amount Successfully Deposited!")
                print("Current Account Balance = ", curr_bal)
            else:
                print("Please enter a positive integral deposit amount!")
                print("Your transaction was terminated!\nPlease try again!!")
        else:
            print("Please enter an integral deposit amount!")
            print("Your transaction was terminated!\nPlease try again!!")

    def withdraw(self):  #function to withdraw amount from an account
        global acc_num
        curr_bal = acc_bal[acc_num]
        print("Current Account Balance = ", curr_bal)
        wit_amt = int(input("Enter amount to be withdrawn: "))
        if wit_amt+1-1 == wit_amt:
            if (wit_amt <= curr_bal) and (wit_amt >= 0):
                curr_bal -= wit_amt
                acc_bal[acc_num] = curr_bal
                print("Amount Successfully Withdrawn!")
                print("Current Account Balance = ", curr_bal)
            else:
                print("Insufficient Account Balance!")
                print("Your transaction was terminated!\nPlease try again!!")
        else:
            print("Please enter an integral withdrawal amount!")
            print("Your transaction was terminated!\nPlease try again!!")

    def chk_bal(self):  #function to check balance amount in an account
        global acc_num
        curr_bal = acc_bal[acc_num]
        print("Current Account Balance: ", curr_bal)

    def exit(self): #function to be displayed on exit from the code
        print("Dear Customer!\nThank You for Banking with us!\nVisit Again!")
        print("**************************************************************************")
        print("__________________________________________________________________________")


op = Operations() #call for class assigned to variable op

print("**************************************************************************")
print("Welcome!")

while True: #loop to be continued until the user wants to opt of the operation
    print("Dear Customer!")
    print("__________________________________________________________________________")
    print("__________________________________________________________________________")
    print("Operations Available!")
    print("__________________________________________________________________________")
    print("__________________________________________________________________________")
    print("**************************************************************************")
    print("Press 1 to Create an Account")
    print("Press 2 to Delete an Account")
    print("Press 3 to Deposit Amount")
    print("Press 4 to Withdraw Amount")
    print("Press 5 to Check Account Balance Amount")
    print("Press 6 to Exit from facility")
    print("**************************************************************************")
    print("__________________________________________________________________________")
    choice = int(input("How would you like to proceed with the following available facilities: "))
    print("**************************************************************************")
    if choice == 1: #for choice 1 directed to create function
        op.create_acc()
        print("__________________________________________________________________________")
        print("__________________________________________________________________________")
        con = input("Do you want to continue banking?\nIf yes press 'y' else press 'n' for No") #asks input whether to continue loop
                                                                                                # repeated for after every function completed
        if con == 'y' or con == 'Y':  # if 'y' user want to continue so loop contiues
            continue
        else:  #if 'n' loop stops and code ends
            op.exit()
            break

    elif choice == 6:  #for choice 6 directed to exit function
        op.exit()
        break

    else:
        if choice in [2, 3, 4, 5]:
            acc_num = input("Enter your account number: ")
            if acc_num in acc_det.keys():
                acc_pass = int(input("Enter your 4 digit password: "))
                print("__________________________________________________________________________")
                print("**************************************************************************")
                if acc_det[acc_num] == acc_pass:
                    if choice == 2: #for choice 2 directed to delete function
                        op.delete_acc()
                        print("__________________________________________________________________________")
                        print("__________________________________________________________________________")
                        con = input("Do you want to continue banking?\nIf yes press 'y' else press 'n' for No")
                        if con == 'y' or con == 'Y':  # if 'y' user want to continue so loop contiues
                            continue
                        else:  #if 'n' loop stops and code ends
                            op.exit()
                            break
                    elif choice == 3:  #for choice 3 directed to deposit function
                        op.deposit()
                        print("__________________________________________________________________________")
                        print("__________________________________________________________________________")
                        con = input("Do you want to continue banking?\nIf yes press 'y' else press 'n' for No")
                        if con == 'y' or con == 'Y':  # if 'y' user want to continue so loop contiues
                            continue
                        else:  #if 'n' loop stops and code ends
                            op.exit()
                            break
                    elif choice == 4:  #for choice 4 directed to withdraw function
                        op.withdraw()
                        print("__________________________________________________________________________")
                        print("__________________________________________________________________________")
                        con = input("Do you want to continue banking?\nIf yes press 'y' else press 'n' for No")
                        if con == 'y' or con == 'Y':  # if 'y' user want to continue so loop contiues
                            continue
                        else:  #if 'n' loop stops and code ends
                            op.exit()
                            break
                    elif choice == 5:  #for choice 5 directed to check balance function
                        op.chk_bal()
                        print("__________________________________________________________________________")
                        print("__________________________________________________________________________")
                        con = input("Do you want to continue banking?\nIf yes press 'y' else press 'n' for No")
                        if con == 'y' or con == 'Y':  # if 'y' user want to continue so loop contiues
                            continue
                        else:  #if 'n' loop stops and code ends
                            op.exit()
                            break
                else:
                    print("Incorrect Account password!")
                    print("Your process was terminated!\nPlease try again!!")
            else:
                print("Account number not found!")
                print("Your process was terminated!\nPlease try again!!")
        else:
            print("Provide a correct option!")
            print("Your process was terminated!\nPlease try again!!")
