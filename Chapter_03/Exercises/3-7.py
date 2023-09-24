guest = ['Mom','Dad','Dude']

print('I found a bigger table.')
guest.insert(0,'Shui')
guest.insert(1,'Ker')
guest.append('Snow')

print(guest[0]+" I hope you can go to my lunch tonight")
print(guest[1]+" I hope you can go to my lunch tonight")
print(guest[2]+" I hope you can go to my lunch tonight")
print(guest[3]+" I hope you can go to my lunch tonight")
print(guest[4]+" I hope you can go to my lunch tonight")
print(guest[5] + " I hope you can go to my lunch tonight")

print(guest[-1]+",sorry,i cant invited you today")
guest.pop()
print(guest[-1]+",sorry,i cant invited you today")
guest.pop()
print(guest[-1]+",sorry,i cant invited you today")
guest.pop()
print(guest[-1]+",sorry,i cant invited you today")
guest.pop()

print(guest[0]+", "+ guest[1] + " you all still in list")
del guest[0]
del guest[0]
print(guest)