#     Magic methods

# Magic methods = Dunder methods (double underscore) __init__ , __str__ , __eq__
#                 They are automatically called by many of Python's built-in-operations
#                 They allow developers to define or customize the behaviour of objects


class Books:

    def __init__(self, title , author , pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f" {self.title} = {self.author}"

    def __eq__(self,other):     # it is usedd to check if the conditions are same                ,,,,,,,,,,,for example  -> itself = the first book and other means another book
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):    # less than
        return self.pages < other.pages    # it is used to compare or measure   (< ,, > )like  1) pages ,, 2) no.of books sold,,,,  3)height  etc.

    def __gt__(self,other):    # greater than comaparision
        return self.pages > other.pages

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author    # it will check if the word is something in the tile or author if it contains it will return truw or false

    def __getitem__(self,key):    # to access the elements bhy indexing
        if key == "title":
            return self.title
    def __getitem__(self,name):
        if name == "author":
            return self.author
        else:
            return f" {name} was not found"


book1 = Books("Ben 10","Man in Action",270)
book2 = Books("Tom and Jerry","ash",221)
book3 = Books("Doreamon","nobita",180)
book4 = Books("Ben 10","Man in Action",270)

print(book1)

print(book1 == book2) # it will check it the two conditions are same as like the two two have same title etc

print(book1 == book4)

print(book1 < book2)    # it is lt which is used to compare the pages of first book to another book

print(book1 > book2)

print("Tom and Jerry" in book2)  # if the tom and herry contains in book2 it will return True or else False

print(book1["title"]) # accessing through indexing if title is there it will give the correct book based on the input or you can change the title to any other name

print(book1["pages"]) # it will give none because we have not set the method in __getitem__ for indexing

print(book3["author"]) # it will give the author name throufh indexing (__getitem__)

print(book3["name of character"]) # it will give the else ouput which is written because of "if" condition