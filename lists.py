#list example
from itertools import count


suits = ['Spades','Clubs','Diamonds','Hearts']

values = ['Ace', 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

print (suits[0]) #here,since the lists starts at Index 0, it prints "Spade"

print (values[12]) #same here, the index starts at zero so the 12th value to be printed is "King"

suits.sort() #sort() arranges in an alphabetical order.
print (suits)

suits.reverse() #reverse allows the list to be sorted in reverse alphabetical order.
print(suits) 

values.reverse()
print(values)

listOne = [101, 102, 103]
listTwo = [104, 105, 106]
listThree = listOne + listTwo
print(listThree) #Here, Python treats the addition as appending listTwo to listOne

#Adding items at the end of the list
listThree += [107] #the += sign will add 107 at the end of the list.
print(listThree)

#Another way of putting an item at the end of the list is by using .append like below:
listThree.append(108)
print(listThree)

#Another example:
fruitBasket1 = ["apples", "oranges", "pears"]
fruitBasket2 = ["mangoes", "pineapples", "tangerines"]
fruitBasket3 = fruitBasket1 + fruitBasket2
print (fruitBasket3)

fruitBasket3.append("lime")
print(fruitBasket3)

#to insert items in the middle of the list, we use insert() method, like so:
listThree.insert(4, 999)
print(listThree)
#in the example above, the insert parameter took two parameters.
#Parameter one is the index position that the new item will take, i.e., position 4.
#Hence, this method call inserts 999 between 103, and 105. Now, 999 is at index 4.
