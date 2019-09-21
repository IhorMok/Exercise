import re

def abbreviate(words):
    words_list = re.split('[-_ ]', words)
    letters_list = []
    clean_words_list = [word for word in words_list if len(word) > 0]
    for word in clean_words_list:
    	letters_list.append(word[0])
    abbreviation = ''.join(letters_list)

    return abbreviation.upper()