#How to create set
my_set = {"Virat", "Rohit", "KL Rahul"}
print(my_set)

#What if we give duplicates
my_set_with_duplicates = {"Virat", "Rohit", "Virat","Rohit", "Shikhar","Rohit"}
print(my_set_with_duplicates)

#Loop through items
my_players = {"Haydan","Sachin","Virat","Michel Bevan","Johnty Rohdes", "MS Dhoni"}
for player in my_players:
  print(player)

#To add one item to a set use the add() method.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#To add more than one item to a set use the update() method.
bikes = {"Tiger", "Kawaski", "Triump"}
bikes.update(["splendar", "m80", "luna"])
print(bikes)

#The set() Constructor
temp_set = set(("1", "2", "3")) # note the double round-brackets
print(temp_set)

#Get the Length of a Set
#To determine how many items a set have, use the len() method.
#To remove an item in a set, use the remove(), or the discard() method.
#If the item to remove does not exist, remove() will raise an error.
#If the item to remove does not exist, discard() will NOT raise an error.
#You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

