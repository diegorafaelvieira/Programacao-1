time1 = 0
time2 = 0
time2f = 0
while True:
    sexo = input("Informe o sexo (m)asculino ou (f)eminino:")
    if sexo == "sair":
        break
    time = int(input("Informe o time (1)Grêmio ou (2)Internacional:"))
    if time==1:
        time1+=1
    elif time==2:
        time2+=1
        if sexo=="f":
            time2f+=1
print("Torcedores do Grêmio:",time1)
print("Torcedores do Internacional:",time2)
print("Torcedoras do Internacional:",time2f)  
