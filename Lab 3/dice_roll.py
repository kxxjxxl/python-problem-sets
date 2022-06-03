from random import *
dice_rolls = int(input("How many times should we roll the dice?: "))
even = 0
odd = 0
for t in range(dice_rolls):
    dice_a = randint(1,6)
    dice_b = randint(1,6)
    result = dice_a + dice_b
    
    if result % 2 == 0:
        even += 1
        even_rolls = (even/dice_rolls) * 100
    else:
        odd += 1
        odd_rolls = (odd/dice_rolls) * 100
   

     
    print("You rolled {} + {} = {}" .format(dice_a,  dice_b, result ))
    
    
print("An even value was rolled {:.2f}% of the time." .format(even_rolls))
print("An odd value was rolled {:.2f}% of the time." .format(odd_rolls))
