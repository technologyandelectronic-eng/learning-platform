# Importar clase Calculator desde src/main.py
from src.main import Calculator


# Función de prueba
# pytest detecta automáticamente funciones que empiezan por test_
def test_add():

    # Crear objeto Calculator
    calculator = Calculator()

    # Ejecutar método add
    result = calculator.add(2, 3)

    # Verificar que resultado sea 5
    # Si no es 5, pytest genera error
    assert result == 5