# Input string
input_string = input("Enter a string: ")

# Initialize variables to point to the start and end of the string
start = 0
end = len(input_string) - 1

# Variable to track if the string is a palindrome
is_palindrome = True

# Loop through the string
while start < end:
    # Compare characters at the start and end
    if input_string[start] != input_string[end]:
        is_palindrome = False
        break
    # Move the pointers
    start += 1
    end -= 1

# Output the result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
