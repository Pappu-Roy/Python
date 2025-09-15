# String slicing in Python

x = "Hello, World!"
print(x[2:5]) # print the characters from index 2 to 4
print(x[:5]) # print the characters from the beginning to index 4
print(x[2:]) # print the characters from index 2 to the end
print(x[-5:-2]) # print the characters from index -5 to -3 (last 5th to last 3rd )

print(x.upper()) # convert to upper case
print(x.lower()) # convert to lower case

x = " Hello, World! "
print(x.strip()) # remove any whitespace from the beginning or the end
print(x.replace("e", "a")) # replace a string with another string
print(x.split(",")) # split the string into a list

# String concatenation

a = "Pappu"
b = "Roy"
c = a+b
print(c)
c = a+ " " + b
print(c)
