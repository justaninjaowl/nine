x = ""
i = ""
while x == "":
    print("Input a number larger than 9")
    x = input()
    if int(x) <= 9:
        print("invalid number")
        x = ""
while int(x) != 9:
    x = str(x)
    takeaway = sum(int(digit) for digit in x)
    for digit in x:
        i += str(digit + " + ")
    else:
        i = i[0:(len(i) - 2)]
    i += str("= " + str(takeaway))
    print(i)
    i = ""
    print(x + " - " + str(takeaway) + " = " + str((int(x) - int(takeaway))))
    x = int(x) - int(takeaway)
    print(x)
else:
    input()
