1
def First_function():
   print("This is my first function")
   print("This is my first function")
   print("This is my first function")

First_function()

2
def Second_Function():
    text= "This is my Second Function"
    print(text)
    print(text)
    print(text)

Second_Function()

3
def Third_Function(text):
    print(text)
    print(text)
    print(text)

Third_Function("This is my Third Function")

#  4
#  defining function with if, elif, else statement

def school_calculator(age,name):
    if age > 5:
      print("Get him the admission in higher secondary school")
    elif age == 5 :
      print("Yes,", name ,"can get admission")
    else:
      print("Sorry!", name , "is too little")

school_calculator(15,"Bilal")

#  5

def future_age(age):
    age = age + 10
    return age

print(future_age(10))

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

def function1(*Kid1, Kid2):
    print(Kid1[2], " and ", Kid2)

def function(*kids, **details):
    print(kids)
    print(details)

function("Ali", "Sara", age=10, city="Lahore")




def function2():
    pass            #doesnot give error


#recursion
def tri_recursion(k):                
  if(k > 0):
    result = k + tri_recursion(k - 1)          # 3 + trixxx(2) -> 2 + trixxx(1) -> 1 + trixxx(0) -> return 0(else)
    print(result)                              # now 1 + 0, 2 + 1, 3 + 3
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(3)