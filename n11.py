want = []
have = []
donation = []
while True :
    name2 = input("Enter the name of a book you own: ")
    if name2:
        have.append(name2)
        break
    else:
        print("you forgot to enter the book'd title: ")
name2 = input("Enter the name of another book you own\n(or press 'Enter to skip): ")
if name2 :
    have.append(name2)
    print(f"your library: {have}")
else:
    print(f"your library: {have}")
print("")
print("")
name1 = input("Enter the name of book you wish to have in the future (or Enter to skip): ")
if name1:
    want.append(name1)
    name1 = input("Enter the name of another book you wish th have ( or press 'Enter' to skip): ")
    if name1:
        want.append(name1)
        print("")
        print(f" your wishlist: {want}")
        print("")
else:
    print("")
    print(f"your wishlist:{want}")
name2 = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if name2 :
    have.append(name2)
    want.remove(name2)
    print(f"updated library: {have}")
    print(f"updated wishlist: {want}")
else:
    print("")
name3 = input("Enter the lite of a book from your libaray like to donate (or press 'Enter' to skip): ")
if name3:
    donation.append(name3)
    print(f"final library after donatlons: {have}")
else:
    print(f"final libary after donatlons: {have}")
