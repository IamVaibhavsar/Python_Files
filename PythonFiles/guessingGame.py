secretWord="vaibhav";
guess="";
guessCount=0;
guessLimit=3;
outOfGuess=False;

while guess!=secretWord and not(outOfGuess):
    if guessCount<guessLimit:
        guess=input("Enter your Guess:")
        guessCount+=1
    else:
        outOfGuess=True

if outOfGuess:
    print("you are out of chances. YOU LOSE!")
else:
    print("your Guess is correct. YOU WIN!")

