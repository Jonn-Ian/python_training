#create a dictionary
person = {"name": "alice", "age": 3, "city": "new york"}
#decalre a key that want to get in dictionary by using tuple
key = ("name", "age")

#loop through the person to get the values in keys using tuple 
# and .get to get the values in dictionary 
values = tuple(person.get(val) for val in key)
print(values)


###################################################################
#convert tuple to list and modify the first element
keys = ("keys", 22, "values")
tuples_to_list = list(keys)
tuples_to_list[0] = "alice"

for i in range(len(tuples_to_list)):
    print(tuples_to_list[i])