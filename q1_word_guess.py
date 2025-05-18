#Importering
import random



def select_random_line(file):
    """Function that selects a random line from the .txt file as the word for the user to guess"""
    line = next(file)
    for num, a_line in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = a_line
    return line
    
def display_question(file):
    """Fuction that displayes the blanks and the letters as you guess them"""
    # A temporary value to get the correct answer
    temp_value = select_random_line(file)
    
    # A 'Permenant' variable to hold the answer without calling the select_random_line function
    # Also removes case sensetivity and leading/trailing white spaces
    correct_answer = temp_value.strip()
    # A intiger that representes the number of letters 
    n_letters = len(correct_answer) 
    
    # A intiger variable denoting the number of guesses that the user has left
    n_guesses = 4
    
    # The blank lines used as a plaseholder for the letters of the chosen word
    letter_display = correct_answer.replace(correct_answer, "_" * len(correct_answer))
    
    # loop to update the diplay as you guess letters 
    for i in range(n_guesses +1):
        print(f"The word has {n_letters} letters you have {n_guesses} guesses left")
        print(letter_display)
        n_guesses-=1
        

def user_input(correct_answer, letter_display, n_guesses):
    pass

def main():
    """The main function that runs the application"""
    
    #Opening a file 
    file = open("word_guess.txt", "r")
    
    display_question(file)
    
    file.close()

main()    