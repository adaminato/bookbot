def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    letter_list = []
    i = 0

    print (f"--- Begin report fo {path_to_file} ---")
    print (f"{word_count(file_contents)} words found in the document")
    print ("\n")
    letters = letter_count(file_contents) 
    for key in letters:
        letter_list.append({"letter":key, "num":letters[key]})
    letter_list.sort(reverse=True, key=sort_on_occurence)
    for i in range(len(letter_list)):
        if letter_list[i]["letter"].isalpha():
            print (f"The '{letter_list[i]["letter"]}' character was found {letter_list[i]["num"]} times")

    
    

    

def word_count(text):
    return len(text.split())

def letter_count(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] = 1 + letters[letter]
        else:
            letters[letter] = 1
    return letters

def sort_on_occurence(dict):
    return dict["num"]

main()
