# Clase Calculator
# Representa una calculadora simple
class Calculator:

    # Método para sumar dos números
    # a: primer número entero
    # b: segundo número entero
    # return: resultado de la suma
    def add(self, a: int, b: int) -> int:

        # Retorna suma de a + b
        return a + b


# Crear objeto de la clase Calculator
calculator = Calculator()

# Ejecutar método add
result = calculator.add(5, 3)

# Mostrar resultado en consola
print(result)