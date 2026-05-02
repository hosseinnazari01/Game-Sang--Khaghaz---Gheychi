computer="Sang"
user=input("Sang - Kaghaz - gheychi: ")
if user == computer:
    print("Mossaavi Shode!")
elif user == "Kaghaz" and computer == "Sang":
    print("To Bordi!")
elif user == "Gheychi" and computer == "Kaghaz":
    print("To Bordi!")
elif user == "Sang" and computer == "Gheychi":
    print("To Bordi!")
else:
    print("Computer Bord!")
