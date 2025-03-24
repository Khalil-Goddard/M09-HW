import pandas as pd

class BookLover():
    
    
    
    # num_books = 0
  #  book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    
    # constructor
    def __init__(self, name, email, fav_genre, num_books):
        self.name = name # string type
        self.email =email # string type
        self.fav_genre = fav_genre # string type
        self.num_books = num_books # int type
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    # add a book 
    def add_book(self, book_name, book_rating): 
        if book_name in self.book_list['book_name'].values:
            return "This Book is already in the book list"
        elif book_rating >= 0 and book_rating <= 5:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            return "Book rating needs to be an integer 0-5"
        
        
    #determine if a person has read a book already   
    def has_read(self, book_name):
        """
        This function takes book_name (string) as input and determines if the person has read the book.
        That is, if that book name is in book_list.
        The method will return True if the person has read the book, False otherwise.
        """
        return book_name in self.book_list['book_name'].values
            
            
            
            
    def num_books_read(self):
        """
        This function takes no parameters and just returns the total number of books the person has read.
        """
        return self.num_books
        
        

        

    def fav_books(self):
        """
        This function takes no parameters and returns the filtered dataframe of the person’s most favorite books.
        Books in this list should have a rating > 3.
        """
        
        return self.book_list[self.book_list['book_rating' ] > 3]
        