# Error handling in python 
try:
    with open("Mark1.xlsx", "r") as f: 
     content = f.read()
except FileNotFoundError:
    print("The file was not found.") 