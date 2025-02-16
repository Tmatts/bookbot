def character_count(file_path: str)->dict:
    char_dict = {}

    with open(file_path) as file:
        file_content = file.read()
        file_content = file_content.lower()  # convert to lowercase for case-insensitive comparison§
        for char in file_content:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char, value in char_dict.items():
            if char.isalpha():
                print(f"The '{char}' character was found {value} times")
        return char_dict


if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    character_count(file_path)