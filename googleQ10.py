# Question 4
# # Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.


def squares(start, end):
    return [ n**2 for n in range(start, end+1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

