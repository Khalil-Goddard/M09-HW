import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        book = "Harry Potter"
        self.assertTrue(book in Lover1.book_list['book_name'].values)
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        Lover1.add_book("Harry Potter", 4)
        expected = 1
        actual = Lover1.book_list['book_name'].value_counts().get("Harry Potter")
        self.assertEqual(expected, actual) 
                
    def test_3_has_read(self): 
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        self.assertTrue(Lover1.has_read("Harry Potter")) 
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        self.assertFalse(Lover1.has_read("The Stranger")) 
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        Lover1.add_book("The Stranger", 3)
        Lover1.add_book("To Kill A Mocking Bird", 2)
        expected = 3
        actual = Lover1.num_books
        self.assertEqual(expected, actual) 
        

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        Lover1 = BookLover("Khalil Goddard", "kg@gmail.com", "Mystery", 0)
        Lover1.add_book("Harry Potter", 4)
        Lover1.add_book("The Stranger", 3)
        Lover1.add_book("To Kill A Mocking Bird", 2)
        Lover1.add_book("The Scarlet Letter", 5)
        self.assertTrue((Lover1.fav_books().book_rating > 3).all())
        
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)