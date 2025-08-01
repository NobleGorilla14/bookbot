def get_word_count(words):
    num_of_words = 0
    word_list = words.split()
    for w in range(0,len(word_list)):
        num_of_words += 1
    return num_of_words


def get_char_count(words):
    chars = {}
    word_list = words.split()
    for w in word_list:
        word = w.split()
        for w in word:
            w = w.lower()
            for c in w:
                if c not in chars:
                    chars[c] = 1
                else:
                    chars[c] += 1
    return chars


def sort_on(items):
    return items["num"]


def sort_char(char_dict):
    characters = []
    for char in char_dict:
      if char.isalpha(): 
         dict = {"char":char,"num":char_dict[char]}
         characters.append(dict)
      else:
         continue
    characters.sort(reverse=True, key=sort_on)
    return characters
