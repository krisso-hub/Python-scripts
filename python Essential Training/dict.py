# searchable list of keys and values
x = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5}

x["two"] = 22
for i in x:
    print("i is {}".format(i))

for k, v in x.items():
    print("k is {}, and v is {}".format(k,v))

print(type(x))
print(id(x))
print(type(x["one"]))