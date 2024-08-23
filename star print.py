# Example of a nested loop to print a pattern

rows = 5

# Outer loop for rows
for i in range(rows):
    # Inner loop for columns
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row
