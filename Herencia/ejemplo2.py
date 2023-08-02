# Ejemplo de jerarquía de herencia a la hora de gestionar excepciones
try:
    # a = 5/0
    j = 5.0
    for i in range(1, 1000):
        j = j**i
        print(j)
except OverflowError as e:
    print(f"ERROR de representación numérica: {e}")
except ZeroDivisionError as e:
    print(f"ERROR de división entre cero: {e}")
except ArithmeticError as e:
    print(f"ERROR aritmético: {e}")
except Exception as e:
    print(f"ERROR general: {e}")
