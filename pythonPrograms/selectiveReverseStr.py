#str1 = "abc$$def1wer%a@"
#str1 = "!abc$$def1wer%a@"
#str1 = "!abc$$def1wer%a@a"
#str1 = "!abc$$def1wer%a@a##"
str1 = ''

def rev(str):
    return str[::-1]

def selectiveRev(str1):
    lastIdx = 0
    newStr = ''
    if str1:
            for curIdx  in range(len(str1)):
                if(str1[curIdx].isalpha()):
                   continue
                else:
                    newStr = newStr + rev(str1[lastIdx:curIdx]) + str1[curIdx]
                    lastIdx = curIdx+1
            else:
                if(str1[curIdx].isalpha()):
                    newStr = newStr + rev(str1[lastIdx:curIdx]) + str1[curIdx]
    return newStr

print("Input string = ",str1)
print("Output string = ", selectiveRev(str1))
