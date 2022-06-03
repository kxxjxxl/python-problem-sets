#Set price for meals and the tax rate
adult_meal_price = 40.50
child_meal_price = 20.25
tax_rate = 15


#Input asking for all the inputs
number_adult_meals = int(input("Enter the number of adults meals purchased: "))
number_child_meals = int(input("Enter the number of child meals purchased: "))
gratuity           = int(input("Enter the percentage of gratuity you want to apply: "))
deposit_paid       = float(input("Enter the deposit amount you have paid: "))


#Calculations to get the price of the adult and child meal
adult_meal_cost =  (number_adult_meals * adult_meal_price)
child_meal_cost =  (number_child_meals * child_meal_price)

#Calculations to get the tax and gratuity costs 
meal_cost     = adult_meal_cost + child_meal_cost      
tax_cost      = (tax_rate/100) * meal_cost
gratuity_cost = (gratuity/100) * meal_cost
total_amount  = meal_cost + gratuity_cost + tax_cost 
amount_owing  = total_amount - deposit_paid

#Printing all the stuff out
print("Meal Cost:     ${:.2f}"     .format(meal_cost))
print("Gratuity Cost: ${:.2f}" .format(gratuity_cost))
print("Tax Cost:      ${:.2f}"      .format(tax_cost))
print("Total Amount:  ${:.2f}"  .format(total_amount))
print("Deposit Paid:  ${:.2f}"  .format(deposit_paid))
print("Amount owing:  ${:.2f}"  .format(amount_owing))
