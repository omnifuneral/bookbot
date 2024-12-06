def word_count():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()                        
        word_list = file_contents.split()               #split string into list for counting
        return len(word_list)

def char_sort():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()          #make whole string lowercase     
        char_dict = {}                                  #initialize empty dictionary
        for char in lower_contents:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] +=1
                else:
                    char_dict[char] = 1
        char_list = [{'character': char, 'count': count} for char, count in char_dict.items()] #conversion from dict to list of dicts
        return char_list

def sort_by_freq(char):                                 #sorting function for list of dicts
    return char['count']






def main():
    count = word_count()
    char_list = char_sort()
    char_list.sort(key=sort_by_freq, reverse=True)      #sorts characters by most to least common

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{count} words found in the document\n")

    for char_data in char_list:
        print(f"The '{char_data['character']}' character was found {char_data['count']} times")

    print("--- End report ---")
   

    

main()