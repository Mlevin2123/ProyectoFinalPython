import csv

# -----------------  ---------------------------------------------
def alphabetic_order():
    my_order = []
    try:
        with open('contacts_list.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
               
                if len(row) < 3:
                    print(f"Fila {i + 1} incompleta y será omitida: {row}")
                    continue
                name, phone, email = row[:3]  
                my_order.append([name, phone, email])
    except FileNotFoundError:
        print("El archivo 'contacts_list.csv' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

    # Ordenar la lista alfabéticamente por nombre mediante la ordenación por combinación
    alphabetic_order_list = ordenamiento_por_mezcla(my_order)
    return alphabetic_order_list

# ----------------- FUNCIÓN PARA ORDENAR LA LISTA ALFABÉTICAMENTE ------------------------------------
def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # Llamada recursiva para ambas mitades
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Índices para recorrer las sublistas
        i, j, k = 0, 0, 0

        # funcion principal
        while i < len(izquierda) and j < len(derecha):
            # Ordenando por primer elemento (nombre), asumiendo que el nombre está en el índice 0
            if izquierda[i][0].lower() <= derecha[j][0].lower():
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Elementos restantes en izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # elementos a la derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

