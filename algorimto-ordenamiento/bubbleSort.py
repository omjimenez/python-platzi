# 1. comenzar a hacer comparaciones de elementos adyacentes
# 2. Repetir hasta tener una pasada completa sin ningun swap.

def bubbleSort(array):
    n = len(array)

    for i in range(n):
        print(f' --- Array ciclo {i} ')
        for j in range(0, n-i):
            #print(f'array {j} -- {n-i-1}')
            #print(array[j])
            #print(f'array[{j}] > array[{j+1}] {array[j]}  {array[j+1]}')
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    array = [190, 1200, 1, 2, 4, 55, 1000, 6, 800]
    print(array)

    array_result = bubbleSort(array)

    print("El arreglo ordenado de forma Ascendente es: ")

    for i in range(len(array_result)):
        print("%d"%array_result[i])

