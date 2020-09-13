import pickle
import sys
from time import sleep

class Book:
    def start1(self):
        self.sets = str(input(">>>"))
    
    contacts = {}

    def delete(self):
        answer1 = str(input("Want to delete the contact?\nEnter 'Yes',if yes or 'No' if no:\n"))
        if answer1.startswith("Y"):
            how = str(input("Which one?:[name]\n"))
            for usr in self.contacts:
                if usr == how:
                    print("Deleting...")
                    del self.contacts[usr]
                    sleep(2)
                    print("The contact succesfuly deleted!")
                    print(self.statem_2())
                else:
                    print("You haven't got any contact with this name.")
                    print(self.statem_2())

    def add(self):
        answer2 = str(input("Add the contact?:\n"))      #There you mast answer yes or no!
        if answer2.startswith("Y"):
            name = str(input("Enter the name of contact:\n"))
            tnumber = int(input("Enter the phone number:\n"))
            print("Adding contact to the notes...")
            self.contacts[name] = str(tnumber)            
            sleep(3)
            print("Contact is succesfuly added")
            print("Now your dictionaries is:\n", self.contacts)
            print(self.statem_2())

    def view(self):
        answer3 = str(input("View all your notes?:\n"))
        if answer3.startswith("Y"):
            print("Your notes:\n",self.contacts)
            print(self.statem_2())
            
    
    def qut(self):
        ex = str(input("Quit the program?:\n"))
        if ex.startswith("Y"):
            sys.exit("Exit...")
            sleep(1)
        elif ex.startswith("Н"):
            print(self.statem_2())
    
    def statem(self):
        print("Adress book v1.0!\nWrite 'Delete','Add','View' if you want to delete, add or view the book!")
        print("((You should write the words with a capital letеer!))")
        self.start1()
        if self.sets.startswith("A"):
            print(self.add())
        elif self.sets.startswith("V"):
            print(self.view())
        elif self.sets.startswith("D"):
            print(self.delete())
        else:
            print(self.qut())
    
    def statem_2(self):
        self.start1()
        if self.sets.startswith("A"):
            print(self.add())
        elif self.sets.startswith("V"):
            print(self.view())
        elif self.sets.startswith("D"):
            print(self.delete())
        else:
            print(self.qut())


p = Book()
print(p.statem())
