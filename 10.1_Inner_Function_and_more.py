
# def fun(msg):           #Outer Function

#     def fun2():         #Inner Function
#         print(msg)
#     fun2()
    
# fun("Hello")

# a = "I am a global var"
# b = "I am also global here"

# def fun():
#     b = "I am enclosing var"

#     def fun2():
#         global a                                  #It is used to change value globally.
#         nonlocal b                                #nonlocal is used to change value in the function.

#         a = "Changing the Global"
#         b = "Changing the nonglobal inside function"

#     fun2()
#     print(b)

# fun()                #Change and print nonglobal b
# print(a)             #Change globally through function 
# print(b)             #Doesn't change globally

# Error Example.
# # Global variable
# global_a = 'geeksforgeeks'

# def outer():
#     def inner():
#         nonlocal global_a # Attempting to reference global variable    #always produce error
#         global_a = 'GeeksForGeeks'  # Modifying the variable
#         print(global_a)
#     inner()
# outer()

def fun1():
    name = "geek"
    
    def fun2():
        name = "Geek"
        
        def fun3():
            nonlocal name  
            name = 'GEEK'  # Modify before using   #Modify the nearest enclosing Scope
            print(name)  
        
        fun3()
        print(name)  # Modified value in fun2()  #fun2 will change
    
    fun2()
    print(name)  # Unchanged value in fun1()     #fun3 will be non affected

fun1()

# Output:
# GEEK
# GEEK
# geek

#Example 2:
def fun1():
    name = "geek"
    
    def fun2():
        nonlocal name              #But this will change fun1() also
        name = "Geek"
        
        def fun3():
            nonlocal name  
            name = 'GEEK'  # Modify before using
            print(name)  
        
        fun3()
        print(name)  # Modified value in fun2()
    
    fun2()
    print(name)  # Unchanged value in fun1()

fun1()