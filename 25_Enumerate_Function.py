
# Marks = [10, 38, 72, 98, 54, 21, 1, 4]

# for Index, marks in enumerate(Marks):
#     print(Index, ":", marks)
#     print("Shayan, Awesome") if Index == 3 else None

# Fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

# for Index, fruits in enumerate(Fruits, start = 1):      #apple will count from 1
#     print(Index, ":", fruits)

Marks = [10, 38, 72, 98, 54, 21, 1, 4]

for Index, marks in enumerate(Marks):
    print(Index, ":", marks)
    if Index == 3:
        print(marks*2)
    
