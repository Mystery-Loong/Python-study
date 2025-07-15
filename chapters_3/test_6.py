guests = ['lu xiaolong','jia tingting','lu yunqi']
print(guests) 
guests.insert(0,'lu yunqi')
guests.insert(2,'grandmother')
guests.append('grandfather')
counts = len(guests)
print(f"The new guests are {guests},totle: {counts}")