somaNotas = 0
alunos = 0
while True:
    nota = float(input("Informe uma nota: "))
    if nota==11:
        break
    alunos+=1
    somaNotas+=nota
if alunos==0:
    print("Sem notas.")
else:    
    print(somaNotas/alunos) 
