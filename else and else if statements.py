age = 12

if age >= 13:
    print("Access granted.")
else:
    print("Sorry, you must be 13 or older to watch this movie.")


#example 2
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("Congratulations. You meet the graduation requirements")
else:
    print("You do not meet the requirements to graduate.")


#Example 3:
donation = 5000
print("Thank you for your donation!")

if donation >=1000:
    print("You've achieved platinum donor status")
elif donation >= 500:
    print("You've achived gold donor status")
elif donation >= 100:
    print("You've achieved silver donor status")
else:
    print("You've achieved bronze donor status")


#Example 4
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")


#CODE CHALLENGE
#Little Codey is an interplanetary space boxer, who is trying to 
# win championship belts for various weight categories on other planets within the solar system.
#Write a space.py program that helps Codey keep track of their target weight by:

#1. Checks which number planet is equal to.
#2.It should then compute their weight on the destination planet.
#Here is the table of conversions:
##	Planet	Relative Gravity
#1	Venus	0.91
#2	Mars	0.38
#3	Jupiter	2.34
#4	Saturn	1.06
#5	Uranus	0.92
#6	Neptune	1.19

#The solution:

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

#The if statement is as below:

if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

print("Your weight is:", weight)