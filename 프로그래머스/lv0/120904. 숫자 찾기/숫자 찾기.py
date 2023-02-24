def solution(num, k):
    num = str(num)
    
    for i in num:
        if i == str(k):
            return num.index(i) + 1
        
    return -1
            