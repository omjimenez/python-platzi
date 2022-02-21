# Buscar el numero menoren mi array.
# Crear dos sub-arrays para llevar el control del algoritmo
# Imprimir el resultado del ordenamiento

def selectionSort(array):
    # recorrer todo el array
    for i in range(len(array)):

        # Encontrar el valor minimo restante dentro del array desordenado
        idxDesordenado = i
        for j in range(i+1, len(array)):
            if array[idxDesordenado] > array[j]:
                idxDesordenado = j

        # ya que encontramos el minimo lo vamos a cambiar 
        # por el primer valor de nuestro array desordenado

        array[i], array[idxDesordenado] = array[idxDesordenado], array[i]

    return array


if __name__ == '__main__':
    array = [20, 5, 21, 6, 23, 7, 34, 999, 68]

# ejecutar la funcion
array_ordenado = selectionSort(array)

print("Arrary Ordenando")

for idx in range(len(array_ordenado)):
    print("%d" %array_ordenado[idx])
