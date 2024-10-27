'''
to catch exceptions gracefully and do something meaningful
try except block is needed for exception handlin
try will contain block of code, which can fail
except will contain code, to be executed if code fails
'''

# reading non existing file with system throwing exception
# lets use open function instead with open to demostrate in read mode
# statements after error/problematic statement are not executed


#with open("non existing", "r+") as f:
#    f.read()

f = None

try:
    f = open("non-existint-file.txt")
except IOError as ioe:
    print(f"Caight Exception in prog {ioe}")
except Exception as ex:
    print(f"Caight Exception in prog {ex}")
finally:
    print(f"finally block")
    if f:
        f.close()
    

print(f"after excpetion")


# catching exception


# catching more specific exception


# finally
