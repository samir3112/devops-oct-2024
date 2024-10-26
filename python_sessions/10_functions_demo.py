# function is block of code to perform a particular task
# consider calculator , I can club code for task like addition, deletion, etc., in blocks, called as function
# we already seen print() func

# declaring callable variable i.e., function



# defining function , won't execute anything, the function need a call to execute

# functions with parameters




# named arguments, called with no values, called with any value
# if there is 1 parameter or fewer parameters with defalut value, they should be placed at the end of parameters list


# collecting number of parameters with *args



# global variable and local variable

orange_price = 50

def discounted_price(discount):
    orange_price = 80
    return (1 - discount)  * orange_price

# global variable declared and used in function without having local vaariable
# global variable declared and local variable used in function with same name
# global variable declared and declaring same global variable inside function
