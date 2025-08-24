#writing to a file
#the code opens a file in write mode
#the user inputs the file name
input_file = input("Enter the file name to write to: ")
with open(input_file, "w", encoding="utf-8") as file: 
    file.write("#Lets learn python👾\n")
    file.write("#This is my first file\n")
    file.write("#This demonstrates file handling in python🐍\n")
    file.write("#Especially file writing💾\n")
file.close
if file.write:
    print("File written successfully")
else:
    print("File not written")    
    