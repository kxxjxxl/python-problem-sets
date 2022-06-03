#First take the input of all the currencies avalible and convert them to Maruvian 

m = int(input('Please enter the number of Maruvian: '))  #m = Maruvian
c = int(input('Please enter the number of Caruvian: '))  #c = Caruvian            
t = int(input('Please enter the number of Taruvian: '))  #t = Taruvian
p = int(input('Please enter the number of Paruvians: ')) #p = Paruvian
friend = int(input('Number of friends you have: '))

CtoM = (c*12)/24  #The way to convert Caruvian to Maruvian is to multiply Caruvian by 12 and then divide it by 24
TtoM = (t*6)/24   #The way to convert Taruvian to Maruvian is to multiply Taruvian by 6 and then divide it by 24
PtoM = (p//24)    #The way to convert Taruvian to Maruvian is to floor divide it by 24

total_m = m + CtoM + TtoM + PtoM
total_mR = round(total_m) #This is to round it off to whole number

#Output for the total Maruvians converted
print("Marvin has {} Maruvians in total" .format(total_mR))
      
friends = total_m/(friend+1)  #Using floor division to equally seprate the Maruvian between each friend
friends_r = round(friends)    #This is to round it off to whole number

#Output for how much Maruvian each friend gets
print("Marvin then takes {} Maruvian(s) for himself and gives {} Maruvian(s) to his friends each" .format(friends_r, friends_r))

jar = total_m%friends_r #Using Mod to find the remainder of the Maruvian that goes into the jar
pR = round(p)           #This is to round it off to whole number  

#Output for the remaining Maruvians that goes back into the jar
print("Marvin then puts the remaining {} Maruvian(s) and {} Paruvian(s) back in the jar " .format(jar, pR))
