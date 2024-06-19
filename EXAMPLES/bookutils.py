def strip_article(title): 
    """ create function which takes element to compare and returns comparison key
    """
    for article in 'A ', 'An ', 'The ':
        if title.startswith(article):
            title = title.removeprefix(article)  # remove article
            break
    return title

if __name__ == "__main__":
    print(strip_article("The Name of the Rose"))
    print(strip_article("1984"))
    print(strip_article("A Confederacy of Dunces"))
