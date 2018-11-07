str1 = 'ddada$dadadadartdadada'

str2 = 'dad'


print("output using count function = ",str1.count(str2))

def subStrCount(str1,subString):
    idx = str1.find(subString)
    if(idx == -1):
        return 0
    else:
        return(1 + subStrCount(str1[idx+1:],subString))

print("output using custom substring count function = ", subStrCount(str1,str2))
