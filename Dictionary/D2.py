# d1 = {1: ‘a’, 2: ‘b’, 3: 120}, then d2 = {‘a’: 1, 2: ‘b’, 120: 3}.

d1 = {1: 'a', 2: 'b', 3: 120}
keys=list(d1.keys())
values=list(d1.values())

d2={}
for i in range(len(keys)):
    d2[values[i]]=keys[i]

print(d2)