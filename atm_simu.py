import os

filename = "atm_simu.txt"
if not os.path.exists(filename):
    open(filename, "w").close()

class ATMsimu:
    def __init__(self, id, name, accnum, bal):
        self.id = id
        self.name = name
        self.accnum = accnum
        self.bal = bal

    def save(self):
        with open(filename, "a") as f:
            f.write(f"{self.id},{self.name},{self.accnum},{self.bal}\n")

def search(id):
    with open(filename, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == str(id):
                print("\n** You searched for :\n")
                print(f"ID={data[0]}, Name={data[1]}, Accnum={data[2]}, Bal={data[3]}")
                return
    print("\n* User not found!!")

def view_bal(acc):
    with open(filename, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[2] == str(acc):
                print("\n** Your Total Balance : ")
                print(f"BAL={data[3]}")
                return
    print("\n* Account Number not found!!")

print("\t** ATM SIMULATOR!! **\n\n")

while True:
    print("\n1. ADD\n2. SEARCH\n3. VIEW BAL\n4. EXIT")
    ch = input("* Enter your choice : ")

    if ch == "1":
        i = input("* Enter ID : ")
        n = input("* Enter Name : ")
        a = input("* Enter Account Number : ")
        b = input("* Enter Balance : ")
        ATMsimu(i, n, a, b).save()

    elif ch == "2":
        i = input("* Enter ID to Search : ")
        search(i)

    elif ch == "3":
        a = input("* Enter Account Number : ")
        view_bal(a)

    elif ch == "4":
        print("Exiting ATM Simulator. Goodbye!")
        break

    else:
        print("** Please enter a valid number!!")