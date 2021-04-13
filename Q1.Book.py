import sys
list_books = []

class Bookshelf:

    def __init__(self, list_books):
            self.available_media = list_books

    def read(self):
        print("Enter the name of the book you'd like to return>>")
        self.book = input()
        print(f'How many pages of "{self.book}" have you read ?')
        self.read_pages = input()
        for books in list_books:
            if self.book == books.title:
                books.get_status(self.read_pages)

class Book(Bookshelf):

    def __init__(self, title, author, publish_year, pages, language, price, read_pages, status, media_type):
        Bookshelf.__init__(self, list_books)
        self.media_type = media_type
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_pages = read_pages
        self.status = status

    def __str__(self):
        print("The books we have in our Bookshelf are as follows:")
        print("================================")
        for books in list_books:
            print(f'title: {books.title}')
            print(f'publish_year: {books.publish_year}')
            print(f'author(s): {books.author}')
            print(f'pages(number of pages): {books.pages}')
            print(f'language: {books.language}')
            print(f'price: {books.price}')
            print(f'status: {books.status}')
            print(f'read_pages: {books.read_pages}')
            print("\n")

    def get_status(self, read_pages):
        """calculate staus for each book that has read"""
        self.read_pages = read_pages
        if self.read_pages < self.pages:
            self.status = 'reading'
        elif self.read_pages >= self.pages:
            self.status = 'finished'
        return self.read_pages, self.status, self.read_pages

def add_media():

    print("Please fill in the information below for add to bookshelf")
    print('Media type :', end="")
    media_type = input()
    print('title :', end="")
    title = input()
    print('publish_year :', end="")
    publish_year = input()
    print('price($) :', end="")
    price = input()
    print('language :', end="")
    language = input()
    print('pages(number of pages) :', end="")
    pages = input()
    print('author(s) :', end="")
    author = input()
    read_pages = '0'
    status = 'unread'
    books = Book(title, author, publish_year, pages, language, price ,read_pages, status, media_type)
    list_books.append(books)

def main():

    books = Bookshelf(list_books)
    done = False
    while done == False:
        print(""" ======Welcome=======
          what do you want?
          1. Add book
          2. return read page
          3. show information of books
          4. Exit
          """)
        choice = int(input("Please Enter Choice number:"))
        if choice == 1:
            add_media()
        elif choice == 2:
            books.read()
        elif choice == 3:
            for book in list_books:
                Book.__str__(book)
        elif choice == 4:
            sys.exit()

main()