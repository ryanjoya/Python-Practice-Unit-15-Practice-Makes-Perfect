def median(lst):
    lst.sort()
    if len(lst)==1:
        return lst[0]
    elif len(lst)%2 != 0:
        return lst[(len(lst)+1)/2-1]
    else:
        return (lst[len(lst)/2-1]+lst[len(lst)/2])/2.0
