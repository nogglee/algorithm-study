def solution(a, b):
    ab=str(a)+str(b)
    ba=str(b)+str(a)
    answer = ab if (ab >= ba) else ba
    
    return int(answer)