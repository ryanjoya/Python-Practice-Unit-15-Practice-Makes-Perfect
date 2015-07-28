def remove_duplicates(lt):
    result = []
    for i in lt:
        if i not in result:
            result.append(i)
    return result
    
print remove_duplicates([1,2,1,1])
