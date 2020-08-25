from random import randint

moderno=0
rio=1
salteado=0
sorteio = []

#Gerador Dos Numeros da lista

i=0
while(i<5):
    sorteio.append(randint(1000,9999))
    i+=1


print(sorteio)

#Moderno
for numerosL in sorteio:
    moderno+=numerosL
moderno=moderno%1000
sorteio.append(moderno)

#Rio---PRECISO TERMINAR
rio=(sorteio[0]*sorteio[1])

if(rio>=10000000):
    rio =(rio%1000000)/1000
else:
    rio = (rio % 100000) / 100
sorteio.append(int(rio))

#Salteado
salteado=(sorteio[0]%100)*4

sorteio.append(salteado)

print(sorteio)