fruit_list = ["apple","mango"]
my_list = ["divya",4,fruit_list]
print(my_list)
fruit_list.append('abc')
print(fruit_list)
print(my_list)
for x in fruit_list:
    if "apple" in fruit_list:
        fruit_list.remove("apple")


