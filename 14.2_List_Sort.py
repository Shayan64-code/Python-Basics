############                                                  Sort List

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()                                      #By default order a to z
# print(thislist)

thislist2 = [100, 50, 65, 82, 23]
# thislist2.sort()                                     #By default order ascending
# print(thislist2)

# thislist.sort(reverse= True)                      #This is used to reverse order 
# thislist2.sort(reverse= thislist)                 #reverse by indicating the thislist

# print(thislist)
# print(thislist2)

# def myfunc(n):                           #This function tells to print numb that is closest to 50
#     return abs(n - 50)                 

# thislist2 = [100, 50, 65, 82, 23]

# thislist2.sort(key= myfunc)
# print(thislist2)

# words = ["banana", "fig", "apple", "kiwi", "cherry"]

# words.sort(key= len)                    #Sort according to the length of words
# print(words)

# numbers = [100, 50, 65, 82, 23, 71]

# # Sort by closeness to 70
# numbers.sort(key=lambda n: abs(n - 70))     #Another way but it uses lambda(It is used when we donot want to define a function)
# print(numbers)

# fruits = ["apple", "banana", "cherry", "kiwi"]

# # Sort by last character of each word
# fruits.sort(key=lambda word: word[-1])                  #a to z order using the last word of Item.
# print(fruits)

thislist = ["banana", "Orange", "Kiwi", "cherry"]      #case sensitive first A to Z than a to z
# thislist.sort()
# print(thislist)

# thislist.sort(key= str.lower)                          #Case insensitive using lower(doesnot lower alphabets)
# print(thislist)

thislist.reverse()                                       #Just revese the whole list
print(thislist)
