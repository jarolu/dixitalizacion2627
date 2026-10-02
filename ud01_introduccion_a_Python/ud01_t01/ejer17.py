# Crea una clase Rectangulo con atributos ancho y alto. Incluye métodos para calcular área y perímetro.


class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base*2 + self.altura*2


if __name__ == "__main__":

    b = int(input("Introduce la base del rectángulo: "))
    a = int(input("Introduce la altura del rectángulo: "))
    rect = Rectangulo(b,a)

    print(f"El rectangulo tiene base {rect.base} y altura {rect.altura}.")

    print(f"Su área es {rect.area()} y su perímetro {rect.perimetro()}.")