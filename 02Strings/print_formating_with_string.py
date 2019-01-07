print("This is print formating, So I am gonna Insert String here {}".format('INSERTED'));

#This will be usefull when you wanted to do something like below 
print("Hey {} Your college {} is Super Awesome !".format('Sudhir',"TKIET"))

#Here the replacement order can be passed in interpolation
print("My Name is {1} {0}".format('Sudhir','Sapkal'))

#We can also assign a variable names and replace the string accordingly

print("My Name is {first_name} {last_name}".format(first_name='Sudhir', last_name='Sapkal'))

#f formatted string litterls
name = 'Sudhir'
age = 25
print(f'{name} is  {age} years old');
