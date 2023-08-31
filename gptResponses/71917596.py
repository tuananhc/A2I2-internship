# You're on the right track! You just need to combine the two pieces of code. Here's how you can do it:

# ```python
total_sum = 0
while True:
    inp = input("Enter a number: ")
    if inp == '0':
        break
    
    try:
        num = int(inp)
    except ValueError:
        print("Not an integer, try again.")
    else:
        total_sum += num

print("The total sum of the numbers is {}".format(total_sum))
# ```

# In this code, we first initialize the `total_sum` variable to 0. Then, we enter an infinite loop using `while True`. Inside the loop, we ask the user for input and check if it is equal to '0'. If it is, we break out of the loop. Otherwise, we try to convert the input to an integer. If it is not a valid integer, we print an error message and continue the loop. If it is a valid integer, we add it to the `total_sum` variable. Finally, after the loop, we print the total sum.