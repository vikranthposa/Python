def multiplierOf(x):
    def mul(n,m):
        #x = 50 #what happens if we uncomment it
        return x*n*m
    return mul

mul10 = multiplierOf(10)
mul4 = multiplierOf(4)

print(mul10(2,3))
print(mul4(2,3))
