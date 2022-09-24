class Book:
    def __init__(self,numberofpages,title,editor,year):
        self.editor=editor
        self.pagenumber=numberofpages
        self.prodyear=year
        self.booktitle=title
# To create object
book=Book(input("Number of pages: \n"), input("Title \n"),input("Editor \n"), input("Year: \n"))
print(book.booktitle)
print(book.prodyear)
print(book.pagenumber)
print(book.editor)