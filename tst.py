import inspect
def generate_exponent_func(power):
    
    def raised_to(no):
        return no ** power
        
    return raised_to

square = generate_exponent_func(2)

cube = generate_exponent_func(3)

print(square(4))
print(cube(5))