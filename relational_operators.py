#Write a condition for a movie streaming platform which 
#checks if users are over 13. If they aren't, print "Sorry, parental control required"

#Define age variable
age = 8

#the condition
if age <= 13:
    print("Sorry, parental control is required")

#Example 2
x = 20
y = 20

if x == y:
    print("These numbers are the same")

uniCredits = 120

if uniCredits >= 120:
    print("Congratulations! You have enough credits to graduate!")

#using the "and" operator
#Rewrite the above if statement so that it checks to see if a student
#meets the minimum gpa requirement of 2.0 as well as the credits.

uniCredits = 120
gpa = 3.4 #we've assigned the gpa here.

if uniCredits >= 120 and gpa >= 2.0:
    print("Congratulations! You meet the requirements to graduate!")