import numpy as np
import pandas as pd

def importar_datos():
    try:
        # Para simplificar, creamos un DataFrame con datos de ejemplo
        data = {
            'Nombre': ['Estudiante' + str(i) for i in range(1, 21)],
            'Parcial 1': np.random.randint(50, 100, 20),
            'Parcial 2': np.random.randint(50, 100, 20),
            'Parcial 3': np.random.randint(50, 100, 20)
        }
        df = pd.DataFrame(data)
        df.to_excel('calificaciones.xlsx', index=False)
        print("Datos importados con éxito.")
        return df.values
    except Exception as e:
        print(f"Error al importar datos: {e}")
        return None

def mostrar_datos(orig_data):
    try:
        print(orig_data)
        print("Datos mostrados con éxito.")
    except Exception as e:
        print(f"Error al mostrar datos: {e}")

def calcular_calificaciones_finales(orig_data):
    try:
        copy_data = np.copy(orig_data)
        finales = (copy_data[:,1] * 0.25 + copy_data[:,2] * 0.25 + copy_data[:,3] * 0.50).reshape(-1, 1)
        print("Calificaciones finales calculadas con éxito.")
        return np.hstack((copy_data, finales))
    except Exception as e:
        print(f"Error al calcular calificaciones finales: {e}")
        return None

def exportar_a_excel(data):
    try:
        df = pd.DataFrame(data, columns=['Nombre', 'Parcial 1', 'Parcial 2', 'Parcial 3', 'Final'])
        df.to_excel('calificaciones_finales.xlsx', index=False)
        print("Datos exportados a Excel con éxito.")
    except Exception as e:
        print(f"Error al exportar datos: {e}")

def main():
    orig_data = None
    final_data = None
    
    while True:
        print("---- Menú ----")
        print("1. Importar Datos")
        print("2. Mostrar datos sin calificaciones finales")
        print("3. Calcular calificaciones finales")
        print("4. Mostrar lista con calificaciones finales")
        print("5. Exportar a Excel")
        print("6. Salir")
        
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            orig_data = importar_datos()
        elif opcion == 2:
            if orig_data is not None:
                mostrar_datos(orig_data)
            else:
                print("Primero importa los datos.")
        elif opcion == 3:
            if orig_data is not None:
                final_data = calcular_calificaciones_finales(orig_data)
            else:
                print("Primero importa los datos.")
        elif opcion == 4:
            if final_data is not None:
                mostrar_datos(final_data)
            else:
                print("Primero calcula las calificaciones finales.")
        elif opcion == 5:
            if final_data is not None:
                exportar_a_excel(final_data)
            else:
                print("Primero calcula las calificaciones finales.")
        elif opcion == 6:
            break
        else:
            print("Opción inválida, intenta de nuevo.")
    
if __name__ == "__main__":
    main()
