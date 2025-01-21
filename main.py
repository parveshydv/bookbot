
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        wc = count_words(file_content)
        dc = character_count(file_content)
        print ("--- Begin report of books/frankenstein.txt ---")
        print(wc,"words found in the document")
        sorted_characters = sorted(dc.items(), key=lambda item: item[1], reverse=True)
        
        for char, count in sorted_characters:
            print(f"The '{char}' character was found {count} times")
        """
        for a in dc:
            
             print("The ",a,"was found ",dc[a], "times")
        """
        print("--- End report ---")

       

        

def count_words(file):
    words = file.split()
    return len(words)


def character_count(book):
    book_lowercase = book.lower()
    dict = {}
    for character in book_lowercase:
        if character.isalpha() == True:
            if character in dict:
                dict[character] += 1
            else:
                dict[character] = 1
    """
    char_list = []
    for char, count in dict.items():
        char_list.append({"name": char, "num": count})
    """

              
    return dict
     


     





main()
