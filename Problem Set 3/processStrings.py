def main():
    string_no = input("Enter a string of digits to process or ’quit’ to stop: ")
    while string_no != 'quit':  #While loop for a sentinel to quit the loop

        processStr(string_no)

        result = getHasRepeatDigit(string_no) #returning a bool and assigning it to result
        if result:
            print('The string has repeated digits')   #If the result is true then print output
        else:
            print('The string has no repeated digits') #If the result is false then print output
            
        getHighest(string_no, result)
        print("")
        
        string_no = input("Enter a string of digits to process or ’quit’ to stop: ")
       
        
def processStr(string_no):  #Giving it the input of the string
    x =[int(i) for i in string_no]  #Getting all the items in the string converted to int and adding them to the list
    print('The sum of the digits in {} is {}' .format(string_no, sum(x)))  #Adding all the items in the list
    
    product = 1
    for f in x:
        product *= f
    print('The product of the digits in {} is {}' .format(string_no, product))  #Looping through list and mulitpling items
    
    
    
def getHasRepeatDigit(string_no):
    x =[int(i) for i in string_no]   
    if len(x) == len(set(x)):    #Compare the size of set and list
        return False             #If size of list & set is equal then it means no duplicates in list
    else:
        return True              #If size of list & set are different then it means yes, there are duplicates in list.
        
                
def getHighest(string_no, result):  
    x =[int(i) for i in string_no]
    highest = max(x)    #Checking for the highest number in the list
    if result == False: #if the result getHasRepeatDigit() is false then print the highest number
        print('The highest digit in the given string is {}' .format(highest))

main()
