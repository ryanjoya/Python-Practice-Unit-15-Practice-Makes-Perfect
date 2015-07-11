def count(sequence, item):
    num = 0
    for i in sequence:
        if i == item:
            num += 1
    return num
