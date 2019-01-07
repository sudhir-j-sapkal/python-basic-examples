#Example 
#Creating a function

def my_function():
  print("Hello from a function")

#Calling a Function
my_function()

#How to send parameters
def greetings(name):
    print("Good Morning, "+name)

#Calling a greetings function
greetings("Vinay")

#Returning function 
def addition(num1,num2):
    return num1+num2;

#Calling addition function
#print("Addition =>"+addition(10,20)) #Will give error
result = addition(10,20)
print("Addition of 10 and 20 is {}".format(result))

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without parameter, it uses the default value:

def substraction(num1=0,num2=0):
    print(num1-num2)

substraction(30,20)
substraction();
substraction(50,50)
