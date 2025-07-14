
# f = open("First_File.txt")           #for txt file opening by default
# b = open("First_Binary.txt", 'b')    #for binary opening (binary is used for images) 

with open("Second_File.txt", 'w') as w:                  #also initialize variable like this 'w'
    w.write("This is the File I created.")
    w.close()

with open("Second_File.txt", 'r') as r: 
    print(r.read())
    r.close()