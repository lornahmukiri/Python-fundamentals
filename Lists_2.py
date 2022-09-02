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

#Modifying list elements
#Example 1
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
#Let's modify the list above to replace Cauliflower with Strawberries
#We will reassign the value using the specific index, like so:
garden [2] = "Strawberries"
print(garden)

#Example 2
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)
#lets replace "Alisha" with "Alex"
garden_waitlist [-1] = "Alex"
print(garden_waitlist)

#Shrinking a list using .remove()
#Example 1:
order_list = ["Celery", "Orange Juice", "Orange","Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list)

new_store_order_list.remove("Onions")
print(new_store_order_list)
#When we call .remove() on a list with a value that does not exist, we will receive a ValueError, as is the case above...

#Creating 2-D lists (lists containing other lists.)
#Example 1
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

#Example 2
ages =[
  ["Aaron", 15], 
  ["Dhruti", 16]
  ]

#Example 3
class_name_test = [
  ["Jenny", 90],
  ["Alexus", 85.5],
  ["Sam", 83],
  ["Ellie", 101.5],
]
print(class_name_test)

#select Sam‘s test score from the list class_name_test
sams_score = class_name_test[2][1]
print(sams_score)

#select Ellies test score from the list class_name_test, using negative indices.
ellies_score = class_name_test [-1][-1]
print(ellies_score)

#MODIFYING 2D Lists
#Example 1
#2D list of the incoming class.
incoming_class = [
["Kenny", "American", 9],
["Tanya", "Russian", 9],
["Madison", "Indian", 7],
]
print(incoming_class)

#changing Madison's grade to 8 (using a positive index)
incoming_class[2][2] = 8
print(incoming_class)

#changing Kenny's name to Ken, using a negative index.
incoming_class[-3][-3] = "Ken"
print(incoming_class)


#LIST REVIEW: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small","Large","Medium"]

#Add Depak's size as Medium.
preferred_size.append("Medium")
print(preferred_size)

customer_data = [
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
]
print(customer_data)

customer_data[2][2] = False
print(customer_data)

customer_data[1].remove(False)
print(customer_data)

customer_data_final =  customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)