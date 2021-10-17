def count_vowels(word: str):
    total_vowels = 0
    word = word.lower()
    for letter in word:
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels
