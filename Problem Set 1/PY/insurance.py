#Asking the input for the level of the plan
level_of_plan    = input("Enter the input of plan you want from Low, Regular or High: ")

#These are all the set prices for all the levels, types of coverage and status
price_low_single = "$36.25"
price_regular_single = "$48.90"
price_high_single = "$69.80"

price_low_family_with_children = "$98.35"
price_regular_family_with_children = "$136.75"
price_high_family_with_children = "$174.55"

price_low_family_with_no_children = "$56.50"
price_regular_family_with_no_children = "$74.70"
price_high_family_with_no_children = "$99.45"


#IF the level is low
if level_of_plan == "Low":
    status = input("Enter your status, Single or Family:")    #Asking the input for either single or family
    if status == "Single":
        print("Your cost is {}" .format(price_low_single))   #Printing output if the person is single
    else:
        child_nochild = input("Do you have a child, Yes or No?: ")   #Asking the input if the person has children or not
        if child_nochild == 'Yes':
            print("Your cost will be {}" .format(price_low_family_with_children))  #Printing the output if has children
        else:
            print("Your cost will be {}" .format(price_low_family_with_no_children)) #Printing the output if no children
            
#IF the level is MEdium           
if level_of_plan == "Regular":
    status = input("Enter your status, Single or Family:")  #Asking the input for either single or family
    if status == "Single":
        print("Your cost is {}" .format(price_regular_single))  #Printing output if the person is single
    else:
        child_nochild = input("Do you have a child, Yes or No?: ") #Asking the input if the person has children or not
        if child_nochild == 'Yes':
            print("Your cost will be {}" .format(price_regular_family_with_children) ) #Printing the output if has children
        else:
            print("Your cost will be {}" .format(price_regular_family_with_no_children))  #Printing the output if no children
            
            
#IF the level is High            
if level_of_plan == "High":
    status = input("Enter your status, Single or Family:")  #Asking the input for either single or family
    if status == "Single":
        print("Your cost is {}" .format(price_high_single)) #Printing output if the person is single
    else:
        child_nochild = input("Do you have a child, Yes or No?: ")  #Asking the input if the person has children or not
        if child_nochild == 'Yes':
            print("Your cost will be {}" .format(price_high_family_with_children)) #Printing the output if has children
        else:
            print("Your cost will be {}" .format(price_high_family_with_no_children))  #Printing the output if no children
