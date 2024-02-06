word = "draW, Skate, photo"
hobby = word.split(",")
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ".join(hobby)
print(result)
