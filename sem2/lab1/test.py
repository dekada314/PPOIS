s = '0100111'
answer: list[int] = []

i = 0
while i < len(s):
    curr_num = s[i]
    j = i
    while j < len(s) and s[j] == curr_num:
        j += 1
    answer.append(j - i)
    i += j - i
    
print(answer)