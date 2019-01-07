print(1 < 2 < 3)
#The above statement checks if 1 was less than 2 and if 2 was less than 3. 
#We could have written this using an and statement in Python:
print(1<2 and 2<3)

#The and is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:
print(1 < 3 > 2)

#The above checks if 3 is larger than both of the other numbers, so you could use and to rewrite it as:
print(1<3 and 3>2)

#It's important to note that Python is checking both instances of the comparisons. We can also use or to write comparisons in Python. For example:
print(1==2 or 2<3)

#Note how it was true; this is because with the or operator, we only need one or the other to be true. Let's see one more example to drive this home:
print(1==1 or 100==1)
