name = 'Roger'
last_name = 'Guevara'
#porque sí
saludo = 'Hola ' + name + ' ' + last_name + 'Como estas?'
print(saludo)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b

def calcular_expresion(expresion):
    """
    Evalúa una expresión matemática combinada escrita como cadena de texto.
    Ejemplo: '2 + 3 * 4 - 5 / 2'
    """
    try:
        resultado = eval(expresion, {"__builtins__": None}, {})
        return resultado
    except Exception as e:
        return f"Error en la expresión: {e}"

# Ejemplo de uso:
exp = "2 + 8 * 0 - 5 / 5"
print(f"Resultado de '{exp}' = {calcular_expresion(exp)}")

