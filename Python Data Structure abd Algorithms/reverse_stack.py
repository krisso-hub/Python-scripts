
import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
co = stack.Stack()

for char in string:
    co.push(char)

while not co.is_empty():

    reversed_string += co.pop()

print(reversed_string)