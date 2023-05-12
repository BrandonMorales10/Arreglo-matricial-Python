import csv

def load_data():
    choice = input("¿Deseas cargar los datos desde un archivo? (s/n): ")
    if choice.lower() == 's':
        file_name = input("Ingresa el nombre del archivo: ")
        try:
            with open(file_name) as file:
                reader = csv.reader(file)
                next(reader) # Saltar la primera fila (encabezados)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            print("No se encontró el archivo. Por favor, inténtalo de nuevo.")
            return load_data()
    elif choice.lower() == 'n':
        data = []
        while True:
            name = input("Ingresa el nombre del individuo (o 'q' para terminar): ")
            if name.lower() == 'q':
                break
            birth_date = input("Ingresa la fecha de nacimiento (en formato DD/MM/AAAA): ")
            data.append([name, birth_date])
        return data
    else:
        print("Opción no válida. Por favor, inténtalo de nuevo.")
        return load_data()

def sort_data(data):
    sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
    return sorted_data

data = load_data()
sorted_data = sort_data(data)

print("Datos ordenados en orden alfabético por nombre y por fecha de nacimiento:")
for row in sorted_data:
    print(row[0], "-", row[1])

## Brandon Morales https://www.instagram.com/lewenn19/