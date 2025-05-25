#Importering
import random

def select_random_line(file):
    """Function that selects a random line from the .txt file for the user"""
    lines = file.readlines()
    total_lines = len(lines)
    random_line = random.randint(0, total_lines - 1)
    return lines[random_line]
    
    
def display_question(file):
    """Fuction that displays the blanks and the letters as you guess them"""
    correct_answer = select_random_line(file).strip().lower()
    
    # A array of letters not in the answer
    wrong_letters = []
    
    # An integer that represents the number of letters 
    n_letters = len(correct_answer) 
    
    # A intiger variable denoting the number of guesses that the user has left
    n_guesses = n_letters
    
    # The blank lines used as a plaseholder for the letters of the chosen word
    letter_display =  "_" * len(correct_answer)
    
    # Loop to update the display as you guess letters 
    while n_guesses > 0:
        print(f"You have {n_letters} letters and you have {n_guesses} guesses.\n")
        print(f"Your word: {letter_display}")
        
        user_char = input("Letter: ")
        user_char = user_char.lower().strip()
        
        is_valid_input = validate_user_char(user_char)
        
        if is_valid_input :
            # If block used to check if you have already guessed a letter  
            if user_char in letter_display or user_char in wrong_letters :
                print("You have already guessed this")
                continue
            # Elif used, logic will run if the if statement above is false 
            elif user_char in correct_answer:
                print("Correct")
                letter_display = update_display(correct_answer, user_char, letter_display)
                n_guesses += 1
            else:
                print("wrong")
                wrong_letters.append(user_char)

            if letter_display == correct_answer:
                print_victory_message(correct_answer)
                break
        
            n_guesses -= 1
            
        else:
            print("Invalid input")
        
    
    if n_guesses == 0 and letter_display != correct_answer:
        print(f"\nYou lost. The correct word was: {correct_answer}")

def validate_user_char(user_char):
    valid_input = True
    # If blocks used for input validation
    if len(user_char) > 1:
        valid_input = False
          
    if not user_char.isalpha():
        valid_input = False
        
    return valid_input

def update_display (correct_answer, 
                user_char, letter_display):
    """Updates the display after the user guesses a letter correctly"""
    letter_display = list(letter_display)
    
    for i in range(len(correct_answer)):
        if correct_answer[i] == user_char:
            letter_display[i] = user_char
        
    
    # Got the idea of "".join() from here:
    # https://stackoverflow.com/questions/1228299/changing-a-character-in-a-string   
    return "".join(letter_display)
  
  
def print_victory_message(corret_answer):
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