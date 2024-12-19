#homework
class Calculator:
    def calculate(self,a=None, b=None, c=None):
        if not all(type(i) in (int,float) for i in (a,b,c) if i is not None):
            raise ValueError("All arguements must be integers or floats.")
        if b is None and c is None:
            return a ** 2
        elif c is None:
            return a + b
        else:
            return a * b * c


calc = Calculator()
try:
    print(calc.calculate(3))           
    print(calc.calculate(5, 9))        
    print(calc.calculate(2, 5.66,83.9))     
    print(calc.calculate(3,"D",5.66))

except ValueError as e:
    print(e)
