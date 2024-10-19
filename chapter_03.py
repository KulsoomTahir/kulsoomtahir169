#3.1 
names = ["Yashal", "Farheen", "Eman"]
print(names[0])
print(names[1])
print(names[2])

#3.2
message= f"{names[0].title()} is my best friend."
print(message)

#3.3
fav_transport = ["Audi", "Fortuner", "Civic", "Vigo"]
for transport in fav_transport:
    print(f"My favorite transport is {transport}")

#3.4
person =["Yashal", "Farheen", "Eman"]
print(f"{person[0].title()}, I would be deeply honoured if you could join me.")

#3.5
person =["Yashal", "Farheen", "Eman"]
person[2]= "Aimen"
print(person)

#3.6
guests = ["Yashal", "Eman", "Farheen"]
guests.insert(0, "Aiza")
print(guests)

guests.append("Anila")
print(guests)

sorry = "Eman"
guests.remove(sorry)
print(guests)
print(f"{sorry.title()}, Sorry! we can't invite you.")

#3.8
places = ["London", "Germany", "Turkey", "America"]
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3.9
guests = ["Yashal", "Eman", "Farheen"]
print(len(guests))

#3.10
cities = ["Lahore", "Karachi", "Islamabad", "Quetta"]
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

print(len(cities))

cities.insert(3, "Abbotabad")
print(cities)

cities.remove("Quetta")
print(cities)