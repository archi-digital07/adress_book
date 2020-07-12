import pickle
import sys
from time import sleep

class Book:
    def start1(self):
        self.sets = str(input(">>>"))
    
    contacts = {}

    def delete(self):
        answer1 = str(input("Хотите удалить контакт?\nНапишите 'ДА',если хотите или 'Нет' если нет:\n"))
        if answer1.startswith("Д"):
            how = str(input("Какой именно?:[Имя]\n"))
            for usr in self.contacts:
                if usr == how:
                    print("Удаление...")
                    del self.contacts[usr]
                    sleep(2)
                    print("Контакт успешно удален!")
                    print(self.statem_2())
                else:
                    print("В списке нету такого контакта.")
                    print(self.statem_2())

    def add(self):
        answer2 = str(input("Добавить контакт?:\n"))  #There you mast answer yes or no!
        if answer2.startswith("Д"):
            name = str(input("Введитте имя:\n"))
            tnumber = int(input("Введите номер:\n"))
            print("Создаеться контакт...")
            self.contacts[name] = str(tnumber)            
            sleep(3)
            print("Контакт успешно создан")
            print("Теперь ваш список:\n", self.contacts)
            print(self.statem_2())

    def view(self):
        answer3 = str(input("Хотите просмотреть записи?:\n"))
        if answer3.startswith("Д"):
            print("Ваши записи:\n",self.contacts)
            print(self.statem_2())
            
    
    def qut(self):
        ex = str(input("Выйти из программы?:\n"))
        if ex.startswith("Д"):
            sys.exit("Выход...")
            sleep(1)
        elif ex.startswith("Н"):
            print(self.statem_2())
    
    def statem(self):
        print("Адресная книга версии 1.0!\nНапишите 'Удалить','Добавить','Просмотреть' чтобы удалить, добавить или просмотреть книгу!")
        print("((Советую вводить все с большой буквы!))")
        self.start1()
        if self.sets.startswith("Д"):
            print(self.add())
        elif self.sets.startswith("П"):
            print(self.view())
        elif self.sets.startswith("У"):
            print(self.delete())
        else:
            print(self.qut())
    
    def statem_2(self):
        self.start1()
        if self.sets.startswith("Д"):
            print(self.add())
        elif self.sets.startswith("П"):
            print(self.view())
        elif self.sets.startswith("У"):
            print(self.delete())
        else:
            print(self.qut())


p = Book()
print(p.statem())
