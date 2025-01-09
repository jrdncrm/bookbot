# first line of code for book.dev (bookbot:7)
# print("hello world")

# Opening a file on Lesson 8 first lines are boots' code
# def main():
   # with open("books/frankenstein.txt") as f:
    #    file_contents = f.read()
   # print(file_contents)

#if __name__ == "__main__":
 #   main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count(text)} words found in the document')

    print(count_characters(text))

    print(f'--- End report ---')


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(monster_book):
    return len(monster_book.split())

def count_characters (letters):
    dictionary = {}
    lowercase_book = letters.lower()
    for i in lowercase_book:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i]=1
    for line in dictionary:
        print(f'The {line} character was found {dictionary[line]} times')        
    return 


main()