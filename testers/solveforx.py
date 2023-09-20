# Solve for x
# x + 4 = 9

# x will always be the 1st value recieved and you only will deal with addition

#recieve the string and split string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    
    num1, num2 = int(num1), int(num2)
    
    return "x = " + str(num2 - num1)
print(solve_eq("x + 4 = 9"))
