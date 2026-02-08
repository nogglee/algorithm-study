def solution(my_string, overwrite_string, s):
    x = my_string[:s] + overwrite_string
    
    return x + my_string[len(x):]