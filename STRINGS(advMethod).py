#.strip()
# remove spaces 

#isnumeric()

# var = "Forest".isnumeric()
# var = "123".isnumeric()
# var = "1F76U2".isnumeric()
# print(var)

# "".join()

# name = " " .join(["Sam", "eats", "his", "lunch", "every day"])
# print(name)

#.split()

# split = "This is my example".split()
# print(split)

# {}.format()

# name = input("Enter your name: ")
# number = len(name)*2
# print("Welcome {name} to our website. Your lucky number is {number}".format(name= name, number= number))

# format with cinditions

# price = 7
# with_tax = price * 9.0
# print("Price: ${:.2f}, With tax: ${:.2f}".format(price, with_tax))

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))