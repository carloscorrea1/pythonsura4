## Entradas = variables = referencias en memoria.
## None es para asignar valor.
## Mensaje de entrada.

nivelAgua=int (input("Digite el nivel del agua: "))

## PROCESO
if(nivelAgua>=0 and nivelAgua<20):
    print(f'el nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua>=20 and nivelAgua < 400):
    print(f'el nivel de agua es {nivelAgua} operando normalmente')
elif(nivelAgua>=400):
    print(f'el nivel de agua es {nivelAgua} llamen a fico')
else:
    print("el nivel de agua no es")

## 