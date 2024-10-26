# another data structure that allows us to interact by 
# associating key and value together

# declaring and printing


fruits = {"oranges":85, "apples":100}



# access by key

print(f"{fruits['oranges']}")

# changes value of a element

fruits["oranges"] = 200
print(f"{fruits['oranges']}")


# adding element

fruits["banana"] = 80


# list of dictionaries and printing

fruits_list = [
    
    {"fruit":"apple", "price" : 80},
    {"fruit":"banana", "price" : 100},
    {"fruit":"orange", "price" : 110}
    
]


print(f"{fruits_list[0]}")

# take element from list of dictionary by index