#Example 1:
greetingText = "Hey there!"
questionText = "How are you?"
fullText = greetingText + questionText
print(fullText)
#>>This will print: Hey there!How are you?

#Adding some spacing in-between both, so we'll use + " " +
fullText = greetingText + " " + questionText
print(fullText)
#>>This will print: Hey there! How are you?


#Example 2:
birthdayString = "I am "
age = 10
birthdayString2 = " years old today!"
#Concatenating an integer with a string is possible IF we turn the integer
#into a string first. 
# Using str() we can convert variables that arent strings into strings. For example:
fullBirthdayString = birthdayString + str(age) + birthdayString2
print(fullBirthdayString)
#>>This will print: I am 10 years old today!

#BUT, if we just wanna print an integer, we can pass a variable as an argument
#to print() regardless of whether it is a string. For instance:
print(birthdayString, age, birthdayString2)
#>>This will still print: I am  10  years old today!

