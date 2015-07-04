def digit_sum(n):
    total = 0
    n = str(n)
    for i in n:
        total = total + int(i)
    return total
