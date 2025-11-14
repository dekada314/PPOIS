def counting_sort(non_sorted):
    if len(non_sorted) <= 1:
        return non_sorted
    
    Min, Max = min(non_sorted), max(non_sorted)
    diff = Max - Min + 1

    count = [0] * diff

    for num in non_sorted:
        count[num - Min] += 1

    for i in range(1,len(count)):
        count[i] += count[i - 1]
        
    result = [0] * len(non_sorted)

    for num in reversed(non_sorted):
        index = count[num - Min]
        result[index - 1] = num
        count[num - Min] -= 1
        
    return result
