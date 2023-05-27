def remove_one_digit_greedy(num):
    # Convert the number to a string for easier manipulation
    num_str = str(num)
    
    # Initialize the maximum number with the input number
    max_num = num
    
    # Iterate through each digit of the number
    for i in range(len(num_str)):
        # Remove the current digit from the number
        new_num_str = num_str[:i] + num_str[i+1:]
        
        # Convert the modified string back to an integer
        new_num = int(new_num_str)
        
        # Update the maximum number if the new number is greater
        if new_num > max_num:
            max_num = new_num
    
    # Return the largest number after removing one digit
    return max_num

# Get input from the user
num = int(input("Enter a number: "))

# Call the function to find the largest number
largest_num = remove_one_digit_greedy(num)

# Print the result
print("Largest number after removing one digit from", num, "is:", largest_num)
