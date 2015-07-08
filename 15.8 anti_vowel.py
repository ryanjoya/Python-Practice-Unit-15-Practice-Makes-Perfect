def anti_vowel(text):
    return ''.join([c for c in text if c.upper() not in 'AEIOU'])
