'''
ATM

'''
user="rana"
password="123"
user_name=input("enter the user name:")
pass_word=input("enter the password:")
s='''
    1.credit
    2.debit
    3.mini statement
    4.exit

'''
ammount=1000
if user_name==user and pass_word==password:
    while True:
        print("====================")
        print(s)
        option=int(input("enter the option:"))
        if option==1:
            credit_ampunt=float(input("enter the amount:"))
            print("ammout after credit:",ammount+credit_ampunt)
        elif option==2:
            debit_ampunt=float(input("enter the amount:"))
            print("ammout after debited:",ammount-debit_ampunt)
        elif option==3:
            print("ammout:",ammount)
        elif option==4:
            break
    else:
        print("incurrect")
