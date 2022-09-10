#!/usr/bin/python3
for n in range(0, 100):
    if (n == 99):
        continue
    print("{:02d}".format(n), end=", ")
print("99")
