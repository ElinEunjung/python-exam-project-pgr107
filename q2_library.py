class Book: 
    """Entity for individual book in the library"""
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f'\n<Title: {self.title} | Author: {self.author} | Num of pages: {self.num_pages}>\n'
    


class Library:
    """Entity responsible for managing books"""
    def __init__(self):
        self.books = []  # creates a new empty book lists in the library
    
    def add_book(self, book):                     
        self.books.append(book)
        print(f"New book {book}added successfully.\n ")
    
    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"The Book <{title}> removed from the library.\n")
                return
        
        print(f"No book found title {title} in the library.\n")
    
    def check_in(self, title):
        """Function allows library visitors to return a book"""
        pass
        
        """TODO: Implement this later    
        # verify if the book exist 
        # checks if the book is unavalible (borrowed)
        # update the book status to available and clear the borrower information
        # provide messages user-friendly message for successful check-in, unavalibale books, non-existent books"""
        
    
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
    


myLibrary = Library()  # create a Library instance

b1 = Book("The Art of War", "Sun Tzu", 150)
b2 = Book("Tao Te Ching", "Lao zi", 100)
b3 = Book("The Art of War", "Sun Tzu", 150)
b4 = Book("Dream of the Red Chamber", "Cao Xueqin", 550)

# add multiple books to the library
myLibrary.add_book(b1)
myLibrary.add_book(b2)
myLibrary.add_book(b3)
myLibrary.add_book(b4)


# attempt to check out a book
# attempt to return a book

# remove a book from the library
myLibrary.remove_book(b5.title)


# print the list of books to verify the results

        

