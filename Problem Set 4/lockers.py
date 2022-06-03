number_of_lockers = 100
lockers = [False] * number_of_lockers # False is closed, True is open

#Running a nested loop to open the lockers for their number and change it
for student_number in range(1,number_of_lockers+1):
    for locker_number in range(0,number_of_lockers):
        if (locker_number+1) % student_number == 0: # if the locker number is exactly divisible by student number
            lockers[locker_number] = not lockers[locker_number] # flip 0 to 1 and vice versa



#list to count the number of True and their positions in the list.
opened = []
count = 1
for x in lockers:
    if x == True:
        opened.append(count)
        count += 1
    else:
        count += 1
#Output the list of the opened locker numbers
print("The lockers are opened at positions: {}" .format(opened))
