
fruits = ["oranges", "grapes", "bananas"]

# open file with read write mode and write above fruits to file (need conversion to str)

# with open("fruits.txt","w+") as f:
 #   f.write(str(fruits))


# open file with read write mode and append some words to file

# with open("fruits.txt","a+") as f:
 #   f.write(str(fruits))


# read from file
with open("fruits.txt","r+") as f:
    print(f"{f.read()}")
