import datetime
def returns(Library_books,name,borrowed_cart,returned_cart):
    if not(name in borrowed_cart):
        print("This person cannot be found in our database")
        return [Library_books,returned_cart]
    while True:
        try:
            Book_ID=input("Please enter the book-id or n to exit: ")
        except:
            print("value error")
            continue
        if Book_ID=="n":
            print("The book has been returned successfully.")
            print("************Thank you******************")
            return [Library_books,returned_cart]
        else:
            borrowed_date=borrowed_cart[name][1]
            book_list=borrowed_cart[name][0]
            returned_date=datetime.date.today()
            diff=returned_date-borrowed_date
            borrowed_days=int(diff.days)
            if Library_books[Book_ID][0] in book_list:
                book_name=Library_books[Book_ID][0]
                book_price=float(Library_books[Book_ID][3][1:])
                if (borrowed_days<=10):
                    fine=0.0
                else:
                    fine=borrowed_days*0.1*book_price
                if name in returned_cart:
                    returned_cart[name][0].append(book_name)
                    returned_cart[name][1].append(book_price)
                    returned_cart[name][2].append(fine)
                else:
                    returned_cart[name]=[[book_name],[book_price],[fine]]
                Library_books[Book_ID][2]=str(int(Library_books[Book_ID][2])+1)
            else:
                print ("The book id entered can't be found in persons record.")    


