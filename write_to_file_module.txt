def write_to_txt(file_name,data_to_write,text_file_choice):
    file=open(file_name,"w+")
    for keys,values in data_to_write.items():
        if text_file_choice=="l":
            file.write(keys+","+values[0]+","+values[1]+","+values[2]+","+values[3]+"\n")
        elif text_file_choice=="b":
            file.write("************************************************************************************************")
            file.write("*******************************Borrow Note:*****************************************************")
            file.write("************************************************************************************************")
            file.write("Name: "+keys+"\n")
            file.write("S.No\t\tBook Borrowed\t\tDate\t\tPrice\n")
            sum=0.0
            for x in range(0,len(values[0])):
                file.write(str(values[0][x])+"\t\t"+str(values[1])+"\t\t"+"$"+str(values[2][x])+"\n")
                sum=sum+values[2][x]
            file.write("Grand Total: \t"+"$"+str(sum)+"\n")
            file.write("************************************************************************************************")
            file.write("**********************************THANK YOU ****************************************************")
            file.write("************************************************************************************************")
        elif text_file_choice=="r":
            file.write("************************************************************************************************")
            file.write("*******************************Return Note:*****************************************************")
            file.write("************************************************************************************************")
            file.write("Name: "+keys+"\n")
            file.write("Book Returned\t\t\tPrice\t\t\tFine\n")
            sum=0.0
            for x in range(0,len(values[0])):
                file.write(str(values[0][x])+"\t\t"+"$"+str(values[1][x])+"\t\t"+"$"+str(values[2][x])+"\n")
                sum=sum+values[2][x]
            file.write("Total Fine: \t"+"$"+str(sum)+"\n")
            file.write("************************************************************************************************")
            file.write("*********************************THANK YOU******************************************************")
            file.write("************************************************************************************************")
    file.close()
