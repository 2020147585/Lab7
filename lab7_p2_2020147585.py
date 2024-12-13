def count_character(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        count = {}

        for char in text:
            if char.isalpha():
                char = char.upper()
                count[char] = count.get(char, 0) + 1

        char_items = list(count.items())
        char_items.sort(key=lambda item: item[1], reverse=True)

        sorted_char = [char for char, count in char_items]

        print(sorted_char)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

if __name__ == "__main__":
    count_character("input_7_2.txt")
