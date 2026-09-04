Guests = ["grace","favour","may","mary"]
Guests[3] = 'joy'
for guest in Guests:
    print(f"you are invited to dinner {guest}")
for list in Guests:
    print(f"{list} you are still invited")
print("i found a bigger table for the dinner")
Guests.insert(0, "fred")
Guests.insert(2, "jay")
Guests.append("john")

print(Guests)
print("")
for guest in Guests:
    print(f"{guest} you are still invited to the dinner")
print(f"i can only invite 2 people {guest}")
while len(Guests) > 2:
    removeing_guest = Guests.pop()
    print(f"Dear {removeing_guest} i can't invite you to dinner anymore")
for guest in Guests:
    print(f"{guest} you are still invited")
del Guests[0]
del Guests[0]
print(Guests)        






