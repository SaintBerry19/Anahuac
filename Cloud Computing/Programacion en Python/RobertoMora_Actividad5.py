import matplotlib.pyplot as plt
import numpy as np

def graficar_linea_recta():
    m = float(input("Introduce el valor de m: "))
    b = float(input("Introduce el valor de b: "))
    
    # Definir valores para x y calcular y = mx + b
    x = np.linspace(-10, 10, 400)
    y = m * x + b
    
    plt.plot(x, y, label=f"y = {m}x + {b}")
    plt.title("Gráfica de una Línea Recta")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_ecuacion_cuadratica():
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    c = float(input("Introduce el valor de c: "))
    
    # Definir valores para x y calcular y = ax^2 + bx + c
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    plt.plot(x, y, label=f"y = {a}x^2 + {b}x + {c}")
    plt.title("Gráfica de una Ecuación Cuadrática")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Graficar Línea Recta")
        print("2. Graficar Ecuación Cuadrática")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            graficar_linea_recta()
        elif opcion == "2":
            graficar_ecuacion_cuadratica()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
