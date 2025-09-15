# To specify a string as an f-string, simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and other operations.

age = 24
txt = f"My name is Pappu Roy, I am in {age} years old."
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# We can also use nested f-strings
name = "Pappu Roy"
age = 24
txt = f"My name is {name}, and I am in {age} years old."
print(txt)