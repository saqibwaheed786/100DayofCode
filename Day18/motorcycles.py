#let’s say we have a list of motorcycles, and the first item in
#the list is 'honda'. How would we change the value of this first item?

#motorcycles=['honda', 'yamaha', 'suzuki' ]
#print(motorcycles)

#motorcycles[0]= 'dacati'
#print(motorcycles)

#Appending Elements to the End of a List

#motorcycles.append('ducati')
#print(motorcycles)

#you can start with an empty list and then add items to the list
#using a series of append() statements

#motorcycles=[]

#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')
#print(motorcycles)

#Inserting Elements into a List

#motorcycles=['honda', 'yamaha', 'suzuki' ]
#motorcycles.insert(2, 'ducati')
#print(motorcycles)

#Removing an Item Using the del Statement
motorcycles=['honda', 'yamaha', 'suzuki', 'ducati']
del motorcycles[1]

#popped_motorcycle = motorcycles.pop()
print(motorcycles)
#print(popped_motorcycle)

#last_own = motorcycles.pop()  # this syntax remove "suzuki" from the list and show outside
#print("The last motorcycle I owned was a " + last_own.title() + "." )

#Removing an Item by Value
#If you only know the value of the item you want to remove, you
#can use the remove() method.


#print a reason for
#removing it from the list  more detail see in Chapter 7
