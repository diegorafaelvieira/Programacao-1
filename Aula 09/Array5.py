
l = []

for i in range(0,5):
    nota = int(input("NOTA: "))
    l.append(nota)

soma = 0
for v in l:
    soma += v
    media = (soma / len(l))

print("SOMA:",soma)
print("MEDIA:",media)
