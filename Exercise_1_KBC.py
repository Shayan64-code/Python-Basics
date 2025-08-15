
# quiz = [
#     {"question": "What is the capital of France", "answer": "Paris"},
#     {"question": "What is 2+2", "answer": "4"},
#     {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"}
# ]

# money = 0
# for item in quiz:                                             #Improved one
#     print("Q:", item["question"])
#     ans = input("Your Answer ")
#     if ans.strip().lower() == item["answer"].lower():
#         money += 100
#         print("Your Answer is correct")
#         print("Add Rs: ", money)
#     else:
#         print("This is wrong")
#         money -= 100
#         print("Deduct Rs: ", money)


# #Example 2:  Using Tuples in list
# quiz = [
#     ("What is the capital of Italy", "Rome"),
#     ("What is 12 x 2", "24"),
#     ("What is the King of Fruits", "Mango")
# ]

# for question, answer in quiz:
#     print("Q:", question)
#     ans = input("Your Answer: ")
#     if ans.strip().lower() == answer.lower():
#         print("Your ans is correct")
#     else:
#         print("This is Wrong")

# #Example with only Dictionary

# quiz = {
#     "What is the color of sky?": "Blue",
#     "What is 10 / 2?": "5",
#     "What is 2 + 5 is": "7"
# }

# for question, answer in quiz.items():
#     print("Q:", question)
#     ans = input("Your Answer: ")
#     if ans.strip().lower() == answer.lower():
#         print("Your ans is correct")
#     else:
#         print("This is Wrong")


#Practice:
KBC = [
    {"question":"What is Capital of France: ","answer":"Paris"},
    {"question":"What is 2+2: ","answer":"4"},
    {"question":"What is the King of Fruits: ","answer":"Mango"}
]

money = 0
for x in KBC:
    print(x["question"])
    ans = input("Give Your Answer: ")
    if ans.strip().lower()==x["answer"].strip().lower():
        print("Your answer is correct!!!")
        money +=100                          #money/or every other variable cannot assign directly in print or
        print("Money added Rs 100:", money)   #other like this money+=100.
    else:
        print("You are wrong")
        money -=100
        print("Money deducted Rs 100:", money) 
print("Money Taken Home:",money)

# questions = [
#     ["What is Capital of France: ","Paris"],
#     ["What is 2+2: ","4"],
#     ["What is the King of Fruits: ","Mango"]
# ]