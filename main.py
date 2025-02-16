def character_count(file_path: str)->dict:
    char_count = 0
    char_dict = {}

    with open(file_path) as file:
        file_content = file.read()
        file_content = file_content.lower()  # convert to lowercase for case-insensitive comparison§
        for char in file_content:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for _ , value in char_dict.items():
            char_count += value
        return char_dict


if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    print(character_count(file_path))