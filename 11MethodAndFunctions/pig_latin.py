def pig_latin(word):
    first_letter = word[0];

    if first_letter in 'aeiou':
        pig_word = word + 'ay';
    else:
        pig_word = word[1:] + first_letter + 'ey'

    return pig_word;

print(pig_latin('apple'));
