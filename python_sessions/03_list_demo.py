# Imagine a container holding multiple objects
# Collection in python is like container, which holds multiple objects 
# and provide way to access and loop through those objects

# list is used to store multiple items in single variable and is defined by square brackets
# mutable meaning, elements inside list can be changed
# declared with square brackets

fruits = ["orange","grapes","apple","orange"]



# declare list of type numbers


# duplicates in list


# items by index , first and second last (last count starts with -1 and then decrease)

fruits[0] = "avacado"
print(f"{fruits[0]}")


# replace items in list, so mutables

# insert item in list at a index, insert always take index as first argument

print(f"{fruits}")

fruits.insert(1,"banana")

print(f"{fruits}")

# append item to end

# remove item by name
fruits.remove("orange")
print(f"{fruits}")


# if there are duplicates, first occurence will be removed

# iterating with for loop


#for  single_fruits  in fruits:
#    print(f"{single_fruits}")

# looping with index and break and continue with fruit_name
# can be done using while loop and comparing index with length

index = 0
while index < len(fruits):
    fruits_name = fruits[index]
    index +=1
    
    if fruits_name == "grapes":
        continue
    
    print(fruits_name)