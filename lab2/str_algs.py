def str_reverse(str):
    s = ''
    for i in range(len(str)-1, -1, -1):
        s += str[i]
    return s
str1 = "sdkcsd2kcsn odkeodk edkeodk"
str2 = "123 456 789"
str3 = "ss          88? !$     ol"
print(str_reverse(str1))
print(str_reverse(str2))
print(str_reverse(str3))