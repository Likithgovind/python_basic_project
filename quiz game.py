#quiz game
questions=("What is the correct file extension for Python files?",
          "Which of the following is the correct way to create a variable in Python?",
          "What is the output of print(2 ** 3)?",
          "Which of these data types is immutable in Python?",
          "What will print(type(5.0)) output?")
options=(("a. .pyth","b. .python","c. .py","d. .pt"),
         ("a. var x = 5","b. x = 5","c. int x = 5","d. x <- 5"),
         ("a. 6","b. 8","c. 9","d. 5"),
         ("a. List","b. Set","c. Dictionary","d. Tuple"),
         ("a. int","b. float","c. double","d. str"))
answers=("c","b","b","d","b")
guesses=[]
score=0
number=0


for question in questions:
    print("==============================================================================")
    print(question)
    for option in options[number]:
        print(option)
    guess=input("enter your option (a,b,c,d):")
    guesses.append(guess)
    if guess==answers[number]:
        print("CORRECT")
        score+=2
    else:
        print("INCORRECT")
        print("the correct answer is :",answers[number])
    number+=1
print("***********************************************")
print("wow! your score is ",score)