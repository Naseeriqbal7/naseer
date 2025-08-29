filename = input("Enter the file name:")
books = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            books.append(line)
            print(books)
except FileNotFoundError:
    print("could not find the file named: " + filename)
except OSError: 
    print("could not open the file named: " + filename)
except Exception:
    print("An unexpected error occurred.")
   