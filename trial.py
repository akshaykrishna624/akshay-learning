print("welcome to ATM")
deposit=1000
balance=deposit
while True:
    print('1. Deposit')
    print('2. Balance')
    print('3. Withdraw')
    print('4. exit')

    
    choice=int(input("\n Enter any options given Above!"))
    if choice==1:
        print("your deposit amount is",deposit)
    elif choice==2:
        print("the current balance is",balance)
    elif choice==3:
        print("Amount withdrawing is successful")
        continue
    elif choice==4:
        print("thank you for visiting") 
        break
    else:
        print("invalid input") 
            
    


