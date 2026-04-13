try:
    a = int(input("ingresa el primer numero:"))
    b = int(input("ingrese el segundo numero:")) 
    resultado = a/b
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("No se puede  dividir por 0")

except ValueError:
    print("Debe ingresar solo numeros")

finally:
    print("Fin")



class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    else:
        print(f"Edad válida: {edad}")

try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)

except EdadInvalidaError as e:
    print(f"Error: {e}")

except ValueError:
    print("Debes ingresar un número válido")
