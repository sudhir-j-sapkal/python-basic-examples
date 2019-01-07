#Create and print a dictionary:
my_car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_car_dict)

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
car_model = my_car_dict["model"]
print(car_model)


#There is also a method called get() that will give you the same result:
player_dict = {
  "cap_id": 101,
  "name": "Virat",
  "highest_score": 183
}
highest_score = player_dict.get("highest_score")
print(highest_score)

#You can change the value of a specific item by referring to its key name:
player_dict["cap_id"] = 175
print(player_dict)

#The dict() Constructor
dict_with_constructor = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(dict_with_constructor)
