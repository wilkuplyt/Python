dictionary = {
    "python": "A high-level programming language known for its readability and simplicity.",
    "variable": "A reserved memory location to store values.",
    "function": "A block of code that only runs when it is called.",
    "list": "A collection which is ordered and changeable.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A programming construct that repeats a group of statements.",
    "string": "A sequence of characters.",
    "integer": "A whole number, positive or negative, without decimals.",
    "boolean": "A data type that can hold one of two values: True or False.",
    "array": "A collection of items stored at contiguous memory locations."
}

def add_word(word, definition):
    dictionary[word] = definition

def search_word(word):
    return dictionary.get(word, "Definition not found.")

def print_dictionary():
    print("\n=== Dictionary ===")
    for word, definition in dictionary.items():
        print(f"{word.capitalize()}: {definition}")
    print("===================")

def main():
    while True:
        print("\n=== Dictionary Menu ===")
        print("1. View all words")
        print("2. Search for a word")
        print("3. Add a new word")
        print("4. Exit")
        action = input("Choose an option (1-4): ")

        if action == '1':
            print_dictionary()

        elif action == '2':
            word = input("Enter the word to search: ").lower()
            definition = search_word(word)
            print(f"{word.capitalize()}: {definition}")

        elif action == '3':
            word = input("Enter the new word: ").lower()
            definition = input("Enter the definition: ")
            add_word(word, definition)
            print(f"Added '{word}' to the dictionary.")

        elif action == '4':
            print("Exiting the dictionary. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
