print('--- create a Set ---')
#create a Set
this_set = {"apple", "banana", "cherry"}
print('this_set:', this_set)

#get the number of items in a set
print('length of this_set:', len(this_set))

#create a set contain different data types
set1 = {"duc", 22, True, "nguyen"}
print('set1:', set1)

#return type of a set
print('type of a set:', type(set1))

#use the set() constructor to make a set
new_set = set(['Nguyen', 'Van', 'Duc', 22])
print('new_set:', new_set)

#access Set items
print('\n--- access Set items ---')
#loop through the set, and print the values:
print('value of new_set:')
for item in new_set:
    print(item)

#check if 'Duc' is present in the set
print('check "Duc" is present in new_set:', 'Duc' in new_set)

## add items
print('\n--- Add items to a set ---')
new_set.add('HUST')
print('add "HUST" to new_set:', new_set)

#Add items from another set into the current set, use the update() method
set2 = {'Sinh', 'vien'}
new_set.update(set2)
print('add "set2" into new_set:', new_set)

print('\n--- remove Set items ---')
#to remove an item in a set, use the remove(), or the discard() method
str1 = "vien"
str2 = "Sinh"
if str1 in new_set and str2 in new_set:
    new_set.remove(str1)
    new_set.discard(str2)
    print('remove "{str1}" and "{str2}" in new_set:'.format(str1 = str1, str2 = str2), new_set)
else:
    print('new_set has not "{str1}" or "{str2}".'.format(str1 = str1, str2 = str2))

#remove the last item by using the pop() method
new_set.pop()
print("remove the last item of new_set:", new_set)

#remove all item in new_set, use the clear() method
new_set.clear()
print('remove all item in new_item:', new_set)

#the del keyword will delete the set completely
#del new_set

#Join Sets
print('\n--- Join Sets ---')
set1 = {"nguyen", "van", "duc"}
print('set1:',set1)
set2 = {1, 2, 3}
print('set2:', set2)
set3 = set1.union(set2)
#set1.update(set2)
print('join set1 and set2:', set3)

#keep ONLY the Duplicates
set4 = {"duc", 22}
set5 = set1.intersection(set4)
#set4.intersection_update(set1)
print('keep the items that exist in both set4, and set set1', set5)

# (set1 or set4) - (set1 and set4) - with the symmetric_difference() method
set6 = set1.symmetric_difference(set4)
print('return the contains only the elements that are NOT in set1 and set2:', set6)

