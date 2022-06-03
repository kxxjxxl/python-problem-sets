class Complex:
    
    #Intializing the variables
    def __init__(self, real = 0, imaginary = 0):
        self.real = real
        self.imagi = imaginary
    
    #Method to get the real part of the complex number
    def getReal(self):
        return print(self.real)
    
    #Method to get the imaginary part of the complex number
    def getImaginary(self):
        return print(str(self.imagi) + "i")
    
    #return real and imaginary using an index operator
    def __getitem__(self,index):
        if index==0:
            return self.real
        else:
            return self.imagi
    
    #return the "a+bi" for of complex number
    def __str__(self):
        if self.imagi == 0:
            return str(self.real)
        else:
            if self.imagi < 0:
                return str("{} - {}" .format(str(self.real), str(self.imagi*-1)))
            else:      
                return ("{} + {}i" .format(str(self.real), str(self.imagi)))
    
    #add a complex number to this complex number
    def __add__(self, secondEq):
        real = self.real + secondEq[0]
        imaginary = self.imagi + secondEq[1]
        return Complex(real, imaginary)
    
    #subtract a complex number to this complex numbe
    def __sub__(self, secondEq):
        real = self.real - secondEq[0]
        imaginary = self.imagi - secondEq[1]
        return Complex(real, imaginary)
    
    #multiply a complex number to this complex numbe
    def __mul__(self, secondEq):
        real = self.real * secondEq[0] - self.imagi * secondEq[1]
        imaginary = self.imagi * secondEq[0] + self.real * secondEq[1]
        return Complex(real, imaginary)
    
    #divide a complex number to this complex numbe
    def __truediv__(self, secondEq):
        real = (self.real * secondEq[0] + self.imagi * secondEq[1]) / (secondEq[0]**2 + secondEq[1]**2)
        imaginary = (self.imagi * secondEq[0] - self.real * secondEq[1] ) / (secondEq[0]**2 + secondEq[1]**2)
        return Complex(real, imaginary)
    
    #get the absolute value of the complex number
    def absoluteValue(self):
        return int(self.real**2 + self.imagi**2)**0.5

    
    
#main function to test the variables   
def main():
    real = int(input("Please enter the real part of your first complex number: "))
    imaginary = int(input("Please enter the imaginary part of your first complex number: "))
    c1 = Complex(real, imaginary)
    print("Your first complex number is {}" .format(c1))
    print()
    real = int(input("Please enter the real part of your second complex number: "))
    imaginary = int(input("Please enter the imaginary part of your second complex number: "))
    c2 = Complex(real, imaginary)
    print("Your second complex number is {}" .format(c2))
    print()
    print("The addition of {} and {} is {}".format(c1,c2,str(c1 + c2)))
    print("The subtraction of {} and {} is {}".format(c1,c2,str(c1 - c2)))
    print(("The multiplication of {} and {} is {}".format(c1,c2,str(c1 * c2))))
    print(("The division of {} and {} is {}i".format(c1,c2,str(c1 / c2))))
    print("The absolute value of c1 is {:.2f}" .format(c1.absoluteValue()))
    print("The absolute value of c2 is {:.2f}" .format(c2.absoluteValue()))
    print()
    c1.getReal()  #Testing the getReal method of the class
    c1.getImaginary() #Testing the getImaginary method of the class
    
    
main()  
    
