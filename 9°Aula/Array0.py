n = 5
array = []

for x in range(0,n):
    v = int(input("INFORME UM VALOR: "))
    array.append(v)

s = 0
for v in array:
    s += v

print("")
print(s/n)
