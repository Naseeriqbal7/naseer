import pickle

with open("books.bin", "rb") as file:
    books = pickle.load(file)
    for book in books:
        print(books)
        