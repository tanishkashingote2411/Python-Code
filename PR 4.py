substring = input("Enter the secret message: ")
string = input("Enter the coded message: ")

if substring in string:
    print("Found")
else:
    print("Not Found")