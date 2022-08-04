#Loops practice

#forLoop
for name in ["Carter", "Reagan", "Obama", "Trump"]:
    print (name + " was a U.S. President.")

for name in ["Mike Pence", "Joe Biden"]:
    print (name + " was a Vice-President in the USA.")

for name in ["Mwai Kibaki", "Michael Kijana Wamalwa"]:
    print (name + " was a Vice-President in Kenya")

#a for loop always requires that you declare a variable.
#written in the format of: for..(variable) in..(range): PS. NOTICE the colon : at the end of the condition.

#Example 2
x = 2
multipliers = [1, 2, 3, 4]
for num in multipliers:
    print (x * num)

x = 2
multipliers = [1,2,3,4]
print (x * multipliers) #This will give a different result. 
#..Instead of multiplying variable 2 by the multiples inside the list, 
#..it will repeat the list twice and give: [1, 2, 3, 4, 1, 2, 3, 4]

#Alternative code:
x = 2
for num in range (1,5):
    print (x * num)

#Example 3 - multiplying 2 with every number from 1 to 1000
x = 2
for num in range (1, 1001):
    print(x * num)




