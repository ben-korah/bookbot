def count_words(text):
    word_array = text.split()
    return len(word_array)

def count_chars(text):
    char_count = {}
    uncased = text.lower()
    #word_array = word_array.split()
    for char in uncased:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    #return word_array
def sort_on(dict):
    return dict["num"]

def  sort_chars(text):
    chars = count_chars(text)
    character = []
    i = -1
    for char in chars:
        i += 1
        character.append({'char': char, 'num': chars[char]})
    character.sort(reverse=True, key=sort_on)
    return character

def test():
    print(f'{sort_chars('This is a tEst')}')

#test()

