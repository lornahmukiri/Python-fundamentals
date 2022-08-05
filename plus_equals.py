#Python offers a shorthand for updating variables. 
# When you have a number saved in a variable and 
# want to add to the current value of the variable, 
# you can use the += (plus-equals) operator

#Example 1:
milesWalked = 12 #This is our first variable representing the number of miles walked

#Then we want to update the variable above to include another 3 miles we walked,. So:
milesWalked +=3
print(milesWalked)
#...This will print 15.
#So, instead of recalculating from the start, we've kept a grand total and updated it when we walked further.


#Example 2:
#The += can also be used for string concatenation:

hikeCaption = "What an amazing time to walk through nature!" # Our first variable

#lets add some hashtags that we almost forgot!:
hikeCaption += "#sunnyDay"
hikeCaption += "feelingBlessed"
print(hikeCaption) #., this will print: What an amazing time to walk through nature!#sunnyDayfeelingBlessed
#what we've done aboe is created a social media caption for the photograph of nature we took on our hike,
#  but then update the caption to include important social media tags we almost forgot.

#Example 3:
#We’re doing a little bit of online shopping and find a pair of new sneakers. 
# Right before we check out, we spot a nice sweater and some fun books we also want to purchase!
#Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.
totalPrice = 0
newSneakers = 50.00

totalPrice += newSneakers

niceSweater = 40.00
funBooks = 30.00
#let's update the total price now:
totalPrice += niceSweater + funBooks

print("The total price is", totalPrice)
#this will print 120
