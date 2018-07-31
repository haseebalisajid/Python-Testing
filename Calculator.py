def Calculator():
    print("Welcome to CB Calculator")
    print("..........\n.......\n...\n.")
    print("CB Calculator is now ready to calculate your values")
    print("\nSelect operation ")
    print("a.Add")
    print("s.Subtract")
    print("m.Multiply")
    print("d.Divide")

    choice = input("enter your chioce(a/s/m/d): = ")
    num1 = int(input("enter 1st number = "))
    num2 = int(input("enter 2nd number = "))

    if choice == 'a':
        print(num1,"+",num2,"=",num1 + num2)
    elif choice == 's':
        print(num1,"-",num2,"=",num1 - num2)
    elif choice == 'm':
        print(num1,"*",num2,"=",num1 * num2)
    elif choice == 'd':
        print(num1,"/",num2,"=",num1 / num2)
    else:
        print("invalid operator")
z='y'
while z=='y':
    Calculator()
    z = str(input("do you want to calculate more(y/n)"))
    if z=='n':
        print("Good Bye")
