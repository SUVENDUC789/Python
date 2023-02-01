d = {}

# Add in dictionary
d["suv"] = "python"
d["sup"] = "angular"
d["debu"] = "python"
d["hri"] = "java"

# print(3+1+2+1+1+1)
print(d.keys())
print(d.values())
print(d.items())


d.update({"hri": "try to convince"})  # change the previous key wise value
d.update({"swati": "try to convince"})  # add last key and value
print(d)


print(d.get('suv'))  # get key wise value in dictionary
d2 = d  # two reference variable point two the same object
d2 = d.copy()  # d2 containt new copy object


del d["hri"]# delete in dictionary
print(d.pop("sup"))  # it return value of key
d.clear()  # Empty dictionary
del d # delete whole dictionary
print(d)
