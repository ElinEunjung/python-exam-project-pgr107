#Importering
import random
import re


def select_random_line(file):
    """Function that selects a random line from the .txt file as the word for the user to guess"""
    line = next(file)
    
    for num, a_line in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = a_line
    return line.lower().strip()
    
    
def display_question(file):
    """Fuction that displayes the blanks and the letters as you guess them"""
    correct_answer = select_random_line(file)
    
    # A intiger that representes the number of letters 
    n_letters = len(correct_answer) 
    
    # A intiger variable denoting the number of guesses that the user has left
    n_guesses = n_letters
    
    # The blank lines used as a plaseholder for the letters of the chosen word
    letter_display =  "_" * len(correct_answer)
    
    # loop to update the diplay as you guess letters 
    while n_guesses>0:
        if(letter_display == correct_answer):
            victory(correct_answer)
            break
        print(f"The word has {n_letters} and you have {n_guesses} left.\n")
        print(f"Your word: {letter_display}")
        user_input = input("Letter: ")
        user_input = user_input[0].lower().strip()
        if(user_input in letter_display):
            print("You have alredy guessed this")
        elif(user_input in correct_answer):
            print("Corret")
            letter_display = update_display(correct_answer, user_input, letter_display)
            
        else:
            print("wrong")
        
        n_guesses -= 1
    
    if(n_guesses == 0 and letter_display  != correct_answer):
        print(f"\nYou lost. The correct word was: {correct_answer}")


def update_display(correct_answer, user_input, letter_display):
    """Function that updates the display when the user gueesses a letter correctly"""
    letter_display = list(letter_display)
    
    for i in range(len(correct_answer)):
        if(correct_answer[i] == user_input):
            letter_display[i] = user_input
        
    
    # got the idea of "".join() from here https://stackoverflow.com/questions/1228299/changing-a-character-in-a-string   
    return "".join(letter_display)
  
  
def victory(corret_answer):
    print(f"You won. the word is indeed {corret_answer}")  
    
    
def main():
    """The main function that runs the application"""
    
    try:
        #Opening a file 
        file = open("word_guess.txt", "r")
    
        display_question(file)
    
        file.close()
    except FileNotFoundError:
        print("Error: word_guess.txt not found")


main()    