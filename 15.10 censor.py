def censor(text, word):
    text = text.split()
    
    result = []
    
    for string in text:
        if string == word:
            result.append('*' * len(string))
        else:
            result.append(string)
            
    return ' '.join(result)

print censor("this hack is wack hack", "hack")
