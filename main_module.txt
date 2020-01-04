#importing the modules
import borrow_module
import return_module
import write_to_file_module
#Reading the database from Library_books.txt file
file=open("books.txt","r")
file_String=file.read()
file.close()
file_String=file_String.split("\n")
# Dictionaries to store the information about borrowed and returned books
borrowed_cart={}
returned_cart={}
#Putting database information to a python dictionary named as "Library_books"
Library_books={}
check=True
for each in file_String:
    line=each.split(",")
    Library_books[line[0]]=line[1:]
    try:
        Library_books.pop("")
    except:
        pass
#Fuction to display the Library_books database
def display_books(menu):
    print ("Book id\t\tBook name\t\t\tQuantity\t\tPrice")
    for keys,values in menu.items():
        print(keys+"\t\t"+values[0]+"\t\t\t"+values[2]+"\t\t\t"+values[3])
    print("\n")
while check==True:
    choice=int(input("1)ENTER 1 TO DISPLAY AVAILABLE BOOKS\n2)ENTER 2 TO BORROW BOOK\n3)ENTER 3 TO RETURN BOOK\n4)ENTER 4 TO QUIT THE PROGRAM\n"))
    if  choice==1:
        display_books(Library_books)
    elif choice==2:
        name=input("Enter your name: ")
        borrow_list=borrow_module.borrow(Library_books,name,borrowed_cart)
        Library_books=borrow_list[0]
        borrowed_cart=borrow_list[1]
    elif choice==3:
        name=input("Enter your name: ")
        return_list=return_module.returns(Library_books,name,borrowed_cart,returned_cart)
        Library_books=return_list[0]
        returned_cart=return_list[1]
    elif choice==4:
        break
    else:
        print(" Sorry !!The entered number doesnot exist")

write_to_file_module.write_to_txt("books.txt",Library_books,"l")
write_to_file_module.write_to_txt("borrowed.txt",borrowed_cart,"b")
write_to_file_module.write_to_txt("returned.txt",returned_cart,"r")
