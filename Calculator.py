num1=float(input("Enter a Number1: "))
num2=float(input("Enter a Number2: "))
print("Enter a Match: ")
print("1.+")
print("2.-")
print("3.*")
print("4./")
choice=input("Enter a Number Match: ")
if choice =="1":
    result=num1+num2
    print("Natije Jame: ",int(result))
elif choice =="2":
    result=num1-num2
    print("Natije Tafrigh: ",int(result))
elif choice =="3":
    result=num1*num2
    print("Natije Zarb: ",int(result))
elif choice =="4":
    if num2 !=0:
     result=num1/num2
    print("Natije Taghsim: ",int(result))
else:
    print("Error! Taghsim bar sefr Momken Nist.")
