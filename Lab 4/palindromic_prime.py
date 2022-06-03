def main():
    count = 0
    PRIMES_PER_LINE = 10
    checkNum = 1
    number = int(input("How many palindromic primes should be computed?: "))
    while count < number:
        checkNum += 1
        if  isPrime(checkNum) and isPalindrome(checkNum):
            print('{:>5d} '.format(checkNum), end='')
            if (count + 1) % PRIMES_PER_LINE == 0:
                print()
            count +=1

def reverse(number):
    reverse = 0
    while number != 0:
        lastDigit = number % 10
        number //= 10
        reverse = (reverse * 10) + lastDigit
    return reverse

def isPrime(n):
    divisor = 2
    while divisor <= n / 2:
        if n % divisor == 0:    # if True number NOT prime
            return False
        divisor += 1
    return True


def isPalindrome(num):
    if (reverse(num) == num):
        return True
    else:
        return False

if __name__ == '__main__':
    main()