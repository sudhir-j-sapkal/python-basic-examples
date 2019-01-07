x = 20
def printer():
    x=10
    return x

print(x)

#LEGB 
#1. Local(L): Defined inside function/class
#2. Enclosed(E): Defined inside enclosing functions(Nested function concept)
#3. Global(G): Defined at the uppermost level
#4. Built-in(B): Reserved names in Python builtin modules

#Globle
name = "Global Sudhir"

def greet():

    #ENCLOSING
    name = "Enclosing Sudhir"

    def hello():
        #LOCAL
        name = "LOCAL Sudhir"
        print("Hello "+name)

    hello()

greet()

