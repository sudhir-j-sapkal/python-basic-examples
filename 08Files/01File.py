f = open("demo.txt", "r")
#print(f.read())

#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many character you want to return:

#print(f.read(5))

#Read Lines
#You can return one line by using the readline() method:
print(f.readline())
