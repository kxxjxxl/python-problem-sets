from random import randint

dice_Rolls = int(input("How many times should we roll the dice? "))
x = 1
even = 0
odd = 0


#Randomizing the dices and adding them
while x <= dice_Rolls:
    diceA = randint(1, 6)
    diceB = randint(1, 6)
    result = diceA + diceB
    print("You rolled {} + {} = {}" .format(dice_A,  dice_B, result ))    #Output of the dice rolled and their sum
    x += 1


#Checking to see if the number is odd or even.
    if result % 2 == 0:
        even += 1
        even_Rolls = (even / dice_Rolls) * 100
    else:
        odd += 1
        odd_Rolls = (odd / dice_Rolls) * 100


#Output of the percentage of evens and odds rolled
print("An even value was rolled {:.2f}% of the time." .format(even_Rolls))
print("An odd value was rolled {:.2f}% of the time." .format(odd_Rolls))