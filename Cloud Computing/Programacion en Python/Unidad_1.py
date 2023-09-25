import datetime

def obtener_nombre():
    return input("Por favor, escribe tu nombre: ")

def obtener_genero():
    while True:
        genero = input("Por favor, escribe tu género (M o F): ").upper()
        if genero in ['M', 'F']:
            return genero
        else:
            print("Por favor, introduce una opción válida.")

def obtener_ano_nacimiento():
    while True:
        try:
            year = int(input("Por favor, escribe tu año de nacimiento: "))
            return year
        except ValueError:
            print("Por favor, introduce un año válido.")

def calcular_edad(year):
    current_year = datetime.datetime.now().year
    return current_year - year

def main():
    print("¡Bienvenido al programa!")
    print("Se te solicitarán algunos datos personales.")
    
    while True:
        nombre = obtener_nombre()
        genero = obtener_genero()
        year = obtener_ano_nacimiento()
        edad = calcular_edad(year)

        if genero == 'M':
            print(f"Bienvenido {nombre}, tu edad es {edad}")
        else:
            print(f"Bienvenida {nombre}, tu edad es {edad}")

        repetir = input("¿Deseas calcular la edad para otro usuario? (s/n): ").lower()
        if repetir != 's':
            print("Gracias por participar, adios!")
            break

main()
