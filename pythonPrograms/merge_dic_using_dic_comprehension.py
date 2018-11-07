d1 = {"vik":10, "prav":20, "kal":30, "sai":40}

d2 = {"vik":100, "prav":200, "kal":300, "anil":400}

'''
finalD = {}
for key in d1.keys():
    finalD[key] = d1[key] + d2[key]
print(finalD)
'''

print("d1 = ",d1)
print("d2 = ",d2)

finalD = {key:d1.get(key,0)+d2.get(key,0) for key in set(d1)}
print("Only d1",finalD)

finalD = {key:d1.get(key,0)+d2.get(key,0) for key in (set(d1) & set(d2))}
print("Only d1&d2",finalD)

finalD = {key:d1.get(key,0)+d2.get(key,0) for key in (set(d1) | set(d2))}
print("Only d1|d2",finalD)

finalD = {key:d1.get(key,0)+d2.get(key,0) for key in (set(d1) - set(d2))}
print("Only d1-d2",finalD)

finalD = {key:d1.get(key,0)+d2.get(key,0) for key in (set(d1)^set(d2))}
print("Only d1 xOR d2",finalD)
