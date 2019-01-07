#Create Tuple
my_tuple = ("2","2.55","Sudhir",2.4,556);
print(my_tuple)

#Access item in tuple
print(my_tuple[1]);

#Change the tuple value(Once a tuple is created, you cannot change its values. Tuples are unchangeable)
# my_tuple[1] = "blackcurrant"
# The values will remain the same:

# You can't do following operations on tuble 
  # 1. append,
  # 2. insert, 
  # 3. delete, 
  # 4. remove, 
  # 5. pop  

#Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
bikes_tuple = ("Triump Tiger","Kawaski Ninza","MV Augusta","Tiger 800 XC")
for bike in bikes_tuple:
  print(bike)

#Check if Item Exists(To determine if a specified item is present in a tuple use the in keyword)
if "Triump Tiger" in bikes_tuple:
  print("Yes, 'Triump Tiger' bike is in the bikes tuple")

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.

bikes_tuple = tuple(("Triump Tiger","Kawaski Ninza","MV Augusta","Tiger 800 XC"))
print(bikes_tuple)

#Methods
# 1. count(value) -> Returns the number of times a specified value occurs in a tuple
temp_tuple = (1, 3, 5, 8, 7, 5, 4, 5, 8, 5)
count_of_five = temp_tuple.count(5)
print(count_of_five)

#2. index() - Search for the first occurrence of the value 8, and return its position:
index_of_eight = temp_tuple.index(8)
print(index_of_eight)

#The index() method raises an exception if the value is not found.
