def powTwo(maxV):
    x = 0
    while (x<= maxV):
        yield 2**x
        x+=1

poIt = powTwo(2)
print(next(poIt))
print(next(poIt))
print(next(poIt))
print(next(poIt))
print(next(poIt))

