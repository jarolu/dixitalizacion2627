# Números pares e impares
# Solicita al usuario una lista de números separados por espacios y muestra dos listas: una con los pares y otra con los impares.



lista_numeros = list(map(int, input("Introduce una lista de números separada por espacios: ").split()))

lista_pares = [n for n in lista_numeros if n%2==0]

lista_impares = [n for n in lista_numeros if n%2!=0]

print("La lista de números pares es: ",*lista_pares)

print("La lista de números impares es: ",*lista_impares)