#CODE CHALLENGE : SAL'S SHIPPING.
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
# Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

#In this project, you’ll build a program that will take the weight of a package and 
# determine the cheapest way to ship that package using Sal’s Shippers.

#Sal’s Shippers has several different options for a customer to ship their package:

#Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
#Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
#Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
#Here are the prices:

#Ground Shipping

#Weight of Package	                    Price per Pound	Flat Charge
#2 lb or less	                                $1.50	$20.00
#Over 2 lb but less than or equal to 6 lb	    $3.00	$20.00
#Over 6 lb but less than or equal to 10 lb	    $4.00	$20.00
#Over 10 lb	                                    $4.75	$20.00

#Ground Shipping Premium

#Flat charge: $125.00



weight = 41.5

#Ground Shipping
if weight <= 2:
  costGround = weight * 1.50 + 20
elif weight <= 6:
  costGround = weight * 3.0 + 20
elif weight <= 10:
  costGround = weight * 4.0 + 20
else:
  costGround = weight * 4.75 + 20
print ("Ground Shipping: $", costGround)

#Ground Shipping Premium
costGroundPremium = 125.0
print("Ground Shipping Premium: $",costGroundPremium)

#Drone Shipping
if weight <= 2:
  costDrone = weight * 4.50
elif weight <= 6:
  costDrone = weight * 9.00
elif weight <= 10:
  costDrone = weight * 12.00
else:
  costDrone = weight * 14.25

print("Drone Cost Shipping: $", costDrone)