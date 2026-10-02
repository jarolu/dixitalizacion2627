# Conversor de temperaturas
# Escribe un programa que pida al usuario una temperatura en grados Celsius y la convierta a Fahrenheit y Kelvin.


t_celsius = float(input("Escribe la temperatura en grados Celsius: "))

t_fahrenheit = t_celsius*1.8 + 32

t_kelvin = t_celsius + 273.15

print(f"{t_celsius}º Celsius equivale a {t_fahrenheit}º Fahreint y a {t_kelvin}º Kelvin")