class Book: 
    """Class for individual book in the library"""
    def __init__(self, title, author, num_pages, is_borrowed=False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_borrowed = is_borrowed
              
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return (
            f'\n<Title: {self.title} | Author: {self.author}'
            f'| Pages: {self.num_pages} | Status: {status}>\n'
        )


class Library:
    """Class responsible for managing books"""
    def __init__(self):
        self.books = []    # Creates a new empty book lists in the library
    
    def add_book(self, book):                     
        self.books.append(book)
        print(f"New book {book}added successfully.\n ")
    
    def remove_book(self, title):
        book = self.get_book_by_title(title)
        if not book:
            print(f"No book found by title {title} in the library.\n")
            return
        else: 
            self.books.remove(book)
            print(f"The Book <{title}> removed from the library.\n")
            return
           
    def get_book_by_title(self, title):
        """Gets only book title"""
        for b in self.books:
            if b.title == title:
                return b       
        return None
    
    def get_valid_book(self, title):
        """Gets a book by title and prints an error if not found"""
        book = self.get_book_by_title(title)
        if not book:
            print(f"The book <{title}> does not belong to the library.\n" )
            return None
        return book
                    
    def check_in(self, title):
        """Allows library visitors to return a book"""     
        book = self.get_valid_book(title)
        if not book:
            return
        
        # Checks if the book is unavalible (borrowed)        
        if book.is_borrowed == True: # add "== True" for clarity
            book.is_borrowed = False # update status to avaliable
            # provide message for check-in    
            print(f"The book <{title}> has been checked in successfully.\n" )            
            return
        else: 
            print(f"The book <{title}> was not borrowed.\n" )
            return
   
    def check_out(self, title):
        """Allows library visitors to borrow a book"""
        book = self.get_valid_book(title)
        if not book:
            return
        
        # Checks if the books is avalialbe
        if book.is_borrowed == False:
            book.is_borrowed = True # update status to unavaliable
            # provide message for check-out   
            print(f"The book <{title}> has been checked out successfully.\n" )            
            return
        else: 
            print(f"The book <{title}> has already been checked out.\n" )
            
    def __str__(self):
        if not self.books:  # if len(books) == 0:
            return "No books in the library."
          
        """ Changed this code block followed by pythonic style guide
        all_book_list = []       
        for b in self.books:       
            all_book_list.append(str(b))
            res = '\n'.join(all_book_list) # concatenate 
        """   
        
        all_book_list = '\n'. join(str(b) for b in self.books)
        return '[List of books in the library]\n' + f'{all_book_list}\n'
    

if __name__ == "__main__":
    """Only runs if this script is the main file 
       It's ok to delete (__name__ == "__main__") for our exam 
       but I included it to show some professionalism
       """
    
    # Create a Library instance
    myLibrary = Library()  
    
    # Add multiple books to the library
    b1 = Book("The Art of War", "Sun Tzu", 150)
    b2 = Book("Tao Te Ching", "Lao zi", 100)
    b3 = Book("Dream of the Red Chamber", "Cao Xueqin", 550)  
    myLibrary.add_book(b1)
    myLibrary.add_book(b2)
    myLibrary.add_book(b3)
   
    # Attempt to check out a book
    myLibrary.check_out("Vegetarian")  # not registered book
    myLibrary.check_out("The Art of War")

    # Attempt to return a book
    myLibrary.check_in("The Art of War")

    # Remove a book from the library
    myLibrary.remove_book(b2.title)
       
    # Print the list of books to verify the results
    print(myLibrary)

        

