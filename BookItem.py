class BookItem:
    reserved_book_items = []
    
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.info = {}
        
    def updateIssuerInfo(self, name, student_id, days):
        self.info["Name"] = name
        self.info["Student ID"] = student_id
        self.info["Days"] = days
        
    def addToReservedList(self):
        BookItem.addReservedBooks(self)
        
    def removeFromReservedList(self):
        BookItem.reserved_book_items.remove(self)

    @classmethod
    def addReservedBooks(cls, book):
        cls.reserved_book_items.append(book)