first = int(input("Enter First value:"))
operatorv = input("Enter a Operator:")
second = int(input("Enter Second value:"))
if(operatorv == "+"):
    print(first,"+",second, "is:",first + second)
elif(operatorv == "-"):
    print(first,"-",second, "is:",first - second)
elif(operatorv == "*"):
    print(first,"X",second, "is:",first * second)
elif(operatorv == "/"):
    print(first,"/",second, "is:",first / second)
else:
    print("wrong operator")
