#Create a Computation class with a default constructor (without parameters) allowing it to perform various calculations 
# on integer numbers.

#Create a method called Factorial() which allows you to calculate the factorial of an integer. 

#Test the method by instantiating the class.

#Create a method called Sum() allowing you to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.

#Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.

#Create  a method called testPrims() allowing you to test if two numbers are prime between them.

#Create a tableMult() method which creates and displays the multiplication table of a given integer. 
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

#Create a static listDiv() method that gets all the divisors of a given integer on a new list called  Ldiv. 

#Create another listDivPrim() method that gets all the prime divisors of a given integer.
class Computation:
    def __init__(self):
        pass
    
    
    def factorial(self,n):
        if n < 0:
            print("Cannot create a factorial for a negative number")
        elif n == 0 or n ==1:
            return 0
        else:
            reults = 1
            for i in range(2,n+1):
                reults *= i
            return reults
        
        
    def sum_of_integers(self,n):
        count = 0
        if n<0:
            return "Invalid"
        else:
            for i in range(1,n+1):
                count += i
            return count
        
        
    def check_prime(self,n):
        if n <= 1:
            return False
        else :
            for i in range(2,int(n**0.5) +1):
                if n %i  == 0:
                   return False
            return True
        
        
    def check_prime_numbers(self,m,n):
        prime = []
        for nums in range(m,n+1):
            if self.check_prime(nums):
                prime.append(nums)
        return prime
        
    
    def create_table_mult(self,n):
        results = []
        for x in range(1,n):
            entry = f" {n} * {x} = {n*x}"
            results.append(entry)
        return results 
    
    
    
        
        
        
        
            
        
        
        
            
                
            
            

