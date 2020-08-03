
from Book import Book

class Catalog:
    books_list = []
    different_book_count = 0
        
    def addBook(title, author, category, publication_date):
        b = Book(title, author, category, publication_date)
        Catalog.addBooksList(b)
        Catalog.different_book_count += 1
        print("Book {} has been added successfully!".format(title))
    
    def addBookItem(title, isbn, rack):
        for book in Catalog.books_list:
            if book.title == title:
                b = Book.addBookItem(book, isbn, rack)
                print("Book Item {} has been added successfully!".format(isbn))
        
    def removeBook(rem_book):
        for book in Catalog.books_list:
            if book.title == rem_book:
                Catalog.books_list.remove(book)
                Catalog.different_book_count -= 1
                print("Book {} has been removed from the catalog!".format(rem_book))
                
    def removeBookItem(rem_bookitem):
        for book in Catalog.books_list:
            for book_item in book.book_item:
                if book_item.isbn == rem_bookitem:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book Item {} has been removed from the catalog!".format(rem_bookitem))
        
    def searchByTitle(title):
        for book in Catalog.books_list:
            if book.title == title:
                print("Book available!")
                break
        else:
            print("Sorry.. no books are available by this title!")
    
    def searchByAuthor(author):
        count = 0
        for book in Catalog.books_list:
            if book.author == author:
                print(book.title)
                count += 1
        if count == 0:
            print("Sorry.. no books are available by this author!")
            
    def searchByCategory(category):
        count = 0
        for book in Catalog.books_list:
            if book.category == category:
                print(book.title)
                count += 1
        if count == 0:
            print("Sorry.. no books are available under this category")
            
    def searchByPublicationDate(publication_date):
        count = 0
        for book in Catalog.books_list:
            if book.publication_date == publication_date:
                print(book.title)
                count += 1
        if count == 0:
            print("Sorry.. no books are available published on this date!")
            
    def displayAllBooks():
        c = 0
        for book in Catalog.books_list:
            c += book.total_count
            book.printBook()
        print("Total book titles", Catalog.different_book_count)
        print("Total Books", c)
        
    def updateIssuerInfo(book_item, name, student_id, days):
        Book.updateIssuerInfo(book_item, name, student_id, days)
        
    def addToReservedList(book_item):   
        Book.addToReservedList(book_item)
        
    def removeFromReservedList(ret_book_item):
        Book.removeFromReservedList(ret_book_item)

    def viewReservedBookItems():
        Book.viewReservedBookItems()
        
    def viewIssuerInfo(isbn):
        Book.viewIssuerInfo(isbn)

    @classmethod
    def addBooksList(cls, book):
        cls.books_list.append(book)