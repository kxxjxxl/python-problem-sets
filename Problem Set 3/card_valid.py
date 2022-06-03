
#Defining Main fucntion to call all functions and check if card is valid or not
def main():
    card_number = int(input("Enter the credit card number: "))
    double_even_digits = sumDoubleEvenLocation(card_number)
    even = getDigit(double_even_digits)       #Outputs the even number
    odd = sumOddLocation(card_number)         #Outputs the odd number
    total = total_sum(even, odd)              #Sums the even and odd
    result = isValid(card_number, total)      #Outputs the validty by checking len and divisble by 4
    if result:
        print('The card number {} is valid'.format(card_number))
    else:
        print('The card number {} is not valid'.format(card_number))

#Checks the validity of the card by checking for the length and if its divisible by 10
def isValid(card_number, total):
    if getSize(card_number) >= 13 and getSize(card_number) <= 16 and total % 10 == 0:
        if isPrefix(card_number, 4) or isPrefix(card_number, 5) or isPrefix(card_number, 6)  or isPrefix(card_number, 37): 
            return True
        else:
            return False
#Take the digits at even location and returns a list of the digits doubled at even location
def sumDoubleEvenLocation(card_number):
    card_num = [int(i) for i in str(card_number)]
    even_digits = card_num[-2::-2]
    double_even_digits = [] 
    for ele in even_digits: 
        double_even_digits.append(ele + ele)
    return double_even_digits

#Takes the list of the double digits and returns a single digits if there are two digits
def getDigit(double_even_digits):
    sum_single = 0
    for num in double_even_digits:
        if num > 9:
            num = num - 9
            sum_single += num
        else:
            sum_single += num
            
    return sum_single

#Take the digits at odd location and returns a list of the digits at odd location
def sumOddLocation(card_number):
    card_num = [int(i) for i in str(card_number)]
    odd_digits = card_num[-1::-2]
    sum_odd = 0
    for i in odd_digits:
        sum_odd += i
    return sum_odd

#gets size of the cards number
def getSize(d):
    num = str(d)
    count = len(num)
    return count

# a fuction to return the first k digits from the card number
def getPrefix(card_number , k):
    if card_number > k:
        c_string = str(card_number)
        prefix = c_string[0:k]
        int_p = int(prefix)
        return int_p
    else:
        return card_number

#Takes the parameter and getPrefix to if it has the given len
def isPrefix(card_number, d):
    prefix_ = False 
    if getPrefix(card_number, getSize(d)) == d:
        prefix_ = True
        return prefix_
    else:
        return prefix_ 

#To sum the output of even and odd
def total_sum(even, odd):
    total = even + odd
    return total
    
 
            
main()
