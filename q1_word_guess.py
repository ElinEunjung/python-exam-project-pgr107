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
    
def print_random_line(file):
    print(select_random_line(file))

def main():
    """The main function that runs the application"""
    
    #Opening a file 
    file = open("word_guess.txt", "r")
    
    print_random_line(file)
    
    file.close()

main()    