# Drawing Patterns with Nested Loops
# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))
# Initiate a row counter
row = 0
# Draw the pattern using nested loop
while row < size:
    for _ in range (size):
        print("*", end="")
        print() #to move to the next line
        row +=1
