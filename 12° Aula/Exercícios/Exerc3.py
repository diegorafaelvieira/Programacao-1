def parImpar(v):
    if v%2==0:
        return True
    else:
        return False

for i in range (0,100):
    if parImpar(i):
        print(i)
