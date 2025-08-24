# 
# x = 120
# y = 200
# z = 300
# def add(x, y, z):
#     return x + y + z
# print(add(x, y, z))

# file = open("readme.md", "a", encoding="utf-8")
# print(file.read())
# file.close()

with open("readme.md", "a", encoding="utf-8") as file: 
    file.write("#Welcome to PLP\n")
    
    