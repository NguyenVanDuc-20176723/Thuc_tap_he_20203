# create a Dict
print('--- create a Dict ---')
this_dict = {
    "brand": "Ford",
    "model": "mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

print(this_dict)
print("year:", this_dict['year'])

# copy dict
mydict = this_dict.copy()

# length of Dict
print('length of this_dict:', len(this_dict))

# get the value of the "model" key
value_of_model = this_dict.get("model")
print(value_of_model)

# get a list of the keys
key_of_this_dict = this_dict.keys()
print('key of this_dict:', key_of_this_dict)

# get a list of the values
value_of_this_dict = this_dict.values()
print(value_of_this_dict)

# get a list of the key:value pairs
items_of_this_dict = this_dict.items()
print(items_of_this_dict)

# update or add the 'year' og the this_dict by using the update() method
this_dict.update({"year": 2020})
this_dict.update({"name": "duc"})
print(this_dict)

# remove the item in a Dict
this_dict.pop('model')
this_dict.popitem()
del this_dict['year']
print(this_dict)

# remove all the item in a Dict
this_dict.clear()
print(this_dict)

# loop dict
for x in mydict:
    print(x, mydict[x])
    