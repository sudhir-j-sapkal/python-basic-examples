my_list = ["1", 2, "hello"]
print(my_list)

#You access the list items by referring to the index number:
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[1])

#To change the value of a specific item, refer to the index number:

fruit_list[1] = "blackcurrant"
print(fruit_list)

#You can loop through the list items by using a for loop:
for x in fruit_list:
  print(x)

#To determine if a specified item is present in a list use the in keyword:

if "apple" in fruit_list:
  print("Yes, 'apple' is in the fruits list")

#To determine how many items a list have, use the len() method:

print(len(fruit_list))

#To add an item to the end of the list, use the append() method:

fruit_list.append("orange")
print(fruit_list)

#To add an item at the specified index, use the insert() method:

fruit_list.insert(1, "orange")
print(fruit_list)

#There are several methods to remove items from a list:
fruit_list.remove("blackcurrant")
print(fruit_list)

fruit_list.pop()
print(fruit_list)

# To delet item in list
del fruit_list[0]
print(fruit_list)

#The clear() method empties the list:
fruit_list.clear()
print(fruit_list)

#The del keyword can also delete the list completely:
fruit_list["23","44","66"]
del fruit_list
# print(fruit_list) If we try to execute this it will give error of undefine list

#It is also possible to use the list() constructor to make a list
fruit_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(fruit_list)

#Python has a set of built-in methods that you can use on lists.


