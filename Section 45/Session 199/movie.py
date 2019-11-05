class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

if __name__ == "__main__":
    m = Movie("harry potter")
    print(m)