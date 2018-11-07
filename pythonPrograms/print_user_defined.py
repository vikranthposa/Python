
def user_print(*k):
    myList = [str(item) for item in k]
    finalStr = ''.join(myList)
    print(finalStr)

val2 = 3
user_print("val1", " " , val2)


