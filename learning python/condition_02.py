# conditional statement

y = 10
x = 10

if (x > y):
    st = "x is greater than y"
elif (x == y):
    st = "x is the same as y"
else:
    st = "x is less than y"
print(st)

st = "x is less than y" if (x< y) else "x is greater than y or the same as y"
print(st)


# for loop, looping over days of the week

days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
for i, d in enumerate(days):
    
    if (d == "wed"): continue
    print(i, d)

# for loop, looping over some range of numbers with condition

for x in range(2, 15):
    if(x %2 == 0): continue
    print(x, end = " ")


