
# Muiltiplication Table
# Print title
print("          Muiltiplication Table")

print("   |", end =" ")
for i in range(1, 10):
    print(format(i, "3d"), end= " ")
# Display empty line
print()
print("________________________________________")

for i in range(1, 10):
    print(i, " |",  end = " ")
    for j in range(1, 10):
        print(format(i * j, "3d"), end = " " )
# Move to a new line
    print()
