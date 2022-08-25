#Example 1
#Create a new list called sam_height_and_testscore that contains:

#The string "Sam" (to represent Sam’s name)
#The number 67 (to represent Sam’s height)
#The float 85.5 (to represent Sam’s score)
#The boolean True (to represent Sam passing the test)

from doctest import Example


sam_height_and_testscore = ["Sam", 67, 85.5, True]


#List methods: Examples:
#.append() adds an element at the end of a list. E.g.
example_List = [1, 2, 3, 4]
example_List.append(5)
print(example_List)

#Append Example 2:
#create a list
garden = ["Tomatoes", "Garlic", "Spinach"]
#append a new element:
garden.append("Mangoes")
print(garden)

#Append Example 3
orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")
print(orders)

#.remove() removes an element in a list. E.g. 
example_List.remove(4)
print(example_List)