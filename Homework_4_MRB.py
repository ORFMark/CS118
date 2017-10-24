##This is the homework for week 4, as created by Mark Burrell, and Everything Runs
import random ##imports the liabrary that allows use of random functions
print("HW4_MRB_09_26_17")
Correct_Answers = 0
Incorrect_Answers = 0
questions = 0
def questionGen(Question, CorrectA, IncA1, IncA2, IncA3): ##A function for the creation of multiple choice questions with 4 possible option
    global Correct_Answers ##calls the program-wide variable
    global Incorrect_Answers
    global questions
    questions +=1
    ##begin answer list creation and randomization
    answerList=[]
    answerList.append(CorrectA)
    answerList.append(IncA1)
    answerList.append(IncA2)
    answerList.append(IncA3)
    random.shuffle(answerList)
    ##end answer list
    print(Question)
    print("A",answerList[0],"\n")
    print("B",answerList[1],"\n")
    print("C",answerList[2],"\n")
    print("D",answerList[3],"\n")
    ##Sets up the answer check lists
    if CorrectA == answerList[0]:
        cAns=['A','a']
        iAns=['B','b','c','C','d','D']
    elif CorrectA == answerList[1]:
        cAns=['B','b']
        iAns=['A','a','c','C','d','D']
    elif CorrectA == answerList[2]:
        cAns=['C','c']
        iAns=['B','b','a','A','d','D']
    elif CorrectA == answerList[3]:
        cAns=['D','d']
        iAns=['B','b','c','C','a','A']
    ##end creation of answer check lists
        ##asks the user for input and checks it against the lists, responds appropriatly
    while True:
        userAns=str(input("What is the Answer? "))
        if userAns in cAns:
            print("You have chosen wisely")
            Correct_Answers+=1
            break
        elif userAns in iAns:
            print("You have chosen poorly")
            Incorrect_Answers+=1
            break
        else:
            print("Not a valid Answer")
    cAns.clear()
    iAns.clear()
        ##end answer check
        ##actual quiz questions
questionGen("What is 3*4", 12,7,34,90)
questionGen("What is 9*8", 9*8,98,89,312)
questionGen("What is the remainder of 9/4?",9%4,5,-5,94)
questionGen("What is 3*5?", 3*5,35,53,5.3)
questionGen("What is half of 12?",6,4,2,8)
questionGen("What is the third word of this scentence?", 'the', 'is', 'third', 'this')
##end quiz gen
print("Your score is", Correct_Answers/questions, "or", Correct_Answers, "Out of ", questions) ##Prints the score
