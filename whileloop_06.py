secret = "funky"
pw = ""
count = 0
max_count = 5
while pw != secret:
    count += 1
    pw = input(f"{count}: whats the secret word? ")
    if count == 4: break
    if pw == "funky":
        print("good job")
    else:
        print("try again")