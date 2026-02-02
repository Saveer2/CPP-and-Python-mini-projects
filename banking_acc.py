import os
filename = "banking.txt"
if not os.path.exists(filename):
    open(filename,"w").close()

class Bank_Account:
    def __init__(self,name,id,pin,acc_num,balance):
        self.name =  name
        self.id = id
        self.pin = pin
        self.acc_num = acc_num
        self.balance = balance

    def save(self):
        with open(filename,"a") as f:
            f.write(f"{self.name},{self.id},{self.pin},{self.acc_num},{self.balance}\n")
    
    def deposit(self,id,pin,amount):
        lines = []
        check = False
        with open(filename,"r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == str(id) and data[2] == str(pin):
                    balance = int(data[4])
                    balance += amount
                    data[4] = str(balance)
                    check = True
                lines.append(",".join(data))

        if check == True:
            with open(filename,"w") as f:
                for line in lines:
                    f.write(line + "\n")
            print("Deposit Successful!!")
        else:
            print("Your Pin or Id Is wrong!!")

    def withdraw(self,id,pin,amount):
        lines = []
        check = False
        with open(filename,"r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == str(id) and data[2] == str(pin):
                    balance = int(data[4])
                    if balance >= amount:
                        balance -= amount
                        data[4] = str(balance)
                        check = True
                    else:
                        print("Your amount is greater than your balance!!")
                lines.append(",".join(data))

        if check == True:
            with open(filename,"w") as f:
                for line in lines:
                    f.write(line + "\n")
            print("Withdraw Successful!!")
        else:
            print("Your Pin or Id Is wrong!!")    

choice = True
while choice:
    print("\n\t** Bank Account!! **\n")   
    ch = int(input("Enter Your Choice (1. Add Data\n2. Deposit Amount\n3. Withdraw Amount\n4. Exit) \nEnter :")) 

    if ch == 1:
        name = input("Enter Name : ") 
        id = input("Enter ID : ")
        pin = input("Enter PIN : ")
        acc_num = input("Enter Account Number : ")
        bal = int(input("Enter balance : "))
        acc = Bank_Account(name,id,pin,acc_num,bal)
        acc.save()
    elif ch == 2:
        id = input("Enter ID : ")
        pin = input("Enter PIN : ")
        amm = int(input("Enter Amount to deposit : "))
        acc = Bank_Account("", "", "", "", 0)
        acc.deposit(id,pin,amm)
    elif ch == 3:
        id = input("Enter ID : ")
        pin = input("Enter PIN : ")
        amm = int(input("Enter Amount to withdraw : "))
        acc = Bank_Account("","","","",0)
        acc.withdraw(id,pin,amm)
    elif ch == 4:
        print("\n** Thanks for using Bank Account System!!")
        break
    else:
        print("** Invalid Choice!!")
    
    ch1 = input("Do you what to repeat (Y/N) : ")
    if ch1 == "y" or ch1 =="Y":
        choice = True
    else:
        choice = False             

    if choice==False:
        print("\n** Thanks for using Bank Account System!!")
        break