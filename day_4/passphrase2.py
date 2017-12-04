def anagram(word, other_word):
    if sorted(list(word)) == sorted(list(other_word)):
        return True
    return False


with open('input', 'r') as f:
    text = f.readlines()

text = [t.strip() for t in text]

count = 0

for t in text:
    words = t.split()
    invalid = False
    for word in words:
        other_words = words[:]
        other_words.remove(word)
        for other_word in other_words:
            if anagram(word, other_word):
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        count += 1


print(count)
