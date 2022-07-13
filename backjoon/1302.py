# https://www.acmicpc.net/problem/1302

n = int(input())

books = dict()
for _ in range(n):
    name = input()
    if books.get(name, 0) == 0:
        books[name] = 1
    else:
        books[name] += 1

max_sold_count = 0
max_sold_book_name = ""
for book in books:
    if max_sold_count < books[book]:
        max_sold_count = max(max_sold_count, books[book])
        max_sold_book_name = book
    elif max_sold_count == books[book]:
        max_sold_book_name = sorted([max_sold_book_name, book])[0]

print(max_sold_book_name)
