import sys
list_media = []
list_books = []
list_magazine = []
list_podcast = []
list_audiobook = []

class Bookshelf:

        def __init__(self,list_media):
            self.available_media = list_media

        def read(self):
            """this method is for get reading pages according to title"""
            print("Enter the name of the Book/Magazine you'd like to return>>")
            self.media = input()
            print(f'How many pages of "{self.media}" have you read ?')
            self.read_pages = input()
            for media in list_media:
                if self.media == media.title:
                    media.get_status_read(self.read_pages,media.pages)

        def time(self):
            """this method is for get listening  time according to title"""
            print("Enter the name of the Podcast/Audio you'd like to return>>")
            self.media = input()
            print(f'How much time(min) of "{self.media}" have you listen ?')
            self.listen_time = input()
            for media in list_media:
                if self.media == media.title:
                    media.get_status_time(self.listen_time,media.times)

        def get_status_read(self, read_pages, pages):
            """this method change status according to reading pages"""
            self.read_pages = read_pages
            self.pages = pages
            if self.read_pages < self.pages:
                self.status = 'reading'
            elif self.read_pages >= self.pages:
                self.status = 'finished'
            return self.read_pages, self.status

        def get_status_time(self,listen_time,times):
            """this method change status according to listening time"""
            self.listen_time = listen_time
            self.times = times
            if self.listen_time < self.times:
                self.status = 'listening'
            elif self.listen_time >= self.times:
                self.status = 'finished'
            return self.listen_time, self.status

        def progress_percent(self):
            """this method caculate percentage of progress according to status and reading/listening page/time"""
            if self.status == 'reading':
                p = float(self.pages)
                r = float(self.read_pages)
                self.progress = round(r*100/p)
            elif self.status == 'listening':
                t = float(self.times)
                listen = float(self.listen_time)
                self.progress = round(listen*100/t)
            elif self.status=='finished':
                self.progress = 100

            return self.progress

        def sorted_list(self):
            """this method sort(decs) media list accorting return method progress_percent """
            sort_list = sorted(list_media, key=lambda x: x.progress_percent(), reverse=True)
            print("The process of media that have you Read/Listen :")
            print("================================")
            for sort in sort_list:
                print(f'media_type: {sort.media_type}')
                print(f'title: {sort.title}')
                print(f'progress: {sort.progress} %')
                print("\n")

        def __str__(self):
            """print some of media information in bookshelf """
            print("The media we have in our Bookshelf are as follows:")
            print("================================")
            for media in list_media:
                print(f'media_type: {media.media_type}')
                print(f'title: {media.title}')
                print(f'publish_year: {media.publish_year}')
                print(f'price($): {media.price}')
                print(f'status: {media.status}')
                print("\n")

class Book(Bookshelf):

    def __init__(self,title, author, publish_year, pages, language, price,
                 read_pages,status,progress,media_type):
        Bookshelf.__init__(self, list_media)
        self.media_type = media_type
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_pages = read_pages
        self.status = status
        self.progress = progress

    def __str__(self):
        print("Books we have in our Bookshelf are as follows:")
        print("================================")
        for books in list_books:
            print(f'media_type: {books.media_type}')
            print(f'title: {books.title}')
            print(f'publish_year: {books.publish_year}')
            print(f'author(s): {books.author}')
            print(f'pages(number of pages): {books.pages}')
            print(f'language: {books.language}')
            print(f'price: {books.price}')
            print(f'status: {books.status}')
            print(f'read_pages: {books.read_pages}')
            print("\n")

class Magazine(Bookshelf):

    def __init__(self, title, author, publish_year, language, price, pages, issue,read_pages,status,progress,media_type):
        Bookshelf.__init__(self, list_media)
        self.media_type = media_type
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.pages = pages
        self.issue = issue
        self.read_pages = read_pages
        self.status = status
        self.progress = progress

    def __str__(self):
        print("Magazines we have in our Bookshelf are as follows:")
        print("================================")
        for magazines in list_magazine:
            print(f'media_type: {magazines.media_type}')
            print(f'title: {magazines.title}')
            print(f'publish_year: {magazines.publish_year}')
            print(f'author(s): {magazines.author}')
            print(f'pages(number of pages): {magazines.pages}')
            print(f'language: {magazines.language}')
            print(f'price: {magazines.price}')
            print(f'issue: {magazines.issue}')
            print(f'status: {magazines.status}')
            print(f'read_pages: {magazines.read_pages}')
            print("\n")

class Podcastepisode(Bookshelf):

    def __init__(self,title,publish_year,language, price,times,speaker,listen_time,status,progress,media_type):
        Bookshelf.__init__(self, list_media)
        self.media_type = media_type
        self.title = title
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.times = times
        self.speaker = speaker
        self.listen_time = listen_time
        self.status = status
        self.progress = progress

    def __str__(self):
        print("Podcast episodes we have in our Bookshelf are as follows:")
        print("================================")
        for podcasts in list_podcast:
            print(f'media_type: {podcasts.media_type}')
            print(f'title: {podcasts.title}')
            print(f'publish_year: {podcasts.publish_year}')
            print(f'speaker(s): {podcasts.speaker}')
            print(f'time(time of podcast): {podcasts.times}')
            print(f'language: {podcasts.language}')
            print(f'price: {podcasts.price}')
            print(f'status: {podcasts.status}')
            print(f'listen_time: {podcasts.listen_time}')
            print("\n")

class Audiobook(Bookshelf):

    def __init__(self,title,publish_year, price,times,speaker,author,book_language,audio_language,listen_time,status,progress,media_type):
        Bookshelf.__init__(self, list_media)
        self.media_type = media_type
        self.title = title
        self.publish_year = publish_year
        self.price = price
        self.times = times
        self.speaker = speaker
        self.author = author
        self.book_language = book_language
        self.audio_language = audio_language
        self.listen_time = listen_time
        self.status = status
        self.progress = progress

    def __str__(self):
        print("Audiobooks we have in our Bookshelf are as follows:")
        print("================================")
        for audiobooks in list_audiobook:
            print(f'media_type: {audiobooks.media_type}')
            print(f'title: {audiobooks.title}')
            print(f'publish_year: {audiobooks.publish_year}')
            print(f'author(s): {audiobooks.author}')
            print(f'speaker(s): {audiobooks.speaker}')
            print(f'time(time of podcast): {audiobooks.times}')
            print(f'book_language: {audiobooks.book_language}')
            print(f'audio_language: {audiobooks.audio_language}')
            print(f'price: {audiobooks.price}')
            print(f'status: {audiobooks.status}')
            print(f'listen_time: {audiobooks.listen_time}')
            print("\n")

def add_media():

    """"this function get information about each media"""
    print("Please fill in the information below for add to bookshelf")
    read_pages = '0'
    status = 'unread'
    listen_time = '0'
    progress = 0
    print('Media type :', end="")
    media_type = input()
    print('title :', end="")
    title = input()
    print('publish_year :', end="")
    publish_year = input()
    print('price($) :', end="")
    price = input()
    if media_type == 'book':
        print('language :', end="")
        language = input()
        print('pages :', end="")
        pages = input()
        print('author(s) :', end="")
        author = input()
        media = Book(title, author, publish_year, pages, language, price,read_pages,status,progress,media_type)
        list_books.append(media)
    elif media_type == 'magazine':
        print('language :', end="")
        language = input()
        print('pages :', end="")
        pages = input()
        print('author(s) :', end="")
        author = input()
        print('issue :', end="")
        issue = input()
        media = Magazine(title, author, publish_year, language, price, pages, issue,read_pages,status,progress,media_type)
        list_magazine.append(media)
    elif media_type == 'podcast':
        print('language :', end="")
        language = input()
        print('time(min) :', end="")
        times = input()
        print('speaker(s) :', end="")
        speaker = input()
        media = Podcastepisode(title,publish_year,language, price,times,speaker,listen_time,status,progress,media_type)
        list_podcast.append(media)
    elif media_type == 'audiobook':
        print('time(min) :', end="")
        times = input()
        print('speaker(s) :', end="")
        speaker = input()
        print('author(s) :', end="")
        author = input()
        print('book_language :', end="")
        book_language = input()
        print('audio_language :', end="")
        audio_language = input()
        media = Audiobook(title,publish_year, price,times,speaker,author,book_language,audio_language,listen_time,status,progress,media_type)
        list_audiobook.append(media)
    list_media.append(media)

def main():

    media = Bookshelf(list_media)
    done = False
    while done == False:
        print(""" ======Welcome=======
          what do you want?
          1. Add book/magazine/podcast/audiobook
          2. show information of bookshelf
          3. show information of books
          4. show information of magazine
          5. show information of podcast episode
          6. show information of audiobook
          7. return read Book/Magazine
          8. return listen Podcast/Audio
          9. calculate and sort list according to progress
          10. Quit
          """)
        choice = int(input("Please Enter Choice number:"))
        if choice == 1:
            add_media()
        elif choice == 2:
            for media in list_media:
                Bookshelf.__str__(media)
        elif choice == 3:
            for book in list_books:
                Book.__str__(book)
        elif choice == 4:
            for magazine in list_magazine:
                Magazine.__str__(magazine)
        elif choice == 5:
            for podcast in list_podcast:
                Podcastepisode.__str__(podcast)
        elif choice == 6:
            for audio in list_audiobook:
                Audiobook.__str__(audio)
        elif choice == 7:
            media.read()
        elif choice == 8:
            media.time()
        elif choice == 9:
            media.sorted_list()
        elif choice == 10:
            sys.exit()
main()


