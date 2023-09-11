# fileName = 'pi_digits.txt'
# with open(fileName) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())
# print(contents)

# with open(fileName) as file_object: 
#     for line in file_object:
#         print(line.rstrip())

# with open(fileName) as file_object:
#     lines = file_object.readlines()

# print(lines)

# for line in lines:
#     print(line.rstrip())

# print(type(lines))
# merhaba = "a\n"
# deneme = "a"
# for i in range(0,2):
#     print(deneme)

# with open(fileName) as file_object:
#     lines = file_object.readlines()
    
# pi = ""
# for line in lines:
#     pi += line.strip()
    
# print(pi)
# print(len(pi))

# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("deneme")
#     file_object.write("I love creating new games.")

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
