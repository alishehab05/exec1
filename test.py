# import math
# import string
# # # # # # #easy
# # # # # # #1
# # # # # # name = ""
# # # # # # age= ""
# # # # # # name=input("Enter your name: ")
# # # # # # age=input("Enter your age: ")
# # # # # # print("Hello " + name + ", you are " + age + " years old.")
# # # # # # #2

# # # # # num = int(input("Enter a number: "))  # Convert input to integer
# # # # # if num % 2 == 0:
# # # # #     print("The number is even.")
# # # # # else:
# # # # #     print("The number is odd.")

# # # # # # #3

# # # # a=input("enter a list")
# # # # # a = a.split(",")  # Split the input string into a list
# # # # def return_first_and_last(a):
# # # #     if len(a) == 0:
# # # #         return None, None
# # # #     first = a[0]
# # # #     last = a[-1]
# # # #     return first, last
# # # # print(return_first_and_last(a))

# # # # # # #4
# # # num=0
# # # a=input("Enter a list of numbers ")
# # # a = list(map(int, a.split()))
# # # num=int(input("Enter a number to search for: "))
# # # def number_in_list(a, num):
# # #     if num in a:
# # #         return True
# # #     else:
# # #         return False
# # # print(number_in_list(a, num))
# # #
# # #medium
# # # # # # #1

# # # User inputs space-separated numbers like: 1 2 3 4 5
# # arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# # if len(arr) !=3:
# #     print("Please enter exactly three numbers.")
# # else:
# #     def sum_is_zero(arr):
# #         if sum(arr) == 0:
# #             return True 
# #         else:
# #             return False
# #     print(sum_is_zero(arr))        

# # # # # # #2
# text=input("Enter a string: ")
# def count_words(text):
#     text=text.lower()
#     words=text.split()
#     word_count={}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count    
# print(count_words(text))
# # # # # #3
class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        self.is_checked_out = True  # Fixed

    def return_book(self):
        self.is_checked_out = False  # Fixed

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - Checked out: {self.is_checked_out}"
class Library:
    def __init__(self):
        self.books = []  # Renamed from self.books to self.collection for clarity

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print("Book not found.")
        return None
b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)
