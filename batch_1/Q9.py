d={'Hritik':6.9*10,'Debarpan':7.3*10,'Suvendu':7.1*10,'Avas':5.5*10}

def sortRuns(d):
    d1={}
    for key,val in d.items():
        d1[val]=key 
    
    print(d1)
    sortRun=list(d1.keys())
    sortRun.sort(reverse=True)
    d2={}
    for i in sortRun:
        d2[i]=d1[i]

    d1={}
    for key,val in d2.items():
        d1[val]=key 
    
    print("After sort run wise desc Ord :",d1)

sortRuns(d) 


# maximum run
run=0
name = None
for key,val in d.items():
    if val > run:
        run=val
        name=key

print('Name : ',name,' Run : ',run)

#name of bats man are 
print('Name of Bats Man Are :',list(d.keys()))

d.update({'Supratim':8.3*10})
print('Name of Bats Man Are :',list(d.keys()))

# Remove the bats man for lowest run
run=max(list(d.values()))
# print(run)
name = None
for key,val in d.items():
    if val < run:
        run=val
        name=key

print('Delete Batsman Name : ',name)
del d[name]
print("After delete lowest",d)

