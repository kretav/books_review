def average_rating(books):
    if not books:
        return 0

    total = sum(book["rating"] for book in books)
    return total / len(books)


def author_statistics(books):
    stats = {}

    for book in books:
        author = book["author"]

        if author not in stats:
            stats[author] = 0

        stats[author] += 1

    return stats