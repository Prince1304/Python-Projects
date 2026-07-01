import time
from operator import index

from numpy.ma.extras import unique


class Book:
    Books = [
        ["kp",9000,1,"kp patel","Wed, 01 Jul 2026"],
    ]
    Order = []

    def __init__(self):

        print("=" * 50)
        print("Welcome to Gen-Z Library")
        print("=" * 50)
        while True:
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Show Books")
            print("4. Order Books")
            print("5. View Orders")
            print("0. Exit")
            print("-" * 50)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addBook()
            elif choice == "2":
                self.removeBook()
            elif choice == "3":
                self.showBooks()
            elif choice == "4":
                self.orderBook()
            elif choice == "5":
                self.vieworder()
            elif choice == "0":
                break
            else:
                print("Please Enter a Valid Choice")

    def security(self):
        print("=" * 50)
        print("This Only For Authorise Use")
        print("=" * 50)
        attempt = 3
        while True:
            if attempt == 0:
                print("Warning! You not Entering.")
                print("Try After 1 Minute.")
                time.sleep(60)
                attempt+=3
            else:
                password = input(f"Enter Password ({attempt} try left): ")
                if password == "admin123":
                    print("Welcome Admin!")
                    print("=" * 50)
                    return
                else:
                    print("Please Enter a Valid Password")
                    attempt -= 1

    def addBook(self):
        self.security()
        unique_book = ''
        while True:
            Book_name = input("Enter Book Name: ")
            for book in self.Books:
                if book[0] == Book_name:
                    print(f"{Book_name} has been Already Added try Another Name.")
                else:
                    unique_book = Book_name
            break
        book_price = input("Enter Book Price: ")
        book_quantity = input("Enter Book Quantity: ")
        book_author = input("Enter Book Author: ")
        current_time = time.strftime("%a, %d %b %Y",time.localtime())
        book_date = current_time

        addbook = [
            unique_book,
            book_price,
            book_quantity,
            book_author,
            book_date
        ]
        self.Books.append(addbook)
        print("-" * 50)
        print(f"{unique_book} has been added to the Books List.")
        print("-" * 50)

    def removeBook(self):
        self.security()
        Book_name = input("Enter Book Name: ")
        for book in self.Books:
            if book[0] == Book_name:
                self.Books.remove(book)
                print("-" * 50)
                print(f"{Book_name} has been removed from the Books List.")
                print("-" * 50)
            else:
                print("Please Enter a Valid Book Name.")

    def showBooks(self):
        column = ["Index","Book Name", "Book Price", "Book Quantity", "Book Author", "Book Date"]
        Inx = 1
        print("=" * 100)
        print(f"{"My Book List":^100}")
        print("=" * 100)
        print(f"{column[0]:<10}{column[1]:<15} {column[2]:<15} {column[3]:<15} {column[4]:<15} {column[5]:<15}")
        print("-" * 100)
        if not self.Books:
            print("No Books have been Founded!")
            return
        else:
            for book in self.Books:
                print(f"{Inx:<10}{book[0]:<15} {book[1]:<15} {book[2]:<15} {book[3]:<15} {book[4]:<15}")
                Inx+=1
        print("=" * 100)

    def orderBook(self):
        column = ["Index", "Book Name", "Price", " Qnty"]
        Inx = 1
        print("=" * 45)
        print(f"{"My Book List":^45}")
        print("=" * 45)
        print(f"{column[0]:<10}{column[1]:<15} {column[2]:<10} {column[3]:<10}")
        print("-" * 45)
        if not self.Books:
            print("No Books have been Founded!")
            print("=" * 45)
            return
        else:
            for book in self.Books:
                print(f"{Inx:<10}{book[0]:<15} {book[1]:<15} {book[2]:<15}")
                Inx+=1
        print("=" * 45)

        while True:
            order_book = input("Enter Order Book Name (Press 'o' for Order): ")
            if order_book == "o" or order_book == "O":
                break
            else:
                for book in self.Books:
                    if book[0] == order_book:
                        if book[2] == 0:
                            print(f"Book '{order_book}' is Currently Out of Stock!")
                        else:
                            book[2] -= 1
                            order_entry = book.copy()
                            book_inx = book[0].index(order_book)
                            current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
                            order_entry.insert(5, current_time)
                            self.Order.append(order_entry)
                    else:
                        print("Please Enter a Valid Order Book Name.")
    def vieworder(self):
        column = ["Index", "Book Name", "Price", " Qnty", "Author", "Publish Date", "Order Date"]
        inx = 1
        qnty = 1
        print("=" * 110)
        print(f"{"My Order Book List":^110}")
        print("=" * 110)
        print(f"{column[0]:<5} {column[1]:<10} {column[2]:<10} {column[3]:<10} {column[4]:<15} {column[5]:<20} {column[6]:<20}")
        print("-" * 110)
        if not self.Order:
            print("No Orders have been Founded!")
            print("=" * 110)
            return
        else:
            for ob in self.Order:
                print(f"{inx:<5} {ob[0]:<10} {ob[1]:<10} {qnty:<10} {ob[3]:<15} {ob[4]:<20} {ob[5]:<20}")
                inx += 1
                print("=" * 110)

    print("*"*100)
    print("Thanks for Use Gen-Z Library!")
    print("I hope you Visit Again!")
    print("*"*100)

book = Book()
