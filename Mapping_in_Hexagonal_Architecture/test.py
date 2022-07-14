x = {
    (2, 3): 7,
    (3, 4): 8

}

temp = (2, 3)
x[temp] = 9
print(x)
print(temp in x.keys())
