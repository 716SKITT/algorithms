n = int(input("enter lenght: "))
user_list = []
i = 0
while i < n:
    string = "Enter element #" + str(i + 1) + ":"
    user_list.append((int(input(string))))
    i += 1

print((user_list))