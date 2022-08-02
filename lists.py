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
print(listThree)