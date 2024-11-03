
def word_count(line):
    return len(line.split(" "))

def character_count(line):
    char_list = []
    lower_line = line.lower()
    flag = True

    for item in lower_line:
        if item.isalnum():
            for dict in char_list:
                if dict.get("letter") == item:
                    dict["num"] += 1
                    break
                    
            else:
                char_count = {}
                char_count["letter"] = item
                char_count["num"] = 1
                char_list.append(char_count)
    
    return char_list

def sort_on(dict):
    return dict["num"]

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    print(f"{word_count(file_contents)} words found in the book.")

    char_counts_list = character_count(file_contents)
    char_counts_list.sort(reverse=True, key=sort_on)
    for dict in char_counts_list:
        print(f"The '{dict["letter"]}' character was found {dict["num"]} times")

    print("--- end report ---")

main()