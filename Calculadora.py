def get_user_input():
    
    try:
        
        # Aquí se dice al usuario que ingrese dos números y la operación que desea.
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    
    except ValueError:
        # Excepción en caso de que el usuario ingrese algo que no sea un número.
        print("Input invalido. Por favor ingrese numeros.\n")
        return get_user_input() # Se solicita al usuario que digíte de nuevo los números.

def ejecutar_operacion(user_input, operations):
    num1, num2, operation = user_input
    
    # Condicional para verificar si la operación elegida es válida y, si es así, realizarla.
    if operation in operations:
        result = operations[operation](num1, num2)
        
    else:
        result = "Operacion invalida.\n"
    
    # Imprime resultado.
    print("Resultado:", result, "\n")

def main():
    # Se usa lambda para definir un diccionario de operaciones.
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    while True:
        
        # Obtiene la entrada del usuario.
        user_input = get_user_input()

        # Condicional que verifica si elusuario desea salir.
        if user_input[2].lower() == 'exit':
            print("Salir.\n")
            break

        # Ejecutar operación e imprimir resultado.
        print("\nCalculando...")
        ejecutar_operacion(user_input, operations)

if __name__ == "__main__":
    main()
