def purify(number):
    return [ x for x in number if x % 2 == 0]

print (purify([1,2,3,4,5,6,7,8,9,10]))
