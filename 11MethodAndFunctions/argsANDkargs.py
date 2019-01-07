def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(50,60))

#args - python treats agrs as tuples
#args is just name , it can be anything , just make sure it should followed with '*' symbol

def myfuncforkargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfuncforkargs(fruit="apple",icecream="butterscotch")

#kargs - means it is sending the argubments as key word arguments called as dictonories 

#we can use both at same time

def my_function(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

my_function(10,20,30,food="eggs",fruit="apple")
