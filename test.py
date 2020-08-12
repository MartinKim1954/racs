DEFAULT = 0
x = 0x01
y = 0x02
z = 0x04

DEFAULT_1 = DEFAULT | x | y | z
print(DEFAULT_1)

DEFAULT_1 = DEFAULT_1 & ~y

print(DEFAULT_1)

if DEFAULT_1 & y:
    print("y is there")
else:
    print("y is not there")