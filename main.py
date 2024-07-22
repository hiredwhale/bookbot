def main():
    book_location = "./books/frankenstein.txt"
    text = get_book_text(book_location)

    print(f"--- Begin report of {book_location} ---")
    print(f"{get_word_count(text)} words found in the document")
    print()

    letter_count = get_letter_count(text)
    letter_count.sort(reverse=True, key=lambda x: x["count"])
    for letter_data in letter_count:
        print(f"The {letter_data["letter"]} character was found {letter_data["count"]} times")

    print("--- End report ---")

def get_book_text(location):
    with open(location) as f:
        return f.read()

def get_word_count(content):
    words = content.split()
    return len(words)

def get_letter_count(content):
    letters = []
    alpha = [
        "a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x",
        "y", "z"]
    lowered = content.lower()
    for char in alpha:
        letter = {}
        letter["letter"] = char
        letter["count"] = lowered.count(char)
        letters.append(letter)
    return letters

main()