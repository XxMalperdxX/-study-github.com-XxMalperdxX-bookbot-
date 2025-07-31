

def get_num_words(text):
    words = text.split()
    return len(words)

def count_words(text):
    alphabet = {}
    new_list= text.split()
    new_list= text.split()
    for word in new_list:
        full_word = list(word)
        for letter in full_word:
            lower_case = letter.lower()
            if lower_case not in alphabet:
                alphabet[lower_case] = 1
            elif lower_case in alphabet:
                alphabet[lower_case] += 1
    return alphabet

def sort_dic(dictonary):
    sort = dict(sorted(dictonary.items(), key=lambda t: t[1], reverse=True))
    return sort