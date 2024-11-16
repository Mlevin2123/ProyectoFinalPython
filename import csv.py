import csv

# ----------------- FUNCTION TO READ THE CSV FILE ---------------------------------------------
def alphabetic_order():
    my_order = []
    try:
        with open('contacts_list.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # Validate row data to ensure it has exactly three elements
                if len(row) < 3:
                    print(f"Fila {i + 1} incompleta y será omitida: {row}")
                    continue
                name, phone, email = row[:3]  # Extract first three elements
                my_order.append([name, phone, email])
    except FileNotFoundError:
        print("El archivo 'contacts_list.csv' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

    # Sort list alphabetically by name using merge sort
    alphabetic_order_list = ordenamiento_por_mezcla(my_order)
    return alphabetic_order_list

# ----------------- FUNCTION TO SORT THE LIST ALPHABETICALLY ------------------------------------
def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # Recursive call for both halves
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Indices for traversing the sublists
        i, j, k = 0, 0, 0

        # Main merging loop
        while i < len(izquierda) and j < len(derecha):
            # Sorting by first element (name), assuming name is at index 0
            if izquierda[i][0].lower() <= derecha[j][0].lower():
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Remaining elements in izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Remaining elements in derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista
