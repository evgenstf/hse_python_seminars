def is_letter(index, text):
    char = text[index]
    return ('a' <= char and char <= 'z') or ('A' <= char and char <= 'Z')

def is_defice(index, text):
    if text[index] != '-':
        return False
    elif index == 0 or index + 1 == len(text):
        return False
    else:
        return is_letter(index - 1, text) and is_letter(index + 1, text);

def is_in_word(index, text):
    return is_letter(index, text) or is_defice(index, text)


def extract_words(text):
    words = []
    index = 0
    while index < len(text):
        word = ''
        while index < len(text) and is_in_word(index, text):
            word += text[index]
            index += 1
        while index < len(text) and not is_in_word(index, text):
            index += 1

        if word:
            words.append(word)

    return words

text = input()
words = extract_words(text)

print(len(words))

print("words:", words)
