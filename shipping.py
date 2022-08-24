
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