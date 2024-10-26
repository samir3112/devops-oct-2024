import json

# both dict and json looks same (There is quotes around json variable to represent it as str)
# but dictionary is built in, in-memory data structure to hold key-values

# json on other hand represent data in text format, mostly for data tranfer over network
# json.loads() function is used to parse json string into python dictionary to perform dictionary like operations

# sample dictionary and print type

fruits_dict = {"oranges":100, "grapes":50}
fruits_str = '{"oranges":100, "grapes":50}'

print(f"{type(fruits_dict)}")
print(f"{type(fruits_str)}")




# sample json string (enclosed in single quotes) and print type
# the type will actually be string but this is how data is exchanged between client-server


# convert to dict with json.loads and print type


fruits_json = json.loads(fruits_str)
print(f"{type(fruits_json)}")

fruits_json["banana"] = 100
print(f"{fruits_json}")