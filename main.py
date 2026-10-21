books = [
    {"id": "101", "title": "The Great Gatsby"},
    {"id": "102", "title": "1984"}
]

search = input("Enter book ID or Title: ").lower()

for book in books:
    if search == book["id"] or search in book["title"].lower():
        print("Found:", book)