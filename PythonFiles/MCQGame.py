from MCQGame2 import Question

MCQ=[
    "What color of apples? \na)red\nb)blue\nc)green\nd)yellow",
    "Half adder has how many inputs?\na)1\nb)2\nc)3\nd)4",
    "which operator can be overloaded?\na).\nb).*\nc)::\nd)+"
]

questions = [
    Question(MCQ[0],"a"),       #Objects of class Question
    Question(MCQ[1],"b"),
    Question(MCQ[2],"d"),
]

def run_test(questions):        #looping through objects
    score=0
    for question in questions:
        answer=input(question.prompt)       #invoke elements of array MCQ
        if answer==question.answer:
            score=score+1
    print("You got " + str(score) + " out of " + str(len(questions)) +" correct")

run_test(questions)