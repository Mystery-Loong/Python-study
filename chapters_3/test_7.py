guests = ['lu xiaolong','jia tingting','lu yunqi']
print(guests) 
guests.insert(0,'lu yunqi')
guests.insert(2,'grandmother')
guests.append('grandfather')
print(f"The new guests are {guests}")

print(f"because dinner unable to deliver on time,so I only can invite two guests")

popped_guest = guests.pop()
print(f"{popped_guest.title()} I so sorry to can'n invite you attend my inner")

popped_guest = guests.pop()
print(f"{popped_guest.title()} I so sorry to can'n invite you attend my inner")

popped_guest = guests.pop()
print(f"{popped_guest.title()} I so sorry to can'n invite you attend my inner")

popped_guest = guests.pop()
print(f"{popped_guest.title()} I so sorry to can'n invite you attend my inner")

print(guests)

print(f"{guests[0].title()} you can attend my inner")
    
print(f"{guests[1].title()} you can attend my inner")

del guests[0]
del guests[0]
print(guests)