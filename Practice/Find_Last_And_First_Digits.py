# Find the first digit of the number
def firstdigit(x):
    # Removeing till the first digit is present
    while x >= 10:
        x = x//10
        # Returns the first digit
    return x
def lastdigit(x):
    # Returns the last digit
    return (x%10)
# Getting the input value from user
a=int(input("Enter A Number: "))
print("The First Digit: ",firstdigit(a))
print("The Last Digit: ",lastdigit(a))
