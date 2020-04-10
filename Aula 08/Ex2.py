valor = 0
contador = 1
for n in range(64,547):
    if n%2==0:
        if contador%2==0:
            print("Pong")
        else:
            print("Ping")
        contador+=1
    else:
        print(n)
    valor+=1
    
