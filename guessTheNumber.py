#random allows for random.randchoice(letters) and random.ranint(start, end). Time allows for dramatic pause.
import random, time


print('Hello, what is your name?')
#global variable throughout program, unless overriden
name = input () #input function is already string, so it can be cancantonised below.
if name == "poop" or "fart" or "butt": #I think i need regex for this to work properly
    print ("Gross.")
    time.sleep (2) #dramatic pause


print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
                     #cancantination of all strings

while True:
    secretnumber = (random.randint (1, 20))#random integer (lower limit, upper limit)

#how many chances do you want to give them? Range starts at 1 and goes upto but does not include 7
    for guessesTaken in range (1, 7):
                    print ("Take a guess.")
                    try: #try:/ except: if non-integer is entered
                    #variable declared within block, guess, is a local variable that gets deleted at the end of the block
                        guess = int(input ())#input() starts as a string, but is changed to and integer with int.
                    except ValueError: 
                        print ("That's not a number!")
                        continue #starts block at the top

                #next if has to be in line with try to move code forward, otherwise it is tried after ValueError
                    if guess < secretnumber:
                        print ('...higher')
                    elif guess > secretnumber:
                        print ('lower')         
                    else:
                        break

    if guess == secretnumber:
        print ("Great job, you guessed the secret number in " + str(guessesTaken) + " guesses!")

    else:
        print("Nope, the correct answer was " + str(secretnumber))

    print("Would you like to play again (y/n)?")
    again = input ()
    if again == "y" :
        print("Alright, " + name + ", I'll win this time.")
        continue
    else: # if anything other than y is entered, end the program
        print ("Bye, " + name)
        break
          



#DSS
