import os

filename = "contact.txt"
if not os.path.exists(filename):
    open(filename,"w").close()

class contact:
    def __init__(self,id,name,num,relation):
        self.id = id
        self.name = name
        self.num = num
        self.relation = relation

    def save(self):
        with open(filename, "a") as f:
            f.write(f"{self.id},{self.name},{self.num},{self.relation}\n")
            

def view_all():
    with open(filename,"r") as f:
        print("\nID  NAME  NUMBER  RELATION")
        for line in f:
            print(line.strip())

def search_id(id):
    with open(filename,"r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == str(id):
                print(f"Found: ID={data[0]}, Name={data[1]}, Number={data[2]}, Relation={data[3]}")
                return
    print("Contact Not Found!!")


print("\t** CONTACT BOOK!! **\n\n")
while True:

    print("\n\n1. ADD\n2. SEARCH\n3. VIEW ALL\n4. EXIT")
    ch = int(input("* Enter your choice : "))

    if ch == 1:
        n = input("* Enter Name : ")
        i = input("* Enter ID : ")
        nu = (input("* Enter Number : "))
        r = input("Enter Relation : ")
        contact(i,n,nu,r).save()
    
    elif ch == 2:
        id = input("* Enter ID to Search : ")
        search_id(id)
    
    elif ch == 3:
        view_all()

    elif ch == 4:
        break

    else:
        print("** Please enter a valid number!!")
        
