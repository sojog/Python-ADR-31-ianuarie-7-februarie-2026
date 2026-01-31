
# x = "hello"

# if x:
#     print("Conditia este adevarata")
# else:
#     print("Conditia este falsa")



varsta = 20

## VARIANTA 1 - nested
if varsta < 18:
    print("Minor")
else:
    if varsta < 35:
        print("Tanar")
    else:
        if varsta < 65:
            print("Adult")
        else:
            print("Pensionar")


## Varianta 2 - flat (PREFERATA)
if varsta < 18:
    print("Minor")
elif varsta < 35:
    print("Tanar")
elif varsta < 65:
    print("Adult")
else:
    print("Pensionar")