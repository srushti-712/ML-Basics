#assignment 2 - Problem 1

#Complex class to calculate sum, difference and product of 2 user entered complex numbers
class Complex:
    def __init__(self,a,b):
        self.cnum1 = a
        self.cnum2 = b
        

    def add_cnum(self):
        print(f"Addition of {self.cnum1} and {self.cnum2}: ",self.cnum1+self.cnum2)

    def diff_cnum(self):
        print(f"Subtraction of {self.cnum1} from {self.cnum2}: ",self.cnum2-self.cnum1)

    def mul_cnum(self):
        print(f"Multiplication of {self.cnum1} and {self.cnum2}: ",self.cnum1*self.cnum2)

    def perform_op(self):
        self.add_cnum()
        self.diff_cnum()
        self.mul_cnum()
        
        

#Driver Code
real1, imag1 = list(map(int,(input("Enter the space separated real and imaginary parts of one complex number: ").strip().split())))
real2, imag2 = list(map(int,(input("Enter the space separated real and imaginary parts of another complex number: ").strip().split())))
complex_num1 = complex(real1,imag1)
complex_num2 = complex(real2,imag2)

C = Complex(complex_num1,complex_num2)
C.perform_op()

