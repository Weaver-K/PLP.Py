# Error handling in python 
#First input file to be received
input_file = input("Enter the file name: ")
#the code runs to read the file
try:
    with open(input_file, "r") as f: 
     content = f.read()
except FileNotFoundError:
    print("The file was not found.")
else:
     print("File retrieved successfully") 