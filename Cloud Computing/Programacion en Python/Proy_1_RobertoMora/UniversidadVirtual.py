import datetime

def main():
    # Mensaje de bienvenida
    print("¡Bienvenido al Proyecto_1_UniversidadVirtual!")
    
    # Solicitar el nombre del usuario
    nombre = input("Por favor, ingresa tu nombre: ")

    # Solicitar fecha de nacimiento y asegurarse de que esté en el formato correcto
    while True:
        fecha_nacimiento_str = input("Por favor, ingresa tu fecha de nacimiento en formato dd-mm-aaaa: ")
        try:
            fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, '%d-%m-%Y').date()
            break
        except ValueError:
            print("Formato incorrecto. Inténtalo nuevamente.")
    
    # Mostrar fecha de nacimiento en formato aaaa-mm-dd
    print(f"Tu fecha de nacimiento en formato aaaa-mm-dd es: {fecha_nacimiento.strftime('%Y-%m-%d')}")

    # Calcular edad usando la fecha de nacimiento y tomando en cuenta si el usuario ya cumplio o no anios, si el statement es true se resta 1 anio, de lo contrario false = 0 no se resta.
    today = datetime.date.today()
    edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    # Guardar datos en un archivo de texto
    with open("datos.txt", "w") as file:
        file.write(nombre + "\n")
        file.write(fecha_nacimiento_str + "\n")
        file.write(str(edad) + "\n")

    print("Los datos han sido guardados en el archivo 'datos.txt'.")

if __name__ == "__main__":
    main()
