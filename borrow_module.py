import datetime
def borrow(Library_books,name,borrowed_cart):
    while True:
        try:
            Book_ID=input("Please enter the book-id or n to exit: ")
        except:
            print("Error detected")
            continue
        if Book_ID=="n":
            return [Library_books,borrowed_cart]
            break
        if Book_ID in Library_books:
            if int(Library_books[Book_ID][2])>0:
                book_name=str(Library_books[Book_ID][0])
                book_price=float(Library_books[Book_ID][3][1:])
                borrowed_date=input("Enter borrowed date (mm/dd/yyyy): ")
                borrowed_date=borrowed_date.split("/")
                borrowed_date=datetime.date(int(borrowed_date[2]),int(borrowed_date[0]),int(borrowed_date[1]))
                print("You have borrowed the book successfully")
                print("************THANK YOU******************")
                if name in borrowed_cart:
                    borrowed_cart[name][0].append(book_name)
                    borrowed_cart[name][2].append(book_price)
                else:
                    borrowed_cart[name]=[[book_name],borrowed_date,[book_price]]
                Library_books[Book_ID][2]=str(int(Library_books[Book_ID][2])-1)           
            else:
                print ("Book cannot be found in our stock.")
        else:
            print("Book id doesnot exist in stock.")   
