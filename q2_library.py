class Book: 
    """Entity for individual book in the library"""
    def __init__(self, title, author, num_pages, is_borrowed=False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_borrowed = is_borrowed
        
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Avaliable"
        return f'\n<Title: {self.title} | Author: {self.author} | Pages: {self.num_pages} | Status: {status}>\n'
    


class Library:
    """Entity responsible for managing books"""
    def __init__(self):
        self.books = []  # creates a new empty book lists in the library
    
    def add_book(self, book):                     
        self.books.append(book)
        # print(f"New book {book}added successfully.\n ")
    
    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"The Book <{title}> removed from the library.\n")
                return
        
        print(f"No book found title {title} in the library.\n")
    
    def get_book_by_title(self, title):
        """Function to get only book title"""
        for b in self.books:
            if b.title == title:
                return b       
        return None
        
    def is_registered(self, title):
        """Function to verify if the book is registered."""
        # checks if the book exists by seeing if get_book_by_title returns a value
        return self.get_book_by_title(title) is not None 
       
        
    def check_in(self, title):
        """Function allows library visitors to return a book"""     
        book = self.get_book_by_title(title)
        if not book:           
            print(f"The book <{title}> does not belongs to the libary.\n" )
            return
        
        # checks if the book is unavalible (borrowed)        
        if book.is_borrowed == True:
            book.is_borrowed = False # update the books status to avaliable
            # provide message for for check-in    
            print(f"The book <{title}> has returned successfully.\n" )            
            return
        else: 
            print(f"The book <{title}> was not borrowed.\n" )
            return

    
    def check_out(self, title):
        """Function allows library visitors to borrow a book"""
        pass
    
        """TODO: Implement this later
        # checks if the books is avalialbe
        # marks it as checked out if possible"""
    
    def __str__(self):
        if not self.books:  # if len(books) == 0:
            return "No books in the library."
        
        
        all_book_list = []       
        for b in self.books:       
            all_book_list.append(str(b))
            res = '\n'.join(all_book_list) # concatenate 
            
        return '[List of books in the library]\n' + f'{res}\n'
    

if __name__ == "__main__":
    """Only runs if this script is the main file (Ok to delete (__name__ == "__main__") for our exam but I included it to show some professionalism)"""
    
    # create a Library instance
    myLibrary = Library()  
    
    # add multiple books to the library
    b1 = Book("The Art of War", "Sun Tzu", 150)
    b2 = Book("Tao Te Ching", "Lao zi", 100)
    b3 = Book("The Art of War", "Sun Tzu", 150)
    b4 = Book("Dream of the Red Chamber", "Cao Xueqin", 550)   
    myLibrary.add_book(b1)
    myLibrary.add_book(b2)
    myLibrary.add_book(b3)
    myLibrary.add_book(b4)
    
    
    # attempt to check out a book
    myLibrary.check_in("Vegitarian")
    # attempt to return a book
    
    # remove a book from the library
    #myLibrary.remove_book(b1.title)
    
    
    # print the list of books to verify the results

        

