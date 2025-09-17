class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
        
    def bookinfo(self):
        print(f"The no of books in the library are {self.no_of_books}, the books are:")
        for book in self.books:
            print(book)

l=Library()
l.addbook("Harry potter1")
l.addbook("Harry potter2")
l.addbook("Harry potter3")
l.bookinfo()