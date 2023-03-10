
# menbership operator
y = ("tom", "tin", "gone")
x = "tin"
if "go" not in  y:
    print("the comparison is true")
else:
    print("the comparison is false")
# dictinary of male and female animals
def main():
    animals = {"cock" : "cockerel", "he_goat" : "she_goat", "lamb" : "sheep", "dog" : "dog"}
    male_female_animals(animals)
    for k, v in animals.items():
        print(f"{k} : {v}")
def male_female_animals(n):
    for i in n:
        print(f"the male is {i} and their female is  {n[i]}")
main()
