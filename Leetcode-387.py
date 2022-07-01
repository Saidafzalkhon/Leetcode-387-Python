s = input()
son = -1
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j] and i!=j:
            son = -2
            break
        else:
            son = i
    if son!= (-2):
        break
        
print(son if son>-1 else -1)