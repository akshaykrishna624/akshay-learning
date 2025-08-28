while True:
    print("\n select operations")
    print("1. add")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    
    choice=input("enter any choice")
    
    if choice in('1','2','3','4'):
        try:
            num1=int(input("enter first number"))
            num2=int(input("enter second number"))
        except ValueError:
            print("invaid input!.Please enter number only")
            continue
        if choice=='1':
            print("sum =",num1+num2)
        elif choice=='2':
            print("substract =",num1-num2)
        elif choice=='3':
            print("MULTIPLY =",num1*num2)
        elif choice=='4':
            if num2==0:
                print("CANNOT DIVIDE BY ZERO")
            else:
                print("DIVIDE =",num1/num2)    
    elif choice=='5':
        print("EXITING FROM CALCULATOR")
        break
    else:
        print("invalid input")

